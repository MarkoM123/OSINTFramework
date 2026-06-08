FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    unzip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN wget https://github.com/projectdiscovery/subfinder/releases/latest/download/subfinder_linux_amd64.zip \
 && unzip subfinder_linux_amd64.zip \
 && mv subfinder /usr/local/bin/subfinder \
 && chmod +x /usr/local/bin/subfinder \
 && rm -f subfinder_linux_amd64.zip

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]