
import pymongo

MONGO_USER = 'usuario_tuma_b3'#.env/variável de ambiente
MONGO_PASSWD = '2d58bba14377dbf144e566a6cac6b131'
MONGO_URI = "mongodb+srv://{username}:{password}@cluster0.8z0o4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


def get_database(database_name: str = 'b3'):
    client = pymongo.MongoClient(
            MONGO_URI.format(username=MONGO_USER,
            password=MONGO_PASSWD))
    return client.get_database(database_name)
