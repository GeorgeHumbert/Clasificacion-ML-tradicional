from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Cargar el modelo entrenado
modelo_cargado = joblib.load('modelo_random_forest_optimizado.pkl')

# Crear la aplicación Flask
app = Flask(__name__)

# Definir la ruta de la API
@app.route('/predict', methods=['POST'])
def predecir():
    datos = request.get_json()

    # Convertir los datos en un DataFrame
    datos_df = pd.DataFrame([datos])

    # Asegurarse de que las columnas coincidan con las del modelo entrenado
    columnas_entrenamiento = modelo_cargado.feature_names_in_
    datos_df = datos_df.reindex(columns=columnas_entrenamiento, fill_value=0)

    # Realizar la predicción
    prediccion = modelo_cargado.predict(datos_df)

    # Devolver la predicción en formato JSON
    return jsonify({'prediccion': int(prediccion[0])})

if __name__ == '__main__':
    app.run(debug=True)

