# 1 Audit du code

---

## Backend : Python/Django

### Code Quality

flake8

avec flake8 dans le backend puis on cree un fichier de configuration .flake8 pour ignorer les dossiers node_modules et static.

uv run flake8 .

on obtient un rapport dans le terminal avec les erreurs.
on constate qu'il ya un probleme unique qui se repete plusieurs fois (E501 line too long) et qui est causé par des ligne de code qui depasse les caracteres autorisés par flake8.
pour resoudre cela , on peut utiliser Black pour formater automatiquement le code et respecter les normes de style.

### Testing

pytest

uv run pytest

on obtient un rapport de test dans le terminal avec les tests qui ont réussi et ceux qui ont échoué.
on constate que les 64/64 test ont reussi , il ya 3 avertissement qui sont liées au manque de dossier staticfile , qui peut etre ignoré pour le moment car il n'est pas essentiel pour le fonctionnement de l'API.

### Deployment Process

le backend utilise Docker pour le déploiement, avec un Dockerfile qui définit l'image de base, les dépendances et les commandes pour démarrer l'application.
puis un docker-compose.yml pour orchestrer les services (API et base de données).

### Monitoring

Dans le backend on peut simplement utliser les logs Django pour monitorer les requetes et les erreurs de l'API.

cat debug.log

cette commande affiche les logs de debug dans le terminal, ce qui permet de suivre les requetes et les erreurs de l'API en temps réel.

cette approche est tres basique , mais on peut utiliser grafana pour monitorer les performances de l'API et les métriques de la base de données en utilisant des exporters comme prometheus pour collecter les données et les visualiser dans grafana.

### Security

Niveau securité , on peut utiliser trivy pour scanner les images Docker à la recherche de vulnérabilités.
trivy fs .

apres execution on obtient un tableau detaillé dans le terminal
0 vulnerabilites timescaledb
et 5 vulnerabilites uv.lock dont des CVEs critiques , qui peuvent etre resolu en mettant a jour les packages ou en appliquant des correctifs de securité.

La solution ici est de mettre a jour Django et d'appliquer les correctifs de securité pour les packages vulnérables.

---

## Frontend : Vue.js

### Code Quality

eslint

avec eslint dans le backend on peut obtenir un rapport des erreurs de style et de syntaxe dans le code.

npm run lint

rien n'est retourné par la commande , ce qui signifie que le code respecte les normes de style et qu'il n'y a pas d'erreur de syntaxe.

### Testing

Vitest

npm run test:unit

Il n'existe pas de test unitaire pour le moment , donc aucun test n'est exécuté et aucun rapport n'est généré.

### Deployment Process

le frontend utilise également Docker pour le déploiement, avec un Dockerfile qui définit l'image de base, les dépendances et les commandes pour démarrer l'application.
puis un docker-compose.yml pour orchestrer les services (frontend et backend).

### Monitoring

pour le frontend on peut utiliser lighthouse qui permet de monitorer les performances de l'application web, l'accessibilité et les bonnes pratiques.

npm install -g lighthouse

puis on peut utiliser la commande
lighthouse http://localhost:3000
pour obtenir un rapport détaillé sur les performances de l'application, l'accessibilité et les bonnes pratiques, ce qui permet d'identifier les points à améliorer pour optimiser l'expérience utilisateur.

### Security

pour le frontend on peut utiliser npm audit pour identifier les vulnérabilités dans les dépendances du projet.
npm audit
cette commande permet d'auditer les dépendances du projet et de signaler les vulnérabilités connues, ce qui permet de prendre des mesures pour sécuriser l'application en mettant à jour les dépendances ou en appliquant des correctifs.

apres utilisation de la commande on trouve 6 vulnerabilites severe , principalement de dependance qu'on peut
resoudre en faisant mettant a jour les packages / supprimant les packages vulnerable

---

# 2 Audit Systeme

### Code Quality

Ce qui manque : Analyse statique automatisée et formatage automatique.
Manuel : Correction des erreurs signalées par flake8 ou eslint.
Automatisé : Analyse avec flake8, eslint.
Points critiques : Non-respect des conventions de style, code non maintenable.

### Testing

Ce qui manque : Tests end-to-end pour le frontend, couverture des cas limites.
Manuel : Écriture des tests.
Automatisé : Exécution avec pytest et vitest.
Points critiques : Tests insuffisants ou non mis à jour.

### Deployment Process

Ce qui manque : Rollback automatisé, vérification des dépendances avant déploiement.
Manuel : Mise à jour des fichiers de configuration.
Automatisé : Déploiement avec Docker Compose et GitHub Actions.
Points critiques : Erreurs humaines, dépendances non vérifiées.

### Monitoring

Ce qui manque : Suivi des performances, alertes en cas d'erreurs critiques.
Manuel : Vérification des logs.
Automatisé : Utilisation de Grafana et Lighthouse.
Points critiques : Logs non surveillés, absence d'alertes.

### Security

Ce qui manque : Analyse régulière des vulnérabilités, validation des mots de passe.
Manuel : Révision des dépendances et configurations.
Automatisé : Analyse avec Trivy, npm audit.
Points critiques : Fichiers sensibles exposés, dépendances vulnérables.

### Documentation

Ce qui manque : Documentation des processus de déploiement et monitoring.
Manuel : Rédaction de la documentation.
Automatisé : Génération de documentation API avec Swagger ou Sphinx.
Points critiques : Documentation obsolète ou incomplète.

---

### Plan d'amélioration

### Code Quality

Short-term fix: Utiliser flake8 et eslint pour identifier et corriger les erreurs de style.
Long-term solution: Intégrer des outils de formatage automatique (Black pour Python, Prettier pour JavaScript) dans le pipeline CI/CD.
Tools/technologies: flake8, eslint, Black, Prettier.

---

### Testing

Short-term fix: Ajouter des tests manquants pour les cas critiques (ex. tests end-to-end pour le frontend).
Long-term solution: Automatiser l'exécution des tests dans le pipeline CI/CD.
Tools/technologies: pytest, vitest, GitHub Actions, GitLab CI/CD.

---

### Deployment Process

Short-term fix: Vérifier manuellement les dépendances avant chaque déploiement.
Long-term solution: Ajouter une étape de vérification des dépendances et un mécanisme de rollback dans le pipeline CI/CD.
Tools/technologies: Docker Compose, GitHub Actions, Trivy.

---

### Monitoring

Short-term fix: Configurer Grafana pour capturer les erreurs en production.
Long-term solution: Mettre en place un tableau de bord avec Grafana pour surveiller les performances et les métriques.
Tools/technologies: Grafana, Lighthouse

---

### Security

Short-term fix: Analyser les dépendances avec Trivy et npm audit, et corriger les vulnérabilités critiques.
Long-term solution: Mettre en place une analyse régulière des vulnérabilités dans le pipeline CI/CD.
Tools/technologies: Trivy, npm audit.

---

# Advanced Git 

### Branch Protection
Pour setup branch protections sur la main branch 

cours_infrastructure_devops > settings > Branches > Add rule > Ruleset name : main > 
- Require PR reviews
- Require status checks to pass
- Require signed commits

### PR Template
Dans le repo , on peut ajouter un template de PR pour standardiser les informations fournies lors de la création d'une pull request.

.github/pull_request_template.md

### Conflict Simulation

- creation d'une branche feature depuis main par exemple feature-branch
- puis on met des modifs dans un fichier par exemple conflit.md et on push la branche feature-branch
- je reviens sur la main et je fais une modif dans le meme fichier conflit.md et je push la main branch
- ensuite je tente de merger la branche feature-branch dans main et je rencontre un conflit