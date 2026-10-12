"""
Script d'enrichissement complet des doctorants LISTIC.
Source: theses.fr API + pages LISTIC scrapées.
- Corrige les 11 entrées existantes (directeurs, dates, statuts)
- Ajoute ~19 doctorants manquants détectés via theses.fr
"""
import json
import hashlib
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
PERSONS_DIR = os.path.join(BASE, "listic personnes")
DOC_PATH = os.path.join(PERSONS_DIR, "listic_personnes.doctorants.json")
EC_PATH = os.path.join(PERSONS_DIR, "listic_personnes.enseignants_chercheurs.json")

NOW = datetime.now().isoformat()

def make_uid(name):
    return hashlib.md5(name.encode()).hexdigest()

# ──────────────────────────────────────────────
# CORRECTIONS DES 11 ENTREES EXISTANTES
# ──────────────────────────────────────────────
CORRECTIONS = {
    "Sabrine BOUAZIZ": {
        "director": "David Amitrano",
        "director_affiliation": "IsTerre",
        "co_director": "Christophe Lin-Kwong-Chon",
        "co_director_affiliation": "LISTIC",
        "co_advisor": "Nicolas Meger",
        "co_advisor_affiliation": "LISTIC",
        "start_date": "2024-08-04",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
    "Karima BOUTALBI": {
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "David Telisson",
        "co_director_affiliation": "LISTIC",
        "start_date": "2022-06-01",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
    "Pierre DARDOUILLET": {
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_directors": [
            {"name": "Herve Verjus", "affiliation": "LISTIC"},
            {"name": "Olivier Le Van", "affiliation": "Externe"},
        ],
        "start_date": "2022-04-01",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "Sujet": "Modelisation des connaissances d'une base de tickets d'un processus GRH",
        "funding": None,
    },
    "Ranya El hadri": {
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_directors": [
            {"name": "Julien Boissiere", "affiliation": "LISTIC"},
            {"name": "Sorana Cimpan", "affiliation": "LISTIC"},
            {"name": "Luc Damas", "affiliation": "LISTIC"},
        ],
        "start_date": "2021-11-01",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
    "Fatema EL-HUSSEINI": {
        "director": "Flavien Vernier",
        "director_affiliation": "LISTIC",
        "co_director": "Hassan N. Noura",
        "co_director_affiliation": "Externe",
        "start_date": "2023-09-01",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
    "Romain FERRER": {
        # Correction: theses.fr indique Vernier+Cimpan (pas Salamatian)
        "director": "Flavien Vernier",
        "director_affiliation": "LISTIC",
        "co_director": "Sorana Cimpan",
        "co_director_affiliation": "LISTIC",
        "start_date": "2024-03-01",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": "@aspire USMB",
    },
    "Douba JAFUNO": {
        # A SOUTENU le 04/11/2025
        "director": "Guillaume Ginolhac",
        "director_affiliation": "LISTIC",
        "co_directors": [
            {"name": "Ammar Mian", "affiliation": "LISTIC"},
            {"name": "Nickolas Stelzenmuller", "affiliation": "Externe"},
        ],
        "Sujet": "Interpretation automatique de donnees geophysiques par techniques d'apprentissage",
        "NNT": "2025CHAMA041",
        "status": "defended",
        "defense_date": "2025-11-04",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "funding": None,
    },
    "Utpal KANT": {
        "director": "Christophe Roche",
        "director_affiliation": "LISTIC",
        "co_director": "Maryam Darvish",
        "co_director_affiliation": "LISTIC",
        "start_date": "2019-12-18",
        "Sujet": "Neuro-Symbolic Artificial Intelligence applied to Container Shipping Supply Chain Transformation",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
    "Paul MATHIEU": {
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Kevin Limonier",
        "co_director_affiliation": "GEODE",
        "start_date": "2023-11-01",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
    "Saloua NAAMA": {
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Francesco Bronzino",
        "co_director_affiliation": "Externe",
        "start_date": "2021-10-01",
        "Sujet": "Vers la geometrisation des grand graphes",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
        "funding": None,
    },
}

# ──────────────────────────────────────────────
# NOUVEAUX DOCTORANTS A AJOUTER
# Tous confirmes via theses.fr API
# ──────────────────────────────────────────────
NEW_DOCTORANTS = [
    {
        "name": "Emma MOLIERE",
        "director": "Emmanuel Trouve",
        "director_affiliation": "LISTIC",
        "co_director": "Argheesh Bhanot",
        "co_director_affiliation": "LISTIC",
        "start_date": "2024-10-01",
        "Sujet": "Detection et prediction de chutes de blocs a partir de series temporelles d'images GB-SAR",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Matthieu VERLYNDE",
        "director": "Ammar Mian",
        "director_affiliation": "LISTIC",
        "co_director": "Yajing Yan",
        "co_director_affiliation": "LISTIC",
        "start_date": "2024-10-01",
        "Sujet": "Classification faiblement supervisee et frugale pour les series temporelles d'images en teledetection",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Lea ZUCCALI",
        "director": "Yajing Yan",
        "director_affiliation": "LISTIC",
        "co_director": "Virginie Pinel",
        "co_director_affiliation": "ISTerre",
        "start_date": "2022-10-01",
        "Sujet": "Assimilation de donnees geodesiques pour une gestion en temps reel des risques naturels",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Theo DELFOLIE",
        "director": "Yajing Yan",
        "director_affiliation": "LISTIC",
        "start_date": "2025-12-08",
        "Sujet": "Pronostic de salissures des modules PV via la modelisation de l'environnement reel et la fusion de donnees",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Gregoire VEST",
        "director": "Yajing Yan",
        "director_affiliation": "LISTIC",
        "co_director": "Fabien Albino",
        "co_director_affiliation": "ISTerre",
        "start_date": "2025-10-01",
        "Sujet": "Inversion de modele volcanique par reseau de neurone avec mesures de deplacement SAR",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Jacques CHARROY",
        "director": "Jean-Luc Got",
        "director_affiliation": "ISTerre",
        "co_directors": [
            {"name": "Svetlana Byrdina", "affiliation": "ISTerre"},
            {"name": "Yajing Yan", "affiliation": "LISTIC"},
        ],
        "start_date": "2022-10-01",
        "Sujet": "Evaluation des ressources et risques lies a la geothermie de moyenne enthalpie par des methodes geophysiques passives",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "David ESALE YOKA",
        "director": "Flavien Vernier",
        "director_affiliation": "LISTIC",
        "co_director": "Ilham Alloui",
        "co_director_affiliation": "LISTIC",
        "start_date": "2024-09-02",
        "Sujet": "Optimisation des architectures de microservices pour le traitement Big Data par des techniques d'Intelligence Artificielle",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Youssouph FAYE",
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Francesco Bronzino",
        "co_director_affiliation": "Externe",
        "start_date": "2022-09-05",
        "Sujet": "Architecture Edge Cloud distribuee pour l'execution d'applications basees sur l'intelligence artificielle",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Gausse Mael DONGMO KENFACK",
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Frederick Douzet",
        "co_director_affiliation": "Externe",
        "start_date": "2026-02-01",
        "Sujet": "Contribution a l'analyse de grands graphes et application a la geopolitique du cyberespace",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Sara PELINKU",
        "director": "Kave Salamatian",
        "director_affiliation": "LISTIC",
        "co_director": "Olaf Maennel",
        "co_director_affiliation": "Externe",
        "start_date": "2025-01-21",
        "Sujet": "Vers la fusion d'informations heterogenes au sein des centres d'operations de securite",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Raphael HATTE",
        "director": "Jean-Yves Ramel",
        "director_affiliation": "LISTIC",
        "co_director": "David Telisson",
        "co_director_affiliation": "LISTIC",
        "start_date": "2025-12-01",
        "Sujet": "Combinaison LLM et GNN pour la fusion de representations multimodales : Application a l'extraction d'information dans les donnees semi-structures",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Francois-Xavier SIKOUMNO",
        "director": "Alexandre Benoit",
        "director_affiliation": "LISTIC",
        "start_date": "2024-01-01",
        "Sujet": "Decentralised federated deep learning, anomaly detection, multitemporal time series",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Lorenzo LOPEZ-UROZ",
        "director": "Alexandre Benoit",
        "director_affiliation": "LISTIC",
        "co_director": "Yajing Yan",
        "co_director_affiliation": "LISTIC",
        "start_date": "2022-01-01",
        "Sujet": "Deep learning, model inversion, physics inspired models",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Lynda FERRAGUYG",
        "director": "Alexandre Benoit",
        "director_affiliation": "LISTIC",
        "start_date": "2022-01-01",
        "Sujet": "Federated learning, bias detection and mitigation",
        "Theme": "AFuTe",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Francesco FLORIS",
        "director": "Sorana Cimpan",
        "director_affiliation": "LISTIC",
        "co_directors": [
            {"name": "Marina Marchisio", "affiliation": "Externe"},
            {"name": "Sergio Rabellino", "affiliation": "Externe"},
        ],
        "start_date": "2022-07-14",
        "Sujet": "Conception et developpement des solutions d'apprentissage en ligne basees sur les donnees educatives",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Andrew Mary HUET DE BAROCHE",
        "director": "Sebastien Monnet",
        "director_affiliation": "LISTIC",
        "co_director": "Stephan Plassart",
        "co_director_affiliation": "LISTIC",
        "Sujet": "Vers une IA resiliente et soutenable",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Sylvain LEJAMBLE",
        "director": "Sebastien Monnet",
        "director_affiliation": "LISTIC",
        "co_directors": [
            {"name": "Flavien Vernier", "affiliation": "LISTIC"},
            {"name": "Ilham Alloui", "affiliation": "LISTIC"},
        ],
        "Sujet": "Knowledge representation for Wise Objects",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
    {
        "name": "Asma DHAOUADI",
        "director": "Sebastien Monnet",
        "director_affiliation": "LISTIC",
        "co_director": "Khadija Bousselmi",
        "co_director_affiliation": "LISTIC",
        "Sujet": "Entreposage de donnees a grande echelle",
        "Theme": "ReGaRD",
        "doctoral_school": "SIE - Sciences Ingenerie Environnement",
        "status": "active",
    },
]

# ──────────────────────────────────────────────
# EXECUTION
# ──────────────────────────────────────────────
print("Chargement doctorants...")
with open(DOC_PATH, "r", encoding="utf-8") as f:
    doctorants = json.load(f)

existing_names = {d["name"].upper().strip() for d in doctorants}

# 1. Corrections des entrées existantes
corrected = 0
for doc in doctorants:
    name = doc["name"]
    if name in CORRECTIONS:
        for key, val in CORRECTIONS[name].items():
            if val is not None:
                doc[key] = val
        corrected += 1

print(f"  {corrected} entrees existantes corrigees")

# 2. Ajout des nouveaux doctorants
added = 0
for new_doc in NEW_DOCTORANTS:
    name_upper = new_doc["name"].upper().strip()
    if name_upper in existing_names:
        print(f"  SKIP (existe deja): {new_doc['name']}")
        continue

    entry = {
        "name": new_doc["name"],
        "url_listic": "Non trouve",
        "email": "Non trouve",
        "email perso": "Non trouve",
        "LinkedIn": "Non trouve",
        "phone": "Non trouve",
        "WhatsApp": "Non trouve",
        "office": "Non trouve",
        "address": "Non trouvee",
        "Theme": new_doc.get("Theme", "Non trouve"),
        "Sujet": new_doc.get("Sujet", "Non trouve"),
        "_unique_id": make_uid(new_doc["name"]),
        "category": "doctorants",
        "last_updated": NOW,
        "status": new_doc.get("status", "active"),
        "doctoral_school": new_doc.get("doctoral_school", "SIE"),
    }

    # Ajouter tous les champs fournis sauf name/Theme/Sujet/status/doctoral_school (deja traites)
    skip = {"name", "Theme", "Sujet", "status", "doctoral_school"}
    for key, val in new_doc.items():
        if key not in skip:
            entry[key] = val

    doctorants.append(entry)
    existing_names.add(name_upper)
    added += 1

print(f"  {added} nouveaux doctorants ajoutes")

with open(DOC_PATH, "w", encoding="utf-8") as f:
    json.dump(doctorants, f, ensure_ascii=False, indent=2)

print(f"  Total doctorants: {len(doctorants)}")

# ──────────────────────────────────────────────
# MISE A JOUR DES CHERCHEURS: phd_students corrige
# ──────────────────────────────────────────────
print("\nMise a jour des chercheurs avec les listes PhD completes...")

# Construire un index directeur -> liste doctorants
director_map = {}
for doc in doctorants:
    directors = []
    if doc.get("director"):
        directors.append(doc["director"])
    if doc.get("co_director"):
        directors.append(doc["co_director"])
    for cd in doc.get("co_directors", []):
        directors.append(cd["name"])

    for director in directors:
        # Normalisation simple
        norm = " ".join(director.upper().split())
        if norm not in director_map:
            director_map[norm] = []
        director_map[norm].append({
            "name": doc["name"],
            "start_date": doc.get("start_date"),
            "subject": doc.get("Sujet", ""),
            "status": doc.get("status", "active"),
        })

with open(EC_PATH, "r", encoding="utf-8") as f:
    chercheurs = json.load(f)

ec_updated = 0
for c in chercheurs:
    raw_name = c.get("name", "")
    # Chercher dans director_map
    norm = " ".join(raw_name.upper().split())
    # Essai exact puis par mots-clés
    match = director_map.get(norm)
    if not match:
        parts = norm.split()
        for key, val in director_map.items():
            if all(p in key for p in parts):
                match = val
                break

    if match:
        current = [d for d in match if d["status"] == "active"]
        past = [d for d in match if d["status"] == "defended"]
        c["phd_students_current_thesesfr"] = current
        c["phd_students_defended_thesesfr"] = past
        ec_updated += 1

with open(EC_PATH, "w", encoding="utf-8") as f:
    json.dump(chercheurs, f, ensure_ascii=False, indent=2)

print(f"  {ec_updated} chercheurs mis a jour avec index PhD automatique")

print("\nEnrichissement complet termine!")
print(f"  Doctorants total en base: {len(doctorants)}")
print(f"  Dont defenses: {sum(1 for d in doctorants if d.get('status') == 'defended')}")
print(f"  Dont actifs: {sum(1 for d in doctorants if d.get('status') == 'active')}")
