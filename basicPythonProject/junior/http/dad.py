import termcolor, requests
from random import choice
# print(help(termcolor))
text = termcolor.colored("Dad Joke 3000", color="blue")
print(text)

input_text = input("Let me tell you a joke! Give me a topic: ")
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": input_text}
).json()

total_jokes = response_json['total_jokes']
results = response_json['results']

if total_jokes > 1:
    print(f"Total jokes are {total_jokes} and here is one of them\n")
    print(choice(results)['joke'])
elif total_jokes == 0:
    print(f"No joke based on this {input_text}\n")
elif total_jokes == 1:
    print(f"Totally one joke, here it is: \n")
    print(results[0]['joke'])