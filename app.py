from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')

PROJECTS = [
    {
        "id": 1,
        "title": "E-Commerce Website",
        "description": "A full-stack e-commerce platform with payment integration",
        "technologies": ["Python", "Flask", "JavaScript", "Stripe API"],
        "image": "/static/images/project1.jpg",
        "github_url": "https://github.com/yourusername/project1",
        "live_url": "https://project1.live"
    },
    {
        "id": 2,
        "title": "Task Management App",
        "description": "A collaborative task management application with real-time updates",
        "technologies": ["Python", "Django", "React", "WebSockets"],
        "image": "/static/images/project2.jpg",
        "github_url": "https://github.com/yourusername/project2",
        "live_url": "https://project2.live"
    }
]

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
        
        print(f"Contact form submission: {name}, {email}, {message}")
        flash('Thank you for your message! I will get back to you soon.', 'success')
        return redirect(url_for('home'))
    
    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json()
    
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
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Something went wrong'}), 500

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
