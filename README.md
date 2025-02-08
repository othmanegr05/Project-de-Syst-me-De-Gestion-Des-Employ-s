# Project-de-Syst-me-de-Gestion-des-Employ-s-
Gestion des Employés est une application développée en Python avec MySQL pour la gestion efficace des informations des employés. Elle permet d'ajouter, modifier, supprimer et afficher les données des employés via une interface simple et intuitive.

📌 Configuration de la base de données :
Avant d'exécuter l'application, vous devez créer une base de données MySQL et une table pour stocker les informations des employés.

📌 Création de la base de données :
CREATE DATABASE SGE;
USE SGE;

📌 Création de la table employer :
CREATE TABLE employer (
    matricule INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    fonction VARCHAR(50) NOT NULL
);

🔧 Configuration de la connexion MySQL :
Dans votre code Python, assurez-vous de modifier les informations de connexion à MySQL en fonction de votre configuration locale

conn = mysql.connector.connect(
    host="localhost",      # Hôte MySQL
    user="votre_utilisateur",  # Remplacez par votre nom d'utilisateur MySQL
    password="votre_mot_de_passe",  # Remplacez par votre mot de passe MySQL
    database="SGE"  # Nom de la base de données
)

Une fois ces étapes complétées, vous êtes prêt à utiliser l'application !!!!