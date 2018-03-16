import os
from jinja2 import FileSystemLoader, Environment
from dotenv import load_dotenv

load_dotenv('./.env')

username = os.getenv('ADMIN_USERNAME')
password = os.getenv('ADMIN_PASSWORD')
source_password = os.getenv('SOURCE_PASSWORD')
relay_password = os.getenv('RELAY_PASSWORD')


templateLoader = FileSystemLoader(searchpath='./')
templateEnv = Environment(loader=templateLoader)
TEMPLATE_FILE = './templates/icecast.xml'
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(
    username=username,
    password=password,
    source_password=source_password,
    relay_password=relay_password
)

icecast_config = open('./icecast.xml', 'w')
icecast_config.write(outputText)
icecast_config.close()
