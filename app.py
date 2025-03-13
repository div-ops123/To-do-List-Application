import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application with instance_relative_config=True
app = Flask(__name__, instance_relative_config=True)

# Ensure the instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# Configure the SQLite database to point to the instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

# Create the database tables within the application context
with app.app_context():
    db.create_all()

# Route for the homepage to view and add tasks
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the task title from the form
        title = request.form['title']
        if title:  # Ensure the title is not empty
            # Create a new task and add it to the database
            new_task = Task(title=title)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))
    
    # Fetch all tasks for display
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# Route to delete a task
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    # Fetch the task or return 404 if not found
    task = Task.query.get_or_404(task_id)
    # Delete the task from the database
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# Run the application on port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
