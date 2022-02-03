
import flask
import datetime

from utils.mongodb_utils import get_database

from routes.get_quotes import blueprint as get_quotes

app = flask.Flask(__name__)
app.register_blueprint(get_quotes)

@app.route("/", methods = [ 'GET' ] )
def hello():
    return flask.jsonify({
        'message' : 'hello from flask!',
        'timestamp': str(datetime.datetime.utcnow())
    })

@app.route("/outra_rota")
def outro_hello():
    return flask.jsonify({
        'message': 'de outra rota'

    })

@app.route("/b3/historicaldata/<codneg>")
def get_quote_by_codneg(codneg):
    db = get_database('b3')
    collection = db.get_collection('historicalData')

    quote = collection.find_one( { 'CODNEG': codneg }, { '_id': 0  } )

    return flask.render_template('index.html', context=quote)

    #return flask.jsonify(quote)




