FROM python:3.9-slim

EXPOSE 30000-30009:30000-30009 21 80

# Create and set the working directory
WORKDIR /app

# Copy the Python server script
COPY web_server.py /app/web_server.py
COPY ftp_server.py /app/ftp_server.py
COPY requirements.txt /app/requirements.txt
COPY website /app/website

#COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


CMD ["sh", "-c", "python web_server.py & python ftp_server.py"]
