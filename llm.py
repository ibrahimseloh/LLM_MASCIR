import os
import openai
import speech_recognition as sr
from pygame import mixer
from gtts import gTTS
import psycopg2
from datetime import datetime
import googleapiclient.discovery
import googleapiclient.errors
import yt_dlp as youtube_dl
import vlc
from meet import authenticate_google, ask_meeting_details, create_google_meet, send_email


# Clés API
openai.api_key = 'ENTER-open-ai-api-key'

# Informations de connexion à la base de données PostgreSQL
dbname = "ENTER-Data-Base-Name"
user = "postgres"
password = "ENTER-Password"
host = "localhost"

# Connexion à la base de données PostgreSQL
try:
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    print("Connexion à la base de données réussie.")
except psycopg2.Error as e:
    print("Erreur lors de la connexion à la base de données:", e)

# Configurez l'API key YouTube
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "ENTER-youtube-API-KEY"

# Classe pour gérer la reconnaissance vocale et la synthèse vocale
class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.language = "fr-FR"
    
    def asr(self):
        with sr.Microphone() as source:
            print("Veuillez parler maintenant.")
            audio = self.recognizer.listen(source)

        try:
            user_input = self.recognizer.recognize_google(audio, language=self.language)
            print("Vous avez dit: " + user_input)
            return user_input
        except sr.UnknownValueError:
            print("La reconnaissance vocale n'a pas pu comprendre l'audio.")
            return None
        except sr.RequestError as e:
            print(f"Erreur lors de la requête à Google Speech Recognition service: {e}")
            return None
    
    def tts(self, output):
        try:
            tts = gTTS(text=output, lang='fr')
            name_file = "output.mp3"
            tts.save(name_file)

            mixer.init()
            mixer.music.load(name_file)
            mixer.music.play()

            while mixer.music.get_busy():
                pass

            mixer.music.stop()
            mixer.music.unload()
            mixer.quit()

            os.remove(name_file)
        except Exception as e:
            print(f"Erreur lors de la synthèse vocale: {e}")

# Classe pour gérer les interactions avec la base de données
class DatabaseManager:
    def __init__(self, connection):
        self.conn = connection
    
    def check_user_in_db(self, first_name, last_name):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM ElderlyUsers WHERE first_name = %s AND last_name = %s", (first_name, last_name))
            users = cur.fetchall()
            cur.close()
            return users
        except psycopg2.Error as e:
            print("Erreur lors de la vérification de l'utilisateur dans la base de données:", e)
            return None
    
    def check_room_number(self, first_name, last_name, room_number):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM ElderlyUsers WHERE first_name = %s AND last_name = %s AND room_number = %s", (first_name, last_name, room_number))
            user = cur.fetchone()
            cur.close()
            return user
        except psycopg2.Error as e:
            print("Erreur lors de la vérification du numéro de chambre:", e)
            return None
    
    def insert_health_info(self, first_name, last_name, physical_state, mental_state, last_meal_time, meal_content):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO HealthInfo (first_name, last_name, physical_state, mental_state, last_meal_time, meal_content)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, physical_state, mental_state, last_meal_time, meal_content))
            self.conn.commit()
            cur.close()
            print("Informations de santé enregistrées avec succès.")
            return True
        except psycopg2.Error as e:
            print("Erreur lors de l'enregistrement des informations de santé:", e)
            return False
    
    def insert_user_info(self, first_name, last_name, age, gender, room_number, medical_conditions, allergies, caregiver_contact, emergency_contact_name, emergency_contact_number):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO ElderlyUsers (first_name, last_name, age, gender, room_number, medical_conditions, allergies, caregiver_contact, emergency_contact_name, emergency_contact_number)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, age, gender, room_number, medical_conditions, allergies, caregiver_contact, emergency_contact_name, emergency_contact_number))
            self.conn.commit()
            cur.close()
            print("Informations utilisateur enregistrées avec succès.")
            return True
        except psycopg2.Error as e:
            print("Erreur lors de l'enregistrement des informations utilisateur:", e)
            return False
    
    def insert_medication_info(self, first_name, last_name, medication_name, dose_taken):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO MedicationInfo (first_name, last_name, medication_name, dose_taken)
                VALUES (%s, %s, %s, %s)
            """, (first_name, last_name, medication_name, dose_taken))
            self.conn.commit()
            cur.close()
            print("Informations sur la prise de médicaments enregistrées avec succès.")
            return True
        except psycopg2.Error as e:
            print("Erreur lors de l'enregistrement des informations sur la prise de médicaments:", e)
            return False
    
    def insert_music_preferences(self, first_name, last_name, music_preferences):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO MusicPreferences (first_name, last_name, preferences)
                VALUES (%s, %s, %s)
            """, (first_name, last_name, music_preferences))
            self.conn.commit()
            cur.close()
            print("Préférences musicales enregistrées avec succès.")
            return True
        except psycopg2.Error as e:
            print("Erreur lors de l'enregistrement des préférences musicales:", e)
            return False

