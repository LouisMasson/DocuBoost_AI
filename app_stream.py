import os
import asyncio
import streamlit as st
from crawl4ai import AsyncWebCrawler
from urllib.parse import urlparse
import nest_asyncio
import threading

# Affiche le logo en haut de l'application
st.image("Docuboost AI.png", use_column_width=True)

# Configuration initiale de Playwright
def setup_playwright():
    try:
        os.system("playwright install")
        os.system("playwright install-deps")
        return True
    except Exception as e:
        st.error(f"Erreur lors de l'installation de Playwright: {e}")
        return False

# Configuration initiale
if not os.path.exists("/home/adminuser/.cache/ms-playwright"):
    setup_playwright()

# Applique nest_asyncio pour permettre l'imbrication des boucles événementielles
nest_asyncio.apply()

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Fonction asynchrone de scraping avec gestion des erreurs
async def scrape_to_markdown(url):
    try:
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url=url)
            return result.markdown
    except ValueError:
        st.error("URL invalide. Veuillez entrer une URL correcte.")
        return None
    except ConnectionError:
        st.error("Erreur de connexion. Vérifiez votre connexion Internet et réessayez.")
        return None
    except Exception as e:
        st.error(f"Une erreur est survenue : {str(e)}")
        if "missing dependencies" in str(e).lower():
            st.error("Erreur de dépendances Playwright. Veuillez contacter l'administrateur.")
        return None

def run_async(coroutine):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coroutine)
    finally:
        loop.close()

# Interface Streamlit
def main():
    st.title("DocuBoost AI")
    st.write("Entrez une URL pour scraper le contenu du site et le télécharger au format Markdown.")

    # Champs de saisie pour l'URL et le nom du fichier
    url = st.text_input("Entrez l'URL à scraper")
    filename_input = st.text_input("Entrez le nom du fichier Markdown (sans extension)")

    # Initialise une variable pour stocker le contenu scrappé
    markdown_content = None

    if st.button("Scraper et Enregistrer"):
        if url and filename_input:
            filename = filename_input + ".md"
            st.write("Scraping en cours...")

            # Exécute le scraping dans un nouveau thread avec sa propre boucle d'événements
            markdown_content = run_async(scrape_to_markdown(url))

            # Vérifie si le scraping a réussi
            if markdown_content:
                st.success(f"Le contenu scrappé est prêt à être téléchargé sous le nom : {filename}")

                # Prévisualisation du contenu Markdown
                preview_length = 2000
                st.subheader("Aperçu du contenu scrappé :")
                st.code(markdown_content[:preview_length] + ("..." if len(markdown_content) > preview_length else ""), language="markdown")
        else:
            st.warning("Veuillez entrer une URL et un nom de fichier.")

    # Affiche le bouton de téléchargement si du contenu a été scrappé
    if markdown_content:
        st.download_button(
            label="Télécharger le fichier Markdown",
            data=markdown_content,
            file_name=filename,
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()
