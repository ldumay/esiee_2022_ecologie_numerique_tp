# ESIEE - 2022 - Ecologie numerique TP

## Backend

### 1 - Pré-requis :

- Python : **v3.10.7**

### 2 - Initialiser et récupérer les dépendances d'un projet python

🚨 C'est la première fois que je fais un projet python, si jamais une commande ne fonctionne pas, n'hésitez pas à corriger le document

Flask se lance en suivant les routes défini dans un fichier app.py

Les 2 premières étapes servent à configurer un projet en local, afin d'installer les dépendances que pour ce projet.
Si vous voulez installer les dépendances en global, vous pouvez les ignorer

#### 2.1 - Créer un environnement local 

```python -m venv venv```

#### 2.2 - Utiliser la console lié à l'environnement local

Docs : https://docs.python.org/3/library/venv.html

- Mac / Linux / WSL : 

```
source venv/bin/activate
```

- Windows - CMD : 

```
Par défaut :
. ./venv/Scripts/activate

Via CMD :
venv/Scripts/activate.bat

Via PS : 
venv/Scripts/Activate.ps1
```

### Bonus : Changer l'interpréteur pour VS Code

` Ctrl + Maj + P `

Sélectionner Python Interpreter

Sélectionner `venv/Scripts/python.exe`

Le code s'adaptera selon les modules installés dans l'environnement local

#### 2.3 - Installer toutes les dépendances lié au projet 

```
pip install -r requirements.txt
```

#### 2.4 - Lancer l'application backend python avec flask

```
python -m flask run
```
---

Lancer avec le debug :

Changer dans `app.py`

> app.run(debug=True)

Éxécuter avec le debug

```
python app.py
```

---

#### 2.5 - Création et migrationd de la base de données

```
python -m flask db init
flask db migrate -m "entries table"
flask db upgrade
```

### 3 - Accès à API

- **[GET]** Test : [http://localhost:5000/test/](http://localhost:5000/test/) ==> View : [datas-test]
- **[GET]** Datas : [http://localhost:5000/data/](http://localhost:5000/data/) ==> View : [datas]