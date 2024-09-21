# Proyecto de Clasificación: Supervivencia en el Titanic

Este proyecto implementa un modelo de clasificación para predecir la supervivencia de los pasajeros del Titanic utilizando **Random Forest**. Además, hemos construido una **API con Flask** para realizar predicciones basadas en datos de entrada nuevos.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos y carpetas:

```bash
Proyecto_Titanic/
│
├── A_Feature_Pipeline.ipynb            # Preprocesamiento de datos
├── B_Training_Pipeline.ipynb           # Entrenamiento y optimización del modelo
├── C_Model_Inference.ipynb             # Inferencia del modelo con nuevos datos
├── app.py                              # API Flask para realizar predicciones
├── modelo_random_forest_optimizado.pkl # Modelo entrenado y optimizado
├── requirements.txt                    # Dependencias necesarias
└── README.md                           # Documentación del proyecto
Descripción del Proyecto
Este proyecto tiene como objetivo entrenar un modelo de clasificación para predecir si un pasajero del Titanic sobrevivió o no, basado en diferentes características como la clase, el género, la edad, entre otros.

Utilizamos un pipeline de preprocesamiento para preparar los datos, luego entrenamos un modelo Random Forest y optimizamos sus hiperparámetros. Finalmente, creamos una API con Flask para permitir predicciones en tiempo real con nuevos datos de pasajeros.

Estructura de los Notebooks
A_Feature_Pipeline.ipynb
Propósito: Preprocesar los datos del Titanic, incluyendo la imputación de valores faltantes y la codificación de variables categóricas.
Resultados: Genera un dataset limpio y listo para el entrenamiento del modelo.
B_Training_Pipeline.ipynb
Propósito: Entrenar el modelo Random Forest con hiperparámetros ajustados mediante Grid Search y validación cruzada.
Resultados: Al final de este notebook, se guarda el modelo entrenado y optimizado en un archivo .pkl para su posterior uso.
C_Model_Inference.ipynb
Propósito: Usar el modelo entrenado para realizar predicciones con nuevos datos y guardar los resultados en un archivo CSV.
Resultados: Predicciones realizadas y exportadas a un archivo predicciones.csv.
API Flask para Predicciones
El archivo app.py implementa una API usando Flask que permite enviar datos de entrada en formato JSON y recibir una predicción sobre la supervivencia del pasajero.

Cómo ejecutar la API Flask
1. Instalar las dependencias:
Asegúrate de tener todas las dependencias instaladas:

bash
Copiar código
pip install -r requirements.txt
2. Ejecutar la API:
En la terminal, navega al directorio donde está app.py y ejecuta el siguiente comando:

bash
Copiar código
python app.py
Esto iniciará un servidor local en http://127.0.0.1:5000.

3. Realizar una predicción:
Para hacer una predicción, puedes usar curl o cualquier cliente HTTP como Postman. Aquí tienes un ejemplo de cómo enviar una solicitud POST con curl:

bash
Copiar código
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
    "pclass": 1,
    "sex": 0,
    "age": 29,
    "sibsp": 1,
    "parch": 0,
    "fare": 50,
    "familysize": 1,
    "embarked_c": 1,
    "embarked_q": 0,
    "embarked_s": 0
}'
Respuesta esperada:
json
Copiar código
{
    "prediccion": 1
}
Esto indica que el pasajero probablemente sobrevivió (1 = sobrevivió, 0 = no sobrevivió).

Dependencias
Las dependencias necesarias están detalladas en el archivo requirements.txt. Asegúrate de instalar las bibliotecas usando:

bash
Copiar código
pip install -r requirements.txt
Bibliotecas principales:
scikit-learn: Para el entrenamiento y evaluación del modelo de clasificación.
pandas: Para la manipulación de datos.
Flask: Para construir la API.
joblib: Para guardar y cargar el modelo entrenado.
Cómo Usar el Proyecto
Clonar el repositorio:
bash
Copiar código
git clone <URL_del_repositorio>
cd Proyecto_Titanic
Instalar dependencias:
bash
Copiar código
pip install -r requirements.txt
Ejecutar los notebooks:
Abre los notebooks en Jupyter o en Google Colab para ejecutar el preprocesamiento, el entrenamiento y la inferencia.

Ejecutar la API Flask:
Sigue los pasos mencionados anteriormente para correr la API localmente y realizar predicciones.

Resultados
El modelo de Random Forest optimizado logró una precisión (accuracy) de aproximadamente 82% en el conjunto de prueba. Además, el modelo está integrado en una API Flask que permite realizar predicciones en tiempo real sobre la supervivencia de pasajeros del Titanic con nuevos datos.

Contribuciones
Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio, crear una nueva rama y enviar tus contribuciones mediante un pull request.

Contacto
Para cualquier duda o sugerencia sobre el proyecto, puedes contactarme.
