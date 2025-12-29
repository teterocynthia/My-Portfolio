from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

# Personal profile (edit these values to your real info)
PROFILE = {
    "name": "Cynthia",
    "title": "Web Programmer • Frontend-focused",
    "bio": "I build polished, accessible web experiences using Python and modern frontend tools.",
    "about": "Hi — I'm Cynthia, a web programmer who enjoys building user-friendly interfaces and reliable server-side systems. I focus on clarity, accessibility, and performance.",
    "location": "Remote",
    "years": 3,
    "email": os.getenv('CONTACT_EMAIL', 'your-email@example.com'),
    "github_handle": "teterocynthia",
    "github_url": "https://github.com/teterocynthia",
    "linkedin_url": "",   # add your LinkedIn URL here
    "avatar_url": ""      # optional: absolute URL to a profile image
}

SKILLS = [
    "Python", "Flask", "HTML", "CSS", "JavaScript",
    "Tailwind CSS", "REST APIs", "Git", "SQL"
]

PROJECTS = [
    {
        "id": 1,
        "title": "E-Commerce Website",
        "description": "A full-stack e-commerce site with product browsing, cart, and Stripe payments. Focused on responsive UI and secure checkout flows.",
        "technologies": ["Python", "Flask", "Tailwind", "Stripe"],
        "image": "/static/images/project1.jpg",
        "github_url": "https://github.com/teterocynthia/project1",
        "live_url": "https://project1.live"
    },
    {
        "id": 2,
        "title": "Task Management App",
        "description": "Collaborative task app with real-time updates and an approachable UI to keep teams organized.",
        "technologies": ["Python", "Django", "React", "WebSockets"],
        "image": "/static/images/project2.jpg",
        "github_url": "https://github.com/teterocynthia/project2",
        "live_url": "https://project2.live"
    }
]

@app.context_processor
def inject_globals():
    """Make profile, skills and current_year available in all templates."""
    return {
        "profile": PROFILE,
        "skills": SKILLS,
        "current_year": datetime.utcnow().year
    }

@app.route('/')
def home():
    return render_template('index.html', projects=PROJECTS[:2])

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic server-side validation
        if not all([name, email, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        # For now, just log and flash. You can wire up an email provider or SMTP later.
        print(f"Contact form submission: {name}, {email}, {message}")
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('home'))

    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not all([name, email, message]):
        return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

    try:
        print(f"API Contact: {name} - {email} - {message}")
        return jsonify({
            'status': 'success',
            'message': 'Thank you for your message! I will get back to you soon.'
        })
    except Exception:
        return jsonify({'status': 'error', 'message': 'Something went wrong'}), 500

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
