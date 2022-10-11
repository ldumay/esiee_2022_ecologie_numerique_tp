# ESIEE - 2022 - Ecologie numerique TP

## Récupérer les dépendances d'un projet python
/!\ C'est la première fois que je fais un projet python, si jamais une commande ne fonctionne pas, n'hésitez pas à corriger le document

Flask se lance en suivant les routes défini dans un fichier app.py

Les 2 premières étapes servent à configurer un projet en local, afin d'installer les dépendances que pour ce projet.
Si vous voulez installer les dépendances en global, vous pouvez les ignorer

- Créer un environnement local
python -m venv venv

- Utiliser la console lié à l'environnement local
	- Source : https://docs.python.org/3/library/venv.html
	- Mac / Linux / WSL :
		source venv/bin/activate
	- Windows :
		Défaut: . ./venv/Scripts/activate
		CMD: ./venv/Scripts/activate.bat
		PowerShell: ./venv/Scripts/Activate.ps1

- Installer toutes les dépendances lié au projet
pip install -r requirements.txt

Lancer python flask
python -m flask run

--- 

# Autre 😉

## Backend

## Pré-requis :

- Python : **v3.10.7**
- Flask : **_**

## But : API

- Page de test : [http://localhost:8001/helloworld/](http://localhost:8001/helloworld/) ==> View : Hello world
- Page de demonstration : [http://localhost:8001/demo/](http://localhost:8001/demo/) ==> View : [datas]

---

### TESTS

```
git clone https://github.com/gurkanakdeniz/example-flask-crud.git
cd example-flask-crud/
```

#### Préparation et activation de l'environement :

- sur Linux :

```
python3 -m venv venv
source venv/bin/activate
```

- sur Windows :

```
py -m venv venv
. .\venv\Scripts\activate
```

#### Installation des pré-requis :

```
pip install --upgrade pip
pip install -r requirements.txt
```
export FLASK_APP=crudapp.py

#### Préparation de la db :

```
flask db init
flask db migrate -m "entries table"
flask db upgrade
```

#### Démrrage du projet :

```
flask run
```

```
pip install flask
pip install flask-swagger-ui
```