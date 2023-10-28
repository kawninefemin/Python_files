qna = {'Hello': 'hii',
       'What is your name': "my name is femin",
       'what is your last online course you have completed?': 'Digital marketing foundation offered by goggle',
       'Is it worth for basic learning ?': 'yes,of course',
       'okay I will enroll': 'great'
       }

while True:
    try:
        qs = input()

        if qs == "quit":
            break
        else:
            print(qna[qs])
    except:
        print("talk you later")
