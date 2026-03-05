# Project App - Django Study Buddy

This is a Django-based study buddy application with AI integrations (Gemini), document summarization, quizzes, and study planning.

## Tech Stack
- Django (Web Framework)
- Vanilla CSS (Styling)
- Google Gemini API (AI Features)
- SQLite (Local Database)
- WhiteNoise (Static File Management)
- Vercel (Deployment)

---

## Local Setup
1. **Clone the repo.**
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate # On Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup Environment Variables:**
   - Create a `.env` file from the placeholder in `.env.example` (or as provided):
     ```text
     GEMINI_API_KEY=your_key
     SECRET_KEY=your_secret_key
     DEBUG=True
     ALLOWED_HOSTS=*
     ```
5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Stat the Server:**
   ```bash
   python manage.py runserver
   ```

---

## Deployment (Vercel)
The project is configured for Vercel using `vercel.json` and `wsgi.py`.
To deploy:
1. Push to GitHub.
2. Link the repository to Vercel.
3. **Important**: Add environment variables (`GEMINI_API_KEY`, `SECRET_KEY`, `DEBUG=False`) in the Vercel project settings.

## Contributing
Please feel free to contribute to this project.
