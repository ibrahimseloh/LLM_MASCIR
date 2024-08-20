from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Scopes requis pour accéder à l'API Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

# Chemin vers le fichier credentials.json
CREDENTIALS_FILE = 'fichier-credential' #fichier-credential.json-à télécharger depuis la plateforme google console

def authenticate_google():
    # Initialiser le flux OAuth et demander l'authentification
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    return creds

def ask_meeting_details():
    # Demander à l'utilisateur de saisir le jour, l'heure, le titre de la réunion, l'adresse e-mail du destinataire
    title = "RDV médicale"
    description = "Court entretien avec le médecin pour checker l'état de santé du patient"
    email = input("Entrez l'adresse e-mail du médecin (ex: medecin@example.com) : ")

    date_input = input("Quel est le jour de la réunion ? (format: YYYY-MM-DD) : ")
    start_time_input = input("À quelle heure commence la réunion ? (format: HH:MM) : ")
    end_time_input = input("À quelle heure se termine la réunion ? (format: HH:MM) : ")

    # Créer les datetime au format ISO 8601
    start_datetime = f"{date_input}T{start_time_input}:00"
    end_datetime = f"{date_input}T{end_time_input}:00"

    return title, description, email, start_datetime, end_datetime

def create_google_meet(creds, title, description, email, start_datetime, end_datetime):
    service = build('calendar', 'v3', credentials=creds)

    # Détails de la réunion
    event = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'Europe/Paris',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Europe/Paris',
        },
        'conferenceData': {
            'createRequest': {
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet'
                },
                'requestId': 'random-string'
            }
        },
        'attendees': [
            {'email': email},
        ],
    }

    event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    print(f"Réunion créée: {event.get('htmlLink')}")
    return event.get('hangoutLink')

def send_email(meeting_link, email):
    sender_email = input("Entrez votre e-mail (ex: votre-email@gmail.com) : ")
    password = input("Entrez votre mot de passe d'application : ")  # Utilisez un mot de passe d'application si nécessaire

    # Configurer le serveur SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Créer le message e-mail
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = email
        message['Subject'] = "Lien de la Réunion Google Meet"

        body = f"Voici le lien de votre réunion Google Meet : {meeting_link}"
        message.attach(MIMEText(body, 'plain'))

        # Envoyer l'e-mail
        server.send_message(message)
        print(f"E-mail envoyé à {email} avec le lien de la réunion.")
    except smtplib.SMTPAuthenticationError:
        print("Erreur d'authentification : Vérifiez votre adresse e-mail et votre mot de passe.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
        server.quit()

if __name__ == '__main__':
    creds = authenticate_google()
    title, description, email, start_datetime, end_datetime = ask_meeting_details()
    meeting_link = create_google_meet(creds, title, description, email, start_datetime, end_datetime)
    send_email(meeting_link, email)
