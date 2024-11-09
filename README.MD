![DocuBoost AI](github%20banner.png)


# DocuBoost AI

# Application de Scraping de Documentation Technique

Cette application Streamlit permet de scraper des sites web de documentation technique et de télécharger le contenu au format Markdown. L'objectif est de fournir du contexte aux outils d'IA de codage comme Cursor AI ou Bolt.new.

## Fonctionnalités

- Scraping de contenu web en utilisant `AsyncWebCrawler`.
- Conversion du contenu scrappé en Markdown.
- Téléchargement du contenu scrappé au format Markdown.
- Gestion des erreurs pour les URL invalides et les problèmes de connexion.

## Prérequis

- Python 3.7 ou supérieur
- `streamlit`
- `crawl4ai`
- `playwright`
- `nest_asyncio`

## Installation

1. Clonez ce dépôt :
    ```bash
    git clone https://github.com/LouisMasson/DocuBoost_AI
    cd votre-repo
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Installez les dépendances système nécessaires pour Playwright :
    ```bash
    sudo apt-get install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2 libpango-1.0-0 libcairo2 libatspi2.0-0 libgtk-3-0 libgdk-pixbuf2.0-0 libxcursor1 libxext6 libpangocairo-1.0-0 libwayland-client0
    ```

## Utilisation

1. Lancez l'application Streamlit :
    ```bash
    streamlit run app_stream.py
    ```

2. Ouvrez votre navigateur web et accédez à l'URL indiquée par Streamlit (par défaut `http://localhost:8501`).

3. Entrez l'URL du site web de documentation technique que vous souhaitez scraper et le nom du fichier Markdown (sans extension).

4. Cliquez sur le bouton "Scraper et Enregistrer".

5. Une fois le scraping terminé, vous pouvez prévisualiser le contenu scrappé et le télécharger en cliquant sur le bouton "Télécharger le fichier Markdown".

## Fonctionnement de l'application

L'application utilise `AsyncWebCrawler` pour scraper le contenu des sites web. Voici un aperçu des principales fonctions :

- `is_valid_url(url: str) -> bool`: Vérifie si une URL est valide.
- `async def scrape_to_markdown(url)`: Scrape le contenu d'une URL et le convertit en Markdown.
- `def run_async(coroutine)`: Exécute une coroutine asynchrone dans une boucle d'événements.

L'interface utilisateur est construite avec Streamlit, permettant aux utilisateurs d'entrer une URL et de télécharger le contenu scrappé en Markdown.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
