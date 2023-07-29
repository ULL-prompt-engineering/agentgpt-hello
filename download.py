import requests

url = 'https://riull.ull.es/xmlui/bitstream/handle/915/7847/reglamento_evaluacion_calificacion2016.pdf'
response = requests.get(url)

if response.status_code == 200:
    with open('reglamento_evaluacion_calificacion2016.pdf', 'wb') as file:
        file.write(response.content)
        print('El PDF se ha descargado correctamente.')
else:
    print('No se ha podido descargar el PDF.')

