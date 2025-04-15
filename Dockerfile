# Utiliser une image officielle Python
FROM python:3.9-slim

# Installer les dépendances
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier tous les fichiers du projet
COPY . .

# Créer la base de données
RUN python -c "import sqlite3; conn = sqlite3.connect('predictions.db'); conn.close()"

# Exposer le port Flask
EXPOSE 5000

# Lancer l'API Flask
CMD ["python", "app.py"]