# Classe pour gérer le divertissement via YouTube
class YouTubeEntertainment:
    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.DEVELOPER_KEY = "ENTER-Youtube-API-KEY"
    
    def search_youtube(self, query):
        youtube = googleapiclient.discovery.build(self.api_service_name, self.api_version, developerKey=self.DEVELOPER_KEY)
        request = youtube.search().list(part="snippet", maxResults=5, q=query)
        response = request.execute()
        return response['items']
    
    def download_and_play(self, video_url):
        try:
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'video.mp4',
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            player = vlc.MediaPlayer('video.mp4')
            player.play()

            while True:
                state = player.get_state()
                if state in [vlc.State.Ended, vlc.State.Error]:
                    break

        except Exception as e:
            print(f"Erreur lors du téléchargement ou de la lecture de la vidéo: {e}")

# Gestion des interactions
class InteractionManager:
    def __init__(self, voice_assistant, database_manager, youtube_entertainment):
        self.voice_assistant = voice_assistant
        self.database_manager = database_manager
        self.youtube_entertainment = youtube_entertainment
        self.first_name = None
        self.last_name = None
    
    def get_user_input(self, mode):
        if mode == '1':  # Manual input
            return input("Vous: ").strip()
        elif mode == '2':  # Voice input
            return self.voice_assistant.asr()
        else:
            print("Mode invalide. Utilisez 1 pour saisie manuelle ou 2 pour saisie vocale.")
            return None
    
    def ask_question(self, question, mode, examples=None, choices=None):
        if examples:
            question += " (Exemple: " + ", ".join(examples) + ")"
        if choices:
            question += " (Choisissez parmi : " + ", ".join(choices) + ")"
        print(f"Bot: {question}")
        self.voice_assistant.tts(question)
        
        user_input = self.get_user_input(mode)
        if choices:
            while user_input not in choices:
                print(f"Bot: Choix invalide. Veuillez choisir parmi : {', '.join(choices)}")
                self.voice_assistant.tts(f"Choix invalide. Veuillez choisir parmi : {', '.join(choices)}")
                user_input = self.get_user_input(mode)
        
        return user_input
    
    def schedule_appointment(self, mode):
        print("Bot: Vous pouvez maintenant prendre un rendez-vous avec votre médecin.")
        self.voice_assistant.tts("Vous pouvez maintenant prendre un rendez-vous avec votre médecin.")
        
        # Authentifier Google Calendar
        creds = authenticate_google()
        
        # Demander les détails de la réunion
        title, description, email, start_datetime, end_datetime = ask_meeting_details()
        
        # Créer la réunion Google Meet
        meeting_link = create_google_meet(creds, title, description, email, start_datetime, end_datetime)
        
        # Envoyer l'e-mail avec le lien de la réunion
        send_email(meeting_link, email)
        
        print(f"Bot: Votre rendez-vous a été pris. Voici le lien pour la réunion : {meeting_link}")
        self.voice_assistant.tts(f"Votre rendez-vous a été pris. Voici le lien pour la réunion : {meeting_link}")



    def handle_conversation(self, mode):
        self.first_name = self.ask_question("Quel est votre prénom ?", mode)
        self.last_name = self.ask_question("Quel est votre nom ?", mode)
        
        users = self.database_manager.check_user_in_db(self.first_name, self.last_name)
        
        if users:
            print(f"Bot: Bonjour {self.first_name} {self.last_name}. Je vais vérifier vos informations.")
        else:
            print("Bot: Vous n'êtes pas encore enregistré. Veuillez fournir les informations suivantes.")
            self.register_user(mode)
        
        self.ask_health_info(mode)
        self.ask_medication_info(mode)
        self.ask_music_preferences(mode)
        
        choice = self.ask_question("Que souhaitez-vous faire maintenant ? Vous pouvez choisir parmi les options suivantes : 1. Continuer la conversation avec l'assistant, 2. Regarder une vidéo, 3. Prendre un rendez-vous avec votre médecin, 4. Arrêter la conversation", mode, choices=["1", "2", "3", "4"])
        
        if choice == "1":
            self.continue_conversation_with_gpt4(mode)
        elif choice == "2":
            self.ask_for_video_preferences_and_play(mode)
        elif choice == "3":
            self.schedule_appointment(mode)
        elif choice == "4":
            self.voice_assistant.tts("Merci et à bientôt!")
            print("Bot: Merci et à bientôt!")
        else:
            print("Bot: Choix invalide. Veuillez réessayer.")
            self.voice_assistant.tts("Choix invalide. Veuillez réessayer.")


    
    def register_user(self, mode):
        age = self.ask_question("Quel est votre âge ?", mode)
        gender = self.ask_question("Quel est votre sexe ?", mode)
        room_number = self.ask_question("Quel est votre numéro de chambre ?", mode)
        medical_conditions = self.ask_question("Quelles sont vos conditions médicales ?", mode)
        allergies = self.ask_question("Avez-vous des allergies ?", mode)
        caregiver_contact = self.ask_question("Quel est le contact de votre soignant ?", mode)
        emergency_contact_name = self.ask_question("Quel est le nom du contact d'urgence ?", mode)
        emergency_contact_number = self.ask_question("Quel est le numéro de téléphone du contact d'urgence ?", mode)
        
        self.database_manager.insert_user_info(
            self.first_name, self.last_name, age, gender, room_number, medical_conditions, allergies, caregiver_contact, emergency_contact_name, emergency_contact_number
        )
    
    def ask_health_info(self, mode):
        physical_state = self.ask_question("Comment vous sentez-vous physiquement aujourd'hui ?", mode)
        mental_state = self.ask_question("Comment vous sentez-vous mentalement aujourd'hui ?", mode)
        last_meal_time = self.ask_question("À quelle heure avez-vous pris votre dernier repas ?", mode)
        meal_content = self.ask_question("Que contenait votre dernier repas ?", mode)
        
        self.database_manager.insert_health_info(
            self.first_name, self.last_name, physical_state, mental_state, last_meal_time, meal_content
        )
    
    def ask_medication_info(self, mode):
        medication_name = self.ask_question("Quel est le nom du médicament pris aujourd'hui ?", mode)
        dose_taken = self.ask_question("Quelle dose avez-vous prise ?", mode)
        
        self.database_manager.insert_medication_info(
            self.first_name, self.last_name, medication_name, dose_taken
        )
    
    def ask_music_preferences(self, mode):
        music_preferences = self.ask_question("Quels sont vos goûts musicaux ?", mode)
        self.database_manager.insert_music_preferences(
            self.first_name, self.last_name, music_preferences
        )
    
    def continue_conversation_with_gpt4(self, mode):
        print("Bot: Je vais continuer la conversation avec le modèle GPT-4.")
        self.voice_assistant.tts("Je vais continuer la conversation avec le modèle GPT-4.")
        
        while True:
            user_input = self.get_user_input(mode)
            if user_input.lower() in ['au revoir', 'bye', 'end']:
                self.voice_assistant.tts("Merci et à bientôt!")
                break
            else:
                response = openai.Completion.create(
                    model="gpt-4",
                    prompt=user_input,
                    max_tokens=150
                )
                reply = response.choices[0].text.strip()
                print("Bot: " + reply)
                self.voice_assistant.tts(reply)
    
    def ask_for_video_preferences_and_play(self, mode):
        video_query = self.ask_question("Quel type de vidéo voulez-vous regarder ?", mode)
        videos = self.youtube_entertainment.search_youtube(video_query)
        
        if videos:
            video_url = f"https://www.youtube.com/watch?v={videos[0]['id']['videoId']}"
            self.youtube_entertainment.download_and_play(video_url)
        else:
            self.voice_assistant.tts("Désolé, je n'ai pas trouvé de vidéos correspondant à votre recherche.")

def main():
    # Initialiser les composants nécessaires
    voice_assistant = VoiceAssistant()
    database_manager = DatabaseManager(conn)
    youtube_entertainment = YouTubeEntertainment()
    interaction_manager = InteractionManager(voice_assistant, database_manager, youtube_entertainment)

    # Choix du mode d'entrée
    mode = input("Choisissez le mode d'entrée (1 pour manuel, 2 pour vocal) : ").strip()
    
    # Gérer la conversation selon le mode sélectionné
    interaction_manager.handle_conversation(mode)

if __name__ == "__main__":
    main()
