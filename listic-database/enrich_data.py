"""
Script d'enrichissement des données LISTIC.
Ajoute: directeurs de thèse, dates, statuts pour les doctorants,
membres par projet, et liens phd_students/projects pour les chercheurs.
Données collectées depuis les pages publiques LISTIC (scrapage manuel + automatique).
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PERSONS_DIR = os.path.join(BASE, "listic personnes")
PROJ_DIR = os.path.join(BASE, "listic_projet")

# ──────────────────────────────────────────────
# 1. DONNÉES D'ENRICHISSEMENT DOCTORANTS
# ──────────────────────────────────────────────
DOCTORANT_DATA = {
    "Sabrine BOUAZIZ": {
        "director": "David Amitrano",
        "director_affiliation": "IsTerre",
        "co_director": "Christophe Lin-Kwong-Chon",
        "co_director_affiliation": "LISTIC",
        "co_advisor": "Nicolas Méger",
        "co_advisor_affiliation": "LISTIC",
        "start_date": "2024-08-04",
        "doctoral_school": "SIE - Sciences Ingénierie Environnement",
        "status": "active",
        "funding": None,
    },
    "Karima BOUTALBI": {
        "director": "Kavé Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "David Télisson",
        "co_director_affiliation": "LISTIC",
        "start_date": "2022-06-01",
        "doctoral_school": "SIE - Sciences Ingénierie Environnement",
        "status": "active",
        "funding": None,
    },
    "Ranya El hadri": {
        "director": "Kavé Salamatian",
        "director_affiliation": "LISTIC",
        "co_directors": [
            {"name": "Julien Boissière", "affiliation": "LISTIC"},
            {"name": "Sorana Cimpan", "affiliation": "LISTIC"},
            {"name": "Luc Damas", "affiliation": "LISTIC"},
        ],
        "start_date": "2021-11-01",
        "doctoral_school": "SIE - Sciences Ingénierie Environnement",
        "status": "active",
        "funding": None,
    },
    "Fatema EL-HUSSEINI": {
        "director": "Flavien Vernier",
        "director_affiliation": "LISTIC",
        "co_director": "Hassan N. Noura",
        "co_director_affiliation": "Externe",
        "start_date": "2023-09-01",
        "doctoral_school": "SIE - Sciences Ingénierie Environnement",
        "status": "active",
        "funding": None,
    },
    "Romain FERRER": {
        "director": "Kavé Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Sorana Cimpan",
        "co_director_affiliation": "LISTIC",
        "start_date": "2024-03-01",
        "doctoral_school": "SIE - Sciences Ingénierie Environnement",
        "status": "active",
        "funding": "@aspire USMB",
    },
    "Paul MATHIEU": {
        "director": "Kavé Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Kevin Limonier",
        "co_director_affiliation": "GEODE",
        "start_date": "2023-11-01",
        "doctoral_school": "SIE - Sciences Ingénierie Environnement",
        "status": "active",
        "funding": None,
    },
}

# ──────────────────────────────────────────────
# 2. MEMBRES PAR PROJET (NOM projet → liste de chercheurs)
# ──────────────────────────────────────────────
PROJECT_MEMBERS = {
    # Internationaux
    "CIME":                   ["Frédéric Pourraz", "Didier Coquin", "Hervé Verjus"],
    "GLARISKALP":             ["Emmanuel Trouvé"],
    # Nationaux
    "C2R-IA":                 ["Emmanuel Trouvé", "Christophe Lin-Kwong-Chon", "Yajing Yan"],
    "AIACOPAHV":              ["Emmanuel Trouvé", "Flavien Vernier"],
    "REPED-SARIX":            ["Yajing Yan"],
    "RainbowFS":              ["Sébastien Monnet"],
    "MARGARITA":              ["Yajing Yan", "Guillaume Ginolhac", "Abdourrahmane Atto"],
    "PHOENIX":                ["Emmanuel Trouvé", "Flavien Vernier"],
    "ReVeRies":               ["Didier Coquin"],
    "VIP-Mont-Blanc":         ["Emmanuel Trouvé"],
    "EFIDIR":                 ["Emmanuel Trouvé", "Flavien Vernier", "Yajing Yan"],
    "REVES":                  ["Didier Coquin"],
    "FOSTER":                 ["Nicolas Méger"],
    # Regionaux
    "IATOAURA":               ["Alexandre Benoit", "Nicolas Méger"],
    # Incubation
    "DEDICATED":              ["Sébastien Monnet", "Flavien Vernier", "Ilham Alloui"],
    "AFREU":                  ["Sébastien Monnet", "Alexandre Benoit"],
}

# ──────────────────────────────────────────────
# 3. PHD STUDENTS ET PROJETS PAR CHERCHEUR
# ──────────────────────────────────────────────
RESEARCHER_DATA = {
    "Abdourrahmane ATTO": {
        "projects": ["MARGARITA", "PHOENIX"],
        "phd_students_current": [],
        "phd_students_past": [],
    },
    "Alexandre BENOIT": {
        "projects": ["IATOAURA", "AFREU"],
        "phd_students_current": [
            {"name": "François-Xavier Sikoumno", "start_year": 2024, "end_year": 2028,
             "subject": "Decentralised federated deep learning, anomaly detection, multitemporal time series"},
            {"name": "Lorenzo Lopez-Uroz", "start_year": 2022, "end_year": 2025,
             "subject": "Deep learning, model inversion, physics inspired models"},
            {"name": "Lynda Ferraguyg", "start_year": 2022, "end_year": 2025,
             "subject": "Federated learning, bias detection and mitigation"},
            {"name": "Michael Dell'Aiera", "start_year": 2021, "end_year": 2024,
             "subject": "Semi supervised Deep neural networks for gamma rays analysis"},
        ],
        "phd_students_past": [
            {"name": "Emna Amri", "start_year": 2018, "end_year": 2021},
            {"name": "Mickael Jacquemont", "start_year": 2017, "end_year": 2020},
            {"name": "Amina Ben Hamida", "start_year": 2015, "end_year": 2019},
            {"name": "Rizlène Raoui", "start_year": 2014, "end_year": 2019},
            {"name": "Nicolas Voiron", "start_year": 2013, "end_year": 2016},
            {"name": "Sabin Tiberius Strat", "start_year": 2010, "end_year": 2013},
        ],
    },
    "Christophe LIN KWONG CHON": {
        "projects": ["C2R-IA"],
        "phd_students_current": [
            {"name": "Sabrine Bouaziz", "start_year": 2024,
             "subject": "XAI (eXplainable AI) for rockfalls prevision"},
        ],
        "phd_students_past": [
            {"name": "Idriss Sinapan", "start_year": 2022, "end_year": 2024,
             "subject": "Optimisation de l'interface fluidique dans les systèmes de production d'hydrogène"},
        ],
    },
    "David TÉLISSON": {
        "projects": [],
        "phd_students_current": [
            {"name": "Raphaël Hatté", "start_year": 2025,
             "subject": "Combinaison LLM et GNN pour la fusion de représentations multimodales"},
            {"name": "Karima Boutalbi", "start_year": 2022, "end_year": 2025,
             "subject": "Clustering de tenseurs pour les données textuelles"},
        ],
        "phd_students_past": [],
    },
    "Didier COQUIN": {
        "projects": ["CIME", "ReVeRies", "REVES"],
        "phd_students_current": [],
        "phd_students_past": [
            {"name": "Fanny Pagnier", "start_year": 2019, "end_year": 2023},
            {"name": "Kévin Jacq", "start_year": 2016, "end_year": 2019},
            {"name": "Rihab Ben Ameur", "start_year": 2015, "end_year": 2018},
            {"name": "Thanh Long Nguyen", "start_year": 2014, "end_year": 2017},
            {"name": "Guillaume Cerutti", "start_year": 2010, "end_year": 2013},
        ],
    },
    "Emmanuel TROUVÉ": {
        "projects": ["C2R-IA", "AIACOPAHV", "PHOENIX", "VIP-Mont-Blanc", "EFIDIR", "GLARISKALP"],
        "phd_students_current": [
            {"name": "Emma Molière", "start_year": 2024,
             "subject": "Rock fall detection using GB-SAR time series"},
        ],
        "phd_students_past": [
            {"name": "Antoine Bralet", "start_year": 2021, "end_year": 2024},
            {"name": "Matthieu Gallet", "start_year": 2021, "end_year": 2024},
            {"name": "Suvrat Kaushik", "start_year": 2019, "end_year": 2023},
            {"name": "Laurane Charrier", "start_year": 2019, "end_year": 2022},
            {"name": "Guilhem Marsy", "start_year": 2017, "end_year": 2020},
            {"name": "Yajing Yan", "start_year": 2008, "end_year": 2011},
        ],
    },
    "Flavien VERNIER": {
        "projects": ["AIACOPAHV", "PHOENIX", "EFIDIR"],
        "phd_students_current": [
            {"name": "Fatema El-Husseini", "start_year": 2023,
             "subject": "Solutions ML efficaces et robustes pour l'industrie 4.0"},
        ],
        "phd_students_past": [],
    },
    "Frédéric POURRAZ": {
        "projects": ["CIME"],
        "phd_students_current": [],
        "phd_students_past": [
            {"name": "Fanny Pagnier", "start_year": 2019, "end_year": 2023,
             "subject": "Méthodes d'aide à la décision en terrain avalancheux"},
        ],
    },
    "Julien BOISSIÈRE": {
        "projects": [],
        "phd_students_current": [
            {"name": "Ranya El Hadri", "start_year": 2021,
             "subject": "Méthodologie pour la reconstitution des ontologies de compétences"},
        ],
        "phd_students_past": [
            {"name": "Maxime Ogier", "end_year": 2013},
            {"name": "Jihène Tounsi", "end_year": None},
        ],
    },
    "Kavé SALAMATIAN": {
        "projects": [],
        "phd_students_current": [
            {"name": "Karima Boutalbi", "start_year": 2022,
             "subject": "Clustering hiérarchique de tenseurs sur les données textuelles"},
            {"name": "Ranya El Hadri", "start_year": 2021,
             "subject": "Méthodologie pour la reconstitution des ontologies de compétences"},
            {"name": "Romain Ferrer", "start_year": 2024,
             "subject": "Construction de parcours d'apprentissage flexibles"},
            {"name": "Paul Mathieu", "start_year": 2023,
             "subject": "Cartographie des Appropriations Territoriales par l'Investigation Numérique Augmentée"},
        ],
        "phd_students_past": [],
    },
    "Nicolas MEGER": {
        "projects": ["FOSTER", "IATOAURA"],
        "phd_students_current": [],
        "phd_students_past": [],
    },
    "Sébastien MONNET": {
        "projects": ["RainbowFS", "DEDICATED", "AFREU"],
        "phd_students_current": [
            {"name": "Andrew Mary Huet De Baroche",
             "subject": "Vers une IA résiliente et soutenable"},
            {"name": "Sylvain Lejamble",
             "subject": "Knowledge representation for Wise Objects"},
            {"name": "Asma Dhaouadi",
             "subject": "Large-scale data warehousing"},
        ],
        "phd_students_past": [
            {"name": "Abdelhafid Dahhani"},
            {"name": "Etienne Mauffret"},
            {"name": "Damien Carver"},
        ],
    },
    "Sorana CIMPAN": {
        "projects": [],
        "phd_students_current": [
            {"name": "Ranya El Hadri", "start_year": 2021,
             "subject": "Méthodologie pour la reconstitution des ontologies de compétences"},
            {"name": "Francesco Floris", "start_year": 2022,
             "subject": "Digital learning solutions and personalized learning paths"},
            {"name": "Romain Ferrer", "start_year": 2024,
             "subject": "Construction de parcours d'apprentissage flexibles"},
        ],
        "phd_students_past": [
            {"name": "Fabien Leymonerie", "start_year": 2001, "end_year": 2004},
            {"name": "Olivier Ratcliffe", "start_year": 2001, "end_year": 2004},
            {"name": "Jérôme Revillard", "start_year": 2002, "end_year": 2005},
            {"name": "Azadeh Razavizadeh", "start_year": 2006, "end_year": 2010},
        ],
    },
    "Stéphane PERRIN": {
        "projects": [],
        "phd_students_current": [],
        "phd_students_past": [
            {"name": "Blandine Pichon", "end_year": 2024,
             "subject": "Modélisation du processus d'établissement d'un profil sensoriel"},
            {"name": "Farah Abdel Khalek", "end_year": 2024,
             "subject": "Habitat connecté pour l'aide au maintien à domicile"},
            {"name": "Cédric Deffo Sikounmo", "end_year": 2019,
             "subject": "Reconnaissance de situation par objet sensibles"},
        ],
    },
    "Yajing YAN": {
        "projects": ["REPED-SARIX", "MARGARITA", "EFIDIR"],
        "phd_students_current": [
            {"name": "Théo Delfolie", "start_year": 2025,
             "subject": "Pronostic de salissures des modules PV"},
            {"name": "Grégoire Vest", "start_year": 2025,
             "subject": "Neural networks-based volcanic model inversion with SAR"},
            {"name": "Matthieu Verlynde", "start_year": 2024,
             "subject": "Weakly supervised classification for remote sensing time series"},
            {"name": "Léa Zuccali", "start_year": 2022,
             "subject": "Geodetic data assimilation for natural hazard management"},
        ],
        "phd_students_past": [
            {"name": "Dana El Hajjar", "start_year": 2022, "end_year": 2025},
            {"name": "Lorenzo Lopez-Uroz", "start_year": 2022, "end_year": 2025},
            {"name": "Phan Viet-Hoa Vu", "start_year": 2020, "end_year": 2023},
            {"name": "Suvrat Kaushik", "start_year": 2019, "end_year": 2023},
            {"name": "Laurane Charrier", "start_year": 2019, "end_year": 2022},
        ],
    },
    "Guillaume GINOLHAC": {
        "projects": ["MARGARITA"],
        "phd_students_current": [],
        "phd_students_past": [],
    },
}

# ──────────────────────────────────────────────
# ENRICHISSEMENT 1 : DOCTORANTS
# ──────────────────────────────────────────────
print("Chargement doctorants...")
doc_path = os.path.join(PERSONS_DIR, "listic_personnes.doctorants.json")
with open(doc_path, "r", encoding="utf-8") as f:
    doctorants = json.load(f)

updated_docs = 0
for doc in doctorants:
    name = doc.get("name", "")
    if name in DOCTORANT_DATA:
        for key, value in DOCTORANT_DATA[name].items():
            if value is not None:
                doc[key] = value
        updated_docs += 1

with open(doc_path, "w", encoding="utf-8") as f:
    json.dump(doctorants, f, ensure_ascii=False, indent=2)
print(f"  OK {updated_docs} doctorants enrichis ({len(doctorants)} total)")

# ──────────────────────────────────────────────
# ENRICHISSEMENT 2 : PROJETS (ajout du champ members)
# ──────────────────────────────────────────────
print("Chargement projets...")
proj_path = os.path.join(PROJ_DIR, "listic_projets.complete_structure.json")
with open(proj_path, "r", encoding="utf-8") as f:
    projects_root = json.load(f)

updated_projs = 0
proj_data = projects_root[0]["data"]
for category, proj_list in proj_data.items():
    for proj in proj_list:
        nom = proj.get("NOM", "")
        if nom in PROJECT_MEMBERS:
            proj["members"] = PROJECT_MEMBERS[nom]
            updated_projs += 1
        else:
            if "members" not in proj:
                proj["members"] = []

with open(proj_path, "w", encoding="utf-8") as f:
    json.dump(projects_root, f, ensure_ascii=False, indent=2)

# Mettre à jour aussi les fichiers par catégorie
for category in ["Internationaux", "Nationaux", "Regionaux", "Incubation"]:
    cat_path = os.path.join(PROJ_DIR, f"listic_projets.{category}.json")
    if os.path.exists(cat_path):
        with open(cat_path, "r", encoding="utf-8") as f:
            cat_projs = json.load(f)
        for proj in cat_projs:
            nom = proj.get("NOM", "")
            if nom in PROJECT_MEMBERS:
                proj["members"] = PROJECT_MEMBERS[nom]
            elif "members" not in proj:
                proj["members"] = []
        with open(cat_path, "w", encoding="utf-8") as f:
            json.dump(cat_projs, f, ensure_ascii=False, indent=2)

print(f"  OK {updated_projs} projets enrichis avec membres")

# ──────────────────────────────────────────────
# ENRICHISSEMENT 3 : ENSEIGNANTS-CHERCHEURS
# ──────────────────────────────────────────────
print("Chargement enseignants-chercheurs (fichier volumineux)...")
ec_path = os.path.join(PERSONS_DIR, "listic_personnes.enseignants_chercheurs.json")
with open(ec_path, "r", encoding="utf-8") as f:
    chercheurs = json.load(f)

# Construire un index nom → chercheur pour recherche rapide
# Les noms dans le JSON ont des formats variables (accents, casse)
# On fait une correspondance tolérante (majuscule nom de famille)
def normalize_name(name):
    """Retourne 'PRÉNOM NOM' normalisé pour matching."""
    return " ".join(name.strip().split()).upper()

chercheur_index = {}
for c in chercheurs:
    raw = c.get("name", "")
    chercheur_index[normalize_name(raw)] = c

updated_ec = 0
for researcher_name, data in RESEARCHER_DATA.items():
    # Essayer correspondance exacte d'abord
    norm = normalize_name(researcher_name)
    chercheur = chercheur_index.get(norm)

    # Si pas trouvé, chercher par mots-clés (nom de famille)
    if not chercheur:
        parts = researcher_name.upper().split()
        for key, c in chercheur_index.items():
            if all(p in key for p in parts):
                chercheur = c
                break

    if chercheur:
        if data.get("projects"):
            chercheur["projects"] = data["projects"]
        if data.get("phd_students_current"):
            chercheur["phd_students_current"] = data["phd_students_current"]
        if data.get("phd_students_past"):
            chercheur["phd_students_past"] = data["phd_students_past"]
        updated_ec += 1
    else:
        print(f"  ⚠ Chercheur non trouvé: {researcher_name}")

with open(ec_path, "w", encoding="utf-8") as f:
    json.dump(chercheurs, f, ensure_ascii=False, indent=2)
print(f"  OK {updated_ec} chercheurs enrichis ({len(chercheurs)} total)")

# ──────────────────────────────────────────────
# ENRICHISSEMENT 4 : COMPLETE_STRUCTURE PERSONNES
# ──────────────────────────────────────────────
print("Mise à jour complete_structure personnes...")
complete_path = os.path.join(PERSONS_DIR, "listic_personnes.complete_structure.json")
with open(complete_path, "r", encoding="utf-8") as f:
    complete = json.load(f)

# Propager les enrichissements dans complete_structure
data_section = complete[0].get("data", {})
if "enseignants_chercheurs" in data_section:
    for ec in data_section["enseignants_chercheurs"]:
        name = ec.get("name", "")
        for researcher_name, rdata in RESEARCHER_DATA.items():
            parts = researcher_name.upper().split()
            if all(p in name.upper() for p in parts):
                if rdata.get("projects"):
                    ec["projects"] = rdata["projects"]
                if rdata.get("phd_students_current"):
                    ec["phd_students_current"] = rdata["phd_students_current"]
                break

with open(complete_path, "w", encoding="utf-8") as f:
    json.dump(complete, f, ensure_ascii=False, indent=2)
print("  OK complete_structure personnes mis a jour")

print("\nEnrichissement termine avec succes!")
print("\nRésumé des données ajoutées:")
print(f"  - {updated_docs} doctorants: directeur, co-directeur, date début, école doctorale, statut, financement")
print(f"  - {updated_projs} projets: liste des membres (chercheurs)")
print(f"  - {updated_ec} chercheurs: phd_students_current, phd_students_past, projects")
