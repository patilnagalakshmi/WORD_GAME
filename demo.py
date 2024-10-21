import requests
import json
word=input()
def fetch_synonyms(word):

  url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
  api_response = requests.request("GET", url)
  res=json.loads(api_response.text)
  synonyms = []
  for entry in res:
    for meaning in entry.get("meanings", []):
        synonyms.extend(meaning.get("synonyms", []))
        for definition in meaning.get("definitions", []):
          synonyms.extend(definition.get("synonyms", []))
    unique_synonyms = list(synonyms)
    return unique_synonyms



print(fetch_synonyms(word))