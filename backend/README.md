## Récupérer les dépendances d'un projet python
/!\ C'est la première fois que je fais un projet python, si jamais une commande ne fonctionne pas, n'hésitez pas à corriger le document

Flask se lance en suivant les routes défini dans un fichier app.py

Les 2 premières étapes servent à configurer un projet en local, afin d'installer les dépendances que pour ce projet.
Si vous voulez installer les dépendances en global, vous pouvez les ignorer

- Créer un environnement local
python -m venv venv

- Utiliser la console lié à l'environnement local
	https://docs.python.org/3/library/venv.html
	- Mac / Linux / WSL :
		source venv/bin/activate
	- Windows :
		CMD: venv/Scripts/activate.bat
		PS: venv/Scripts/Activate.ps1

- Installer toutes les dépendances lié au projet
pip install -r requirements.txt

Lancer python flask
python -m flask run