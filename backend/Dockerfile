# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd

# Copy all files (including start.sh, app/, etc.)
COPY . .

# Give execution permission to the script
RUN chmod +x start.sh
RUN chmod +x wait-for-it.sh

# Expose port 8000
EXPOSE 8000

# Run the script instead of direct command
CMD ["./start.sh"]
