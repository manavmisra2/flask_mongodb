
These versions were the actual versions of my dev environment
* Python 3.6.1
* pip 9.0.1
* virtualenv 15.1.0
* MongoDB shell version: 3.2.16
* Node v6.10.1
* NPM 3.10.10

Create virtualenv
```bash
cd pizzaservice
virtualenv venv
```

Activate virtualenv
```bash
. venv/Scripts/activate # on windows
. venv/bin/activate # on ubuntu
```

Install requirements
```bash
pip install -r api/requirements.txt
```

Optional: Repair broken data.json; the valid json already exists in `data/json/`
```bash
cd scripts
python json_parser.py
```

### Persistence with [MongoDB](https://www.mongodb.com/)
Start MongoDB daemon
```bash
mongod --config mongod.conf
```

Generate database and insert pizzas and extras into collections
```bash
cd scripts
python init_db.py
```

Connect to MongoDB shell for debugging reasons
```bash
mongo pizzaservice
show collections
db.pizzas.find()
db.extras.find()
```

### API with [Flask](http://flask.pocoo.org/)
Start the API (e.g. on a Windows based machine within the pizzaservice dir)
```bash
export FLASK_APP=api/app.py
export FLASK_DEBUG=1
flask run
```

The API base path is [http://localhost:5000/api/v1/](http://localhost:5000/api/v1/) with CORS enabled

To stop the API, hit `ctrl + c`
```bash
deactivate
```

