# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.

import os

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

from django.views.decorators.csrf import csrf_exempt


def botView1(request):
	return render(request,'login.html')


##bot  = ChatBot('Test')
##bot.set_trainer(ListTrainer)

bot = ChatBot('Jarvis',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# bot.train("chatterbot.corpus.english")

bot.get_response("Hi, This is Jarvis. How are you today?")


##for _file in os.listdir('bot_app/files'):
##	try:
##		conv = open('bot_app/files/'+_file,'r').readlines()
##		bot.train(conv)
##	except:
##		conv="You did something. Bye!"
	
@csrf_exempt
def botView(request):
	context_dict = {}
	context = RequestContext(request)
	
	if request.method == 'POST':
		textbox = request.POST.get('textbox1',)
		
		while True:
			try:
				request = textbox
				response = bot.get_response(request)
				# print('Bot: {}'.format(response))
				context_dict.update({'chat_response':response})
				return render_to_response('login.html',context_dict,context)
			except:
				print('You wanna close the chat')
				response = "Ended the conversation"
				context_dict.update({'chat_response':response})
				return render_to_response('login.html',context_dict,context)
			
	else:
		return render(request,'login.html')


