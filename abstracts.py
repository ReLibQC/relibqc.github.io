import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os

def slugify(text):
    """
    Nettoie et formate le nom de l'orateur pour créer un nom de fichier propre.
    Exemple: "Paul W. Ayers" -> "paul-w-ayers"
    """
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text

def fetch_speaker_types_from_web():
    """
    Scrape le site relibqc.github.io pour récupérer les types de présentation (Keynote, Contributed, etc.)
    et les associer au nom de chaque orateur.
    """
    url = "https://relibqc.github.io/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    speaker_types = {}

    # Types de présentations
    prefix_map = {
        '(K)': 'Keynote talk',
        '(C)': 'Contributed talk',
        '(S)': 'Short talk',
        '(F)': 'Flash talk'
    }

    # Parcours des éléments de tableau de l'emploi du temps
    cells = soup.find_all(['td', 'li'])
    for cell in cells:
        text = cell.get_text().strip()
        for prefix, talk_type in prefix_map.items():
            if prefix in text:
                # Extraire le nom de l'orateur situé après le préfixe
                raw_name = text.split(prefix)[-1].strip()

                # Cas spécial si deux orateurs partagent une keynote (ex: "Paul Ayers & Farnaz Heidar-Zadeh")
                if '&' in raw_name:
                    names = [n.strip() for n in raw_name.split('&')]
                    for n in names:
                        speaker_types[n.lower()] = talk_type
                else:
                    speaker_types[raw_name.lower()] = talk_type

    # On ajoute Mario Wolter manuellement s'il est listé comme atelier
    speaker_types['mario wolter'] = 'Workshop / Discussion'

    return speaker_types

def generate_jekyll_talks(csv_filepath, output_dir="2026"):
    os.makedirs(output_dir, exist_ok=True)

    # 1. Récupération des types de présentation depuis le site web
    print("Récupération du programme sur https://relibqc.github.io/...")
    web_speaker_types = fetch_speaker_types_from_web()

    # 2. Lecture du CSV
    df = pd.read_csv(
    csv_filepath,
    engine='python',
    quotechar='"',
    on_bad_lines='skip'  # au cas où une ligne est irrécupérable
)
    df_speakers = df[df['Contribution title'].notna() & df['Full name'].notna()].copy()

    generated_count = 0

    for idx, row in df_speakers.iterrows():
        name = str(row['Full name']).strip()
        name_lower = name.lower()

        # Vérifier si l'orateur est dans le programme du site web
        # Recherche par correspondance exacte ou sous-chaîne (pour gérer les initiales/variations)
        talk_type = None
        for web_name, t_type in web_speaker_types.items():
            if web_name in name_lower or name_lower in web_name:
                talk_type = t_type
                break

        # Ignorer si l'orateur n'est pas dans le programme officiel du site
        if not talk_type:
            print(f"Skipped (not on website schedule): {name}")
            continue

        affiliation = str(row['Institution/affiliation']).strip() if pd.notna(row['Institution/affiliation']) else ""
        title = str(row['Contribution title']).strip()
        abstract = str(row['Contribution abstract']).strip() if pd.notna(row['Contribution abstract']) else "No abstract provided."

        # Échappement des guillemets pour le Front Matter YAML
        clean_title = title.replace('"', '\\"')
        clean_name = name.replace('"', '\\"')
        clean_affiliation = affiliation.replace('"', '\\"')
        clean_type = talk_type.replace('"', '\\"')

        slug = slugify(name)
        filename = f"{slug}.md"
        filepath = os.path.join(output_dir, filename)

        # Contenu du fichier Markdown pour Jekyll
        md_content = f"""---
layout: default
title: "{clean_title}"
speaker: "{clean_name}"
affiliation: "{clean_affiliation}"
type: "{clean_type}"
---

# {title}

**Speaker:** {name}
**Affiliation:** {affiliation}
**Type:** {talk_type}

---

### Abstract

{abstract}

---

[← Return to main schedule]({{{{ site.baseurl }}}}/)
"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)

        print(f"Generated ({talk_type}): {filepath}")
        generated_count += 1

    print(f"\nTerminé ! {generated_count} fichiers générés dans ./{output_dir}/")

if __name__ == "__main__":
    csv_filename = "ReLibQC.csv"
    generate_jekyll_talks(csv_filename, output_dir="2026")

