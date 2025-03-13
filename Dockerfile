# Start with a base image (Step 1)
FROM ubuntu:20.04

# Install Python and pip (Step 2)
RUN apt-get update && apt-get install -y python3 python3-pip sqlite3

# Set the author (optional)
LABEL author="div-ops123"

# Set environment variables (Step 3)
ENV FLASK_APP=app.py \
    FLASK_ENV=development
# No need for tasks.db-specific vars since Flask-SQLAlchemy uses SQLALCHEMY_DATABASE_URI from app.py.

# Set the container working directory (Step 3)
WORKDIR /to-do-app

# Copy the application files into the container's /to-do-app directory (Step 4)
COPY . /to-do-app

# Install dependencies (Step 5)
RUN pip3 install -r requirements.txt

# Expose the application port (Step 6)
EXPOSE 5000

# Create a mount point for persistent data even when container stops (Step 7)
VOLUME "/to-do-app/instance"
# This ensures tasks.db persists in a volume, but you must map it when running.
# Use "/to-do-app/instance" since tasks.db is in the instance folder and /to-do-app is our working directory.

# Set the default command (Step 8)
CMD [ "python3", "app.py" ]