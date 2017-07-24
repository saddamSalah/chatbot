# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import createdb


def createbot():
    bot = ChatBot(
        "Demma",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
            },
            {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.15,
                'default_response': 'I am sorry, but I do not understand.'
            }
        ],
        input_adapter="chatterbot.input.TerminalAdapter",
        output_adapter="chatterbot.output.TerminalAdapter",
        database="./storage/DB.db"
    )
    return bot


def trainbot(bot):
    bot.set_trainer(ListTrainer)
    bot.train([
        "I want to travel",
        "season/specific dates ? ",
        "season",
        "summer season / winter ?",
        "summer",
        "we have package for summer season in alex ",
        "winter",
        "we have package for winter in aswan ",
        "specific dates, summer",
        "we have a package from 2nd to 8th  in Alex",
        "specific dates, summer",
        "we have a package from 2nd to 8th  in Alex",
        "specific dates, summer",
        "we have a package from 2nd to 8th  in Alex",
        "specific dates, autmn",
        "we have a package from 2nd to 8th  in cairo",
        "specific dates, autmn",
        "we have a package from 2nd to 8th  in cairo",
        "specific dates, winter",
        "we have a package from 2nd to 8th  in Aswan",
        "specific dates, winter",
        "we have a package from 2nd to 8th  in Aswan",
        "specific dates, winter",
        "we have a package from 2nd to 8th  in Aswan",
        "reservation hotel",
        " in our hotels You will be impressed we have a five stars hotels",
        "transportation",
        "flight, Buses",
        "name",
        "my name is Deema",
        "Age",
        "26",
    ])
    bot.set_trainer(ChatterBotCorpusTrainer)
    bot.train(
        "chatterbot.corpus.english.greetings",
    )
    return bot


def get_personal_info():
    raw_question = ["What's your name?", "How old are you?", "what's your nationality?", "What's your occupation?"]
    ans = []
    for i in raw_question:
        print i
        ans.append (raw_input())
    return ans


def confirm():
    print"Your Name:", record[0], ",You Have:", record[1], "Years Old", ",You are:", record[2], ",You Work As:", record[3]
    print "To Confirm information press 's' OR press any key To Retry "
    answer = raw_input()
    return answer

if __name__ == "__main__":
    print("Hello")
    Abot = createbot()
    bot = trainbot(Abot)
    record = get_personal_info()
    answer = confirm()
    while answer != 's':
        record = get_personal_info()
        answer = confirm()
    print" Hello", record[0]
    cur,conn = createdb.connect()
    record.insert(0, None)
    createdb.insert(conn,cur, (record,))    #register the information of the client after
    print"Database of Deema contains the following records:"  #confirmed in sqlite database
    createdb.selectAll(cur)
    createdb.close(conn)
    print"How Can i help you? "
    while True:
        try:
            bot.get_response(None)
        # Press  ctrl-d on the keyboard to exit
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

