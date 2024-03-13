import requests

payload = {
    'content': 'pandaborns1968'
}

header = {
    'authorization': ''
}

for i in range(1000):
    payload = {
        'content': i
    }
    r = requests.post('', data=payload, headers=header)
