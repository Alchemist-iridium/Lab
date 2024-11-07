# File: apod_model.py (Model)
import requests

def get_apod(api_key, date=None):
    base_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key}
    if date:
        params['date'] = date
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# File: app.py (Controller)
from flask import Flask, render_template, request, redirect, url_for, flash
from apod_model import get_apod
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key
API_KEY = 'DEMO_KEY'  # Replace with your actual API key

@app.route('/')
def index():
    apod_data = get_apod(API_KEY)
    if not apod_data:
        flash('Unable to fetch the Astronomy Picture of the Day. Please try again later.')
    return render_template('index.html', apod=apod_data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'POST':
        date = request.form['date']
        if validate_date(date):
            apod_data = get_apod(API_KEY, date)
            if apod_data:
                return render_template('history.html', apod=apod_data, current_date=datetime.now().strftime('%Y-%m-%d'))
            else:
                flash('Could not retrieve data for the selected date.')
                return redirect(url_for('history'))
        else:
            flash('Invalid date. Please select a date between June 16, 1995, and today.')
            return redirect(url_for('history'))
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('history.html', current_date=current_date)

def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        start_date = datetime(1995, 6, 16)
        today = datetime.now()
        return start_date <= date <= today
    except ValueError:
        return False

if __name__ == '__main__':
    app.run(debug=True)

# File: templates/index.html (Landing Page)
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Astronomy Picture of the Day</title>
</head>
<body>
    <h1>Astronomy Picture of the Day - {{ apod['date'] if apod else 'Unknown' }}</h1>
    {% if apod %}
        <img src="{{ apod['url'] }}" alt="APOD">
        <p>{{ apod['explanation'] }}</p>
        {% if apod['copyright'] %}
            <p>© {{ apod['copyright'] }}</p>
        {% endif %}
    {% else %}
        <p>Could not load the Astronomy Picture of the Day.</p>
    {% endif %}
    <a href="{{ url_for('history') }}">History Page</a>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>

# File: templates/history.html (History Page)
<!DOCTYPE html>
<html lang="en">
<head>
    <title>APOD History</title>
</head>
<body>
    <h1>Search APOD by Date</h1>
    <form method="post">
        <label for="date">Select Date:</label>
        <input type="date" id="date" name="date" required min="1995-06-16" max="{{ current_date }}">
        <button type="submit">Get Picture</button>
    </form>
    {% if apod %}
        <h2>{{ apod['title'] }} - {{ apod['date'] }}</h2>
        <img src="{{ apod['url'] }}" alt="APOD">
        <p>{{ apod['explanation'] }}</p>
        {% if apod['copyright'] %}
            <p>© {{ apod['copyright'] }}</p>
        {% endif %}
    {% endif %}
    <a href="{{ url_for('index') }}">Home Page</a>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
