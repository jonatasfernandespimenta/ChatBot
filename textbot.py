# -*- coding: utf-8 -*-
print("\n")
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice")

bot = ChatBot ("Test")

convA = ["oi", "ois", "eae cara", "eae cara, blz?","blz?","blz", "olá", "olá, bom dia", "bom dia", "bom dia como vai?", "vou bem"]

convB = ["que filmes voce gosta?", "eu gosto de senhor dos aneis"]

convC = ["como vai você?", "vou bem", "que bom"]

convE = ["você esta bem?", "sim, muito", "fico feliz", "por que?"]

convF = ["gosto de você", "eu tambem,e vc?", "eu tbm", "eu não", "eca", "não ligo"]

convG = ["o que gosta de fazer?", "jogar e vc?", "programar", "adoro"]



bot.set_trainer(ListTrainer)

bot.train(convA)
bot.train(convB)
bot.train(convC)

bot.train(convF)
bot.train(convG)

while True:
	quest = input ("Você: ")

	response = bot.get_response (quest)

	speak.speak(response)