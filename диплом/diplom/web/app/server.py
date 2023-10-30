from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import json

# загружаем модель из файла
with open('models/best_cb_model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg


@app.route('/predict', methods=['POST'])
def predict_func():
	features = request.json
	cols = ['status', 'property_type', 'baths', 'fireplace', 'city', 'sqft',
       'state', 'private_pool', 'year_house_builtt', 'remodeling',
       'parking', 'average_school_rating', 'number_of_schools',
       'average_distance_to_school']
	features_f = pd.DataFrame([features], columns=cols)
	for column in ['sqft', 'target', 'number_of_schools', 'average_school_rating', 'average_distance_to_school', 'baths']:
		features_f[column] = features_f[column].apply(lambda x: abs(x))
		constant = 1e-6
		features_f[column] = np.log(features_f[column] + constant)
	predict = model.predict(features_f)
	return jsonify({'prediction': round(np.exp(predict[0]))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
