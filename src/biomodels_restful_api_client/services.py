import os
import requests

from .constants import API_URL


# GET /{model_id}?format=json|xml
def get_model_info(model_id, out_format="json"):
    response = requests.get(API_URL + "/" + model_id + "?format=" + out_format)
    if out_format == "xml":
        # todo: implement me
        output = None
    else:
        output = response.json()
    return output


# GET /model/files/{model_id}
def get_model_files_info(model_id, out_format="json"):
    response = requests.get(API_URL + "/model/files/" + model_id + "?format=" + out_format)
    if out_format == "xml":
        # todo: implement me
        output = None
    else:
        output = response.json()
    return output


# GET /model/identifiers
def get_model_identifiers(out_format="json"):
    response = requests.get(API_URL + "/model/identifiers?format=" + out_format)
    return response.json()


# GET /model/download/{model_id}
def download(model_id, filename = None):
    DOWNLOAD_URL = API_URL + "/model/download/" + model_id
    local_file = filename
    if filename is not None:
        response = requests.get(DOWNLOAD_URL + "?filename=" + filename)
    else:
        response = requests.get(DOWNLOAD_URL)

    # Save the file data to the local file
    with open(local_file, 'wb') as file:
        file.write(response.content)

    return os.path.abspath(local_file)


"""
MODEL SEARCH OPERATIONS
"""


# GET /search
def search(query="*:*", offset=0, num_results=10, sort="publication_year-desc", out_format="json"):
    search_url: str = API_URL + "/search?query=" + query + "&offset=" + str(offset)
    search_url += "&numResults=" + str(num_results) + "&sort=" + sort + "&format=" + out_format
    results = requests.get(search_url)
    return results.json()


"""
PARAMETERS SEARCH
"""


# GET /parameterSearch/search
def parameter_search(query="*:*", start=0, size=10, sort="model:ascending", out_format="json"):
    search_url: str = API_URL + "/parameterSearch/search?query=" + query + "&start=" + str(start)
    search_url += "&size=" + str(size) + "&sort=" + sort + "&format=" + out_format
    results = requests.get(search_url)
    return results.json()
