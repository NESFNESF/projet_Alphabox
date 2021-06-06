# -*- coding : utf-8 -*-
from django.shortcuts import render
from random import shuffle
from django.http import HttpResponse
from datetime import datetime
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

score = 0
exemple = list()
tab = list()
list_mots = list()
coun = 0
succ = 0
lettre=""



def index(request):
    return render(request ,"new_word/user_interface.html")

def menu_one(request) :
    return render(request,"new_word/solo_menu.html")

def configuration(request):
    return render(request, "new_word/config_solo_game.html")


def config(request):
    global lettre
    mots = open(os.path.join(BASE_DIR , 'static/dictionnaire.txt'),"r")
    t = mots.readline().lower().split("\n")[0]
    lettre = request.POST['lettre']
    while (t[0]!=lettre):
        t = mots.readline().lower().split("\n")[0]
    
  
    tab.insert(0,t)
    while (t[0]==lettre):
        tab.insert(0,t)
        t=mots.readline().lower().split("\n")[0]
    
    shuffle(tab)
    shuffle(tab)
    shuffle(tab)
    
   
    exemple = list()
    list_mots = list()
  
    j=0
    while(j< 5):
        exemple.insert(0,tab[0]);
        list_mots.insert(0,tab[0])
        del tab[0]
        j = j + 1
    
   
    dif = 0
    texts = ""
    tex=""
    return render(request,"new_word/part_one.html" ,context={
        'score' : score,
        'tab' : tab,
        'exemple' : exemple,
        'list_mots' : list_mots,
        'coun' : coun,
        'succ' : succ,
        'dif' : dif,
        'texts' : texts,
        'tex' : tex,
        'lettre' : lettre,
        
    })
    
def part_one(request):
    global score
    global coun
    global succ
    mot = request.POST['mot']
    t = 0
    
    texts = "mot incorrect !!! -5 points "
    tex = "text-danger"
    while(t< len(tab)):
        if(tab[t]==mot):
            list_mots.insert(0,tab[t])
            score = score + 15
            succ = succ + 1
            texts = "mot correct !!! +15 points "
            tex = "text-success"

            
            del tab[t]
            
       
        t = t + 1
    
    coun = coun + 1
    score = score - 5
    dif = coun - succ
    
    
    return render(request,"new_word/part_one.html" ,context={
        'score' : score ,
        'tab' : tab,
        'exemple' : exemple,
        'list_mots' : list_mots,
        'coun' : coun,
        'succ' : succ,
        'dif' : dif,
        'texts' : texts,
        'tex' : tex,
        'lettre' : lettre,
        
    })
    