# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Test")

convIntroduction = ["oi", "ola", "ola, bom dia", "bom dia", "bom dia, como vai voce?", "estou bem"]

convFilms = ["que filmes você gosta?", "eu gosto da trilogia senhor dos anéis"]

trainer = ListTrainer(bot)

trainer.train(convIntroduction)
trainer.train(convFilms)

while True:
    quest = input('Você: ')
    response = bot.get_response(quest)
    if float(response.confidence) > 0.5:
        print('Bot: ', response)
    else:
        print('Bot: Não entendi')
