import requests

SEARCH_URL = "https://collectionapi.metmuseum.org/public/collection/v1.1"
OBJ_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def get_artwork_details(objectid):
    artwork_response = requests.get(f'{OBJ_URL}/objects/{objectid}', timeout=15)

    artwork_response.raise_for_status()

    artwork = artwork_response.json()

    return artwork



def get_image_url(artwork):
    image_url = artwork.get("primaryImage")
    if image_url:
        return image_url
    else:
        return

def get_image(image_url):
    if image_url:
        response = requests.get(image_url, timeout=15)
        response.raise_for_status()

def get_title_and_artist(artwork):
    return artwork.get("title"), artwork.get("artistDisplayName")

def get_objects_with_pictures():
    response = requests.get(
        f'{SEARCH_URL}/search',
        params={'hasImages':'true'},
        timeout=15)

    response.raise_for_status()
    results = response.json()

    object_ids = results.get("objectIDs") or []

    return object_ids


print(get_image_url(get_artwork_details(get_objects_with_pictures()[1])))
