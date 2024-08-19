from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def pscan_CodigoBarra():
    data = request.get_json()
    CodigoBarra = data.get('CodigoBarra')

    df = pd.read.excel('Inventario base prueba.xlsx')

    columna_producto = df[df["Codigo barra"] == CodigoBarra]

    if columna_producto.empty:
        return jsonify({"Error": "Producto no encontrado"}), 404
    
    respuesta = {
        "Producto": columna_producto["Producto"].values[0],
        "inventario": int(columna_producto["Inventario"].values[0]),
        "Id": columna_producto["Id"].values[0],
        "Codigo barra": columna_producto["Codigo barra"].values[0]
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)