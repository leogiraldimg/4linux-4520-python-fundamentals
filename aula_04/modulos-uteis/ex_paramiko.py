from os import getenv

import paramiko
import dotenv


# carregar as informaçoes de variavel de ambiente do arquivo .env local
dotenv.load_dotenv()

# dados sensitivos
HOST = getenv('HOST_IP')
USERNAME = getenv('SSH_USER')
PASSWORD = getenv('SSH_PASSWD')
PORT = getenv('PORT')

# inicializar client do paramiko
client = paramiko.SSHClient()

# adicionar a maquina ao arquivo known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# criar conexao
client.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD)

# executar um comando no host
stdin, stdout, stderr = client.exec_command('ls -l')

# stdout eh como se fosse um buffer

# inspecionar a saida
stdout.readlines()
stdout.read()
