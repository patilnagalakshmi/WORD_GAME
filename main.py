import requests
import random
import json
from ran import words_list
from csv import writer


presentation_count = 0
score_count = 0
TOTAL_PRESENTATION_COUNT = 5

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
    return list(set(synonyms))
 


if __name__ == "__main__":
    print("WELCOME TO SYNONYM WORD GAME\n")
    print("||||| LET'S PLAY |||||\n")

    # r = RandomWords()
    output=[]
    while presentation_count < TOTAL_PRESENTATION_COUNT:
        try:
            # word=r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
            word=random.choice(words_list)
            output.append(word)
            print(f"Provide a synonym for: {word}")
            answer = input("Enter your answer: ").strip().lower()

            output.append(answer)
            synonyms = fetch_synonyms(word)

            output.append(synonyms)
            if not synonyms:
                print(f"No synonyms found for {word}. Skipping...\n")
                output.append("No synonyms")
                continue

            if answer in synonyms:
                score_count += 1
                print("You are correct!!!\n")
                output.append("Correct")
            else:
                print(f"Bad Luck! The correct synonyms were: {', '.join(synonyms)}\n")
                output.append("wrong")

        except Exception as e:
            print(f"An error occurred: {e}\n")

        presentation_count += 1

        #to write in csv file
        with open('event.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(output)
            f_object.close()
        

    print("||||| GAME OVER |||||\n")

    if score_count == TOTAL_PRESENTATION_COUNT:
        print("Voila!! You got all synonyms correct.\n")

    print(f"Your Final Score: {score_count} out of {presentation_count}")
