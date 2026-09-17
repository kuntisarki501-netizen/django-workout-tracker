
# Django Workout Tracker
 
A simple Django web app that displays a weekly workout schedule. Each day shows the muscle group being trained, a list of exercises, and a linked YouTube video to follow along with.
 
## Features
 
- Weekly workout plan displayed as a grid of cards (Monday–Sunday)
- Each day links to a detail page with exercises and a workout video
- Rest days are clearly marked
- A separate Diet page with a sample daily meal plan
- Dark, mobile-friendly UI built with plain CSS
- Built using Django's template inheritance, static files, and dynamic URL routing
## Tech Stack
 
- Python
- Django
- HTML / CSS
## Project Structure
 
```
Workout/
    fitnesssite/        # Django project settings
    workouts/            # Main app
        views.py         # Workout & diet data + view logic
        urls.py           # App routes
        templates/workouts/
            base.html
            navbar.html
            home.html
            day_detail.html
            diet.html
        static/workouts/
            css/style.css
            images/
    manage.py
```
 
## How to Run Locally
 
1. Clone this repository
```bash
   git clone https://github.com/YOUR_USERNAME/django-workout-tracker.git
   cd django-workout-tracker
```
 
2. Create and activate a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
```
 
3. Install Django
```bash
   pip install django
```
 
4. Run the development server
```bash
   python manage.py runserver
```
 
5. Open your browser at:
```
   http://127.0.0.1:8000/
```
 
## What I Learned
 
This project was built while learning core Django concepts:
- Template inheritance (`{% extends %}`, `{% block %}`)
- Passing data from views to templates
- Static files (CSS, images) and the `DEBUG` setting
- Dynamic URLs with parameters
- Reusable template includes (navbar)

 
 

