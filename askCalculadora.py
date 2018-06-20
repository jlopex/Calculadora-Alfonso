#! python3
import csv
import requests
import sys


# Devuelve la operacion en el formato necesario para hacer el request al servidor (dominio, puerto, path,
# query y parametros)
def createOperation(valor1, valor2, operador):
    result = 'http://127.0.0.1:5000/calcular?valor1=' + valor1 + '&valor2=' + valor2
    if operador in '-*/^':
        result += '&operador=' + operador
    return result


fileName = sys.argv[1]
with open(fileName, 'r') as infile, open('resultados.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    csvdata = list(reader)
    for item in csvdata:
        url = createOperation(item[0], item[2], item[1])
        respuesta = requests.get(url)
        print(item[0] + ' ' + item[1] + ' ' + item[2] + ' = ' + respuesta.text)
        writer.writerow([item[0], item[1], item[2], respuesta.text])
    infile.close()
    outfile.close()