import requests

url = 'http://127.0.0.1:8000/consolas/'

user = requests.get('http://127.0.0.1:8000/users/5')
user_data = user.json()
print(user_data['id'])

consola_data = {
    "Consola_client": user_data['id'],
}

response = requests.post(url, json=consola_data)

if response.status_code >= 200 and response.status_code <= 299:
    #sucesso
    print('Status code', response.status_code)
    print('Reason', response.reason)
    #print('Reason', response.text)
    #print('JSON', response.json())
    response_data = response.json()
    print(response_data)
    #print(response_data['Username'])
    #print(response_data['email'])
else:
    #erros
    print('Status code', response.status_code)
    print('Reason', response.reason)
    print('Reason', response.text)