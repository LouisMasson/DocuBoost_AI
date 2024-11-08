# Étape 1 : Utiliser une image de base légère avec Python installé
FROM python:3.9-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier les fichiers locaux dans le répertoire de travail du conteneur
COPY . /app

# Étape 4 : Installer les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port sur lequel Streamlit va tourner
EXPOSE 8501

# Étape 6 : Lancer l'application Streamlit
CMD ["streamlit", "run", "app_stream.py", "--server.port=8501", "--server.address=0.0.0.0"]
