from django.shortcuts import render

workout_plan = [
    {'day': 'Monday', 'focus': 'Chest', 'is_rest': False,
     'exercises': ['Bench Press - 4x10', 'Push Ups - 3x15', 'Chest Fly - 3x12'],
     'video_id': '4Y2ZdHCOXok'},

    {'day': 'Tuesday', 'focus': 'Back', 'is_rest': False,
     'exercises': ['Pull Ups - 4x8', 'Deadlift - 4x10', 'Rows - 3x12'],
     'video_id': 'JdjJC6eIk44'},

    {'day': 'Wednesday', 'focus': 'Abs', 'is_rest': False,
     'exercises': ['Crunches - 4x20', 'Plank - 3x1min', 'Leg Raises - 3x15'],
     'video_id': 'AY_kuI0U9ds'},

    {'day': 'Thursday', 'focus': 'Shoulders', 'is_rest': False,
     'exercises': ['Shoulder Press - 4x10', 'Lateral Raise - 3x12'],
     'video_id': 'zGZVv5zqCFE'},

    {'day': 'Friday', 'focus': 'Arms', 'is_rest': False,
     'exercises': ['Bicep Curl - 4x10', 'Tricep Dips - 3x12'],
     'video_id': 'WvlDMlMx1Ok'},

    {'day': 'Saturday', 'focus': 'Rest Day', 'is_rest': True,
     'exercises': [], 'video_id': '1cZbv9Eyd4c'},

    {'day': 'Sunday', 'focus': 'Leg Day', 'is_rest': False,
     'exercises': ['Squats - 4x10', 'Lunges - 3x12', 'Leg Press - 4x10'],
     'video_id': 'Xg9B6pqHUQE'},
]

diet_plan = [
    {'meal': 'Breakfast', 'items': ['Oats with banana', '2 boiled eggs', 'Green tea'], 'calories': 350},
    {'meal': 'Mid-Morning Snack', 'items': ['Handful of almonds', 'Apple'], 'calories': 150},
    {'meal': 'Lunch', 'items': ['Grilled chicken breast', 'Brown rice', 'Steamed vegetables'], 'calories': 550},
    {'meal': 'Evening Snack', 'items': ['Greek yogurt', 'Mixed berries'], 'calories': 200},
    {'meal': 'Dinner', 'items': ['Grilled fish', 'Sweet potato', 'Salad'], 'calories': 450},
]

def home(request):
    return render(request, 'workouts/home.html', {'workout_plan': workout_plan})

def day_detail(request, day_name):
    day = next((d for d in workout_plan if d['day'].lower() == day_name.lower()), None)
    return render(request, 'workouts/day_detail.html', {'day': day})

def diet(request):
    return render(request, 'workouts/diet.html', {'diet_plan': diet_plan})