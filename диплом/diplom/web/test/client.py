import requests
import json

 

if __name__ == '__main__':
    
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    r = requests.post('http://localhost/predict', json=['active', 'single family residence', 3, 'yes', 'other', 50, 'NC', 'no', 2019, 'no', 'no_info', 2, 3, 20])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)