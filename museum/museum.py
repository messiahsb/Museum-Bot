import requests

URL = "https://collectionapi.metmuseum.org/public/collection/v1.1/"
PARAMS = {
    'hasImages': 'true'
}
response = requests.get(
        f'{URL}/search',
        params=PARAMS,
        timeout=15)

results = response.json()
