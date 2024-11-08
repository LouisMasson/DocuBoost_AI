# Étape 1 : Utiliser une image de base légère avec Python
FROM python:3.9-slim as base

# Définir des variables d'environnement si nécessaire
ENV DATABASE_URL=$DATABASE_URL

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier les fichiers locaux dans le répertoire de travail du conteneur
COPY . /app

# Étape 4 : Installer les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port que Streamlit utilisera
EXPOSE 8501

# Étape 6 : Lancer l'application Streamlit
CMD ["streamlit", "run", "app_stream.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Optionnel : Pour inclure une vérification de l'état de santé de l'application
# HEALTHCHECK --interval=5s --timeout=3s --start-period=30s --retries=3 CMD wget -qO- http://localhost:8501 || exit 1

