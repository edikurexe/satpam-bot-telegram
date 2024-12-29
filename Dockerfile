# Gunakan Python sebagai base image
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Instal semua dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin file script bot
COPY bot.py .

# Salin file environment token.env
COPY token.env .

# Jalankan bot
CMD ["sh", "-c", "TOKEN=$(grep TOKEN token.env | cut -d '=' -f 2) python3 bot.py"]
