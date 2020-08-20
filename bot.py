def bott():
    import json
    import random
    import pyttsx3 as py
    engine = py.init('sapi5', debug = True)
    engine.setProperty('rate', 190)

    while(1):
        with open('mainknowledge/MainKnowledge.json') as knowledge_file:
            knowledge_dict = json.load(knowledge_file)
        knowledge_file.close()
        question = input("You:")
        if(('quit' or 'exit' or 'termiante' or 'bye') in question):
            engine.say('Bye Bye Its nice talking you')
            engine.runAndWait()
            knowledge_file.close()
            exit()

        elif question not in knowledge_dict:
            engine.say('I do not know what u r saying helpme to increase my knowledge by telling me the correct response for your question')
            engine.runAndWait()
            response = input("Train Me:")
            knowledge_dict.update({question.lower():response.lower()})
            with open("mainknowledge/MainKnowledge.json", "r+") as knowledge_file:
                knowledge_file.seek(0)
                json.dump(knowledge_dict, knowledge_file)

        else:
            random_integer = random.randint(0,len(knowledge_dict[question])-1)
            if(len(knowledge_dict[question]) > 1):
                print('Naruto:'+knowledge_dict[question][random_integer])
                engine.say(knowledge_dict[question][random_integer])
                engine.runAndWait()
            else:
                print(type(knowledge_dict[question][0]))
                engine.say(knowledge_dict[question][0])
                engine.runAndWait()

        knowledge_file.close()



if __name__ == '__main__':
    bott()
