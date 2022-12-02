from flask import Flask, request
from flask_api import status
import requests
import platform
import psutil

app = Flask(__name__)
psRam = psutil.virtual_memory()
ram = psRam.total
@app.route('/status')
def status():
    my_system = platform.uname()
    

    features = {'System': my_system.system,
                'Release':my_system.release,
                'version': my_system.version,
                'Processor': my_system.processor,
                'Machine': my_system.machine,
                'Memory_Ram': ram
                }
    return features

@app.route('/poke/<pokemon>')
def poke(pokemon):

    ENDPOINT = 'https://pokeapi.co/api/v2/pokemon/'+pokemon
    response = requests.get(ENDPOINT)
    response = response.json()
    
    return response['abilities'][1]



if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 9000, debug = True)


