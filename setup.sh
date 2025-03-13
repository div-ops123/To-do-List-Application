#!/bin/bash

# Create project directories
mkdir -p templates static instance

# Create required files
touch app.py requirements.txt templates/index.html static/styles.css Dockerfile .gitignore

# Add common Python ignores to .gitignore
echo -e "__pycache__/\n*.pyc\ninstance/" > .gitignore

# Add initial README content
echo -e "# Flask To-Do List App.\n\nA simple Flask web application for managing a to-do list." > README.md

echo "Project structure created successfully!"
