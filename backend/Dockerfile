FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    golang-go \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

RUN cp /root/go/bin/subfinder /usr/local/bin/subfinder

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]