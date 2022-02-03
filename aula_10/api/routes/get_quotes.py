
from flask import Blueprint, jsonify , render_template, request
from utils.mongodb_utils import get_database

blueprint = Blueprint("get_quotes", __name__)

@blueprint.route("/b3/historicaldata/quotes")
def get_quotes():
    db = get_database('b3')
    collection = db.get_collection('historicalData')

    quotes = [
        {
           "CODNEG": q.get('CODNEG'), 
           "DATPRG": q.get('DATPRG'),
           "NOMRES": q.get('NOMRES'),
           "PREABE": q.get('PREABE'),
           "PREMAX": q.get('PREMAX'),
           "PREMED": q.get('PREMED'),
           "PREMIN": q.get('PREMIN'),
           "PREULT": q.get('PREULT')
        } for q in collection.find()

    ]

    return render_template("index.html", 
            context=[ quotes[x] for x in range(10) ])

@blueprint.route("/post" , methods = ['POST'])
def ex_post():
    payload = request.json

    return jsonify(payload)



