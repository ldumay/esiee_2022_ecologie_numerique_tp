# ESIEE - 2022 - Ecologie numerique TP

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