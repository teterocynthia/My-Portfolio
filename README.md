# My Portfolio

Personal portfolio website built with Flask, Tailwind CSS and simple templates.

## What I changed
- Personalized homepage (hero + about + skills).
- Visible social links and avatar in the navbar.
- Improved project cards with technologies and links.
- Contact form posts to /contact (server-side flash messages).
- Warmer, more natural color palette (earthy/organic tones instead of synthetic neon blues/gradients).
- Small aesthetic improvements (fonts & layout).

## Quick local setup

1. Clone the repo:
```bash
git clone https://github.com/teterocynthia/My-Portfolio.git
cd My-Portfolio
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# Windows (PowerShell): .\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional) Set your contact email in an env var:
```bash
export CONTACT_EMAIL="you@example.com"   # macOS / Linux
# Windows PowerShell: $env:CONTACT_EMAIL = "you@example.com"
```

5. Run the app:
```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## To customize
- Edit `PROFILE` in `app.py` to add your real name, title, bio, LinkedIn URL, avatar_url, and email.
- Replace images in `static/images/` (project1.jpg, project2.jpg, profile photo).
- Update or add projects in `app.py` under `PROJECTS`.

## Deploy
This app can be deployed to Render, Railway, Heroku, or any host that supports Python apps. For production, run under Gunicorn and set environment variables instead of committing credentials.
