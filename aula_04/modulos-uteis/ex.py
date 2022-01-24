import dotenv
import os
import subprocess
import random

dotenv.load_dotenv() # .env

USERNAME = os.getenv('APP_USER')

os.environ # retorna todas as variaveis de ambiente
os.path.abspath('.') # retorna o caminho absoluto de um diretorio ou arquivo

subprocess.run('ls', '-l')