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

```
python -m venv venv
```

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
python -m pip install -r requirements.txt
```

> **Si besoin de mettre à jour de fichier `requirements.txt`** :
> 
> ```
> python -m pip freeze > requirements.txt
> ```

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

### 3 - Accès à API

- **[GET]** Test : [127.0.0.1:5000/test/](http://127.0.0.1:5000/test/) ==> View : [datas-test]
- **[GET]** Datas : [127.0.0.1:5000/data/](http://127.0.0.1:5000/data/) ==> View : [datas]

- **[GET-POST-PUT-DELETE]** BDD : `http://localhost:5000/sample_methodes` ==> View [result]

- **[GET]** BDD : `http://127.0.0.1:5000/bdd/` ==> View : [result]
- **[POST]** BDD : `http://127.0.0.1:5000/bdd/create` ==> View : [result]
- **[PUT]** BDD : `http://127.0.0.1:5000/bdd/update/<id>` ==> View : [result]
- **[DELETE]** BDD : `http://127.0.0.1:5000/bdd/delete/<id>` ==> View : [result]

Variables de test

```
{
"heure": 2022-01-01 00:00:03,
"intencite": 2,
"temperature": 2,
"vitesse": 2,
}
```

---[Recherches]---

- [Flask by Example – Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [YOUTUBE - Learning Flask - Managing the database with flask-migrate and flask-sqlalchemy](https://www.youtube.com/watch?v=Ngxu0_xiZhQ)
- [Declaring Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/?highlight=float)
- [Session Basics](https://docs.sqlalchemy.org/en/13/orm/session_basics.html)
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
- [L'opérateur conditionnel ternaire en Python](https://karbotronics.com/blog/2020-03-03-python-operateur-ternaire/)