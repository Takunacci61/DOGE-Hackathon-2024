# LincolnAI

LincolnAI is a powerful application designed to simplify visa navigation and provide access to essential government services. Built with **Flutter** for the front end and **Django** for the back end, the app leverages xAI's Grok to deliver a seamless user experience.

## Features
- Search visa options based on destination, purpose, and nationality.
- Summarise visa requirements with links to official government websites.
- Future integrations for services like tax and healthcare.

## Tech Stack
- **Frontend**: Flutter
- **Backend**: Django
- **AI Integration**: xAI's Grok

## Installation
1. Clone the repository.
2. Set up the Django backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
3. Set up the Flutter frontend:
   ```bash
   cd frontend
   flutter pub get
   flutter run
   ```

## License
This project is open-source and available under the MIT License.
