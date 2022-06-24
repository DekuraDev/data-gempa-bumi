# -*- coding: utf-8 -*-

# open source code 
# get data gempa bumi indonesia bmkg
# coder = DekuraDev


import os,sys,requests,json

link = "http://feriirawan-api.herokuapp.com/list/bmkg/"

response = requests.get(link).json()
try:
    print("\n [×] "+response["message"])
    for i in response["gempa"]:
        print("\n ! wilayah gempa: "+i["wilayah"])
        print(" ! besar magnitudo: "+i["magnitudo"])
        print(" ! kedalaman: "+i["kedalaman"])
        print(" ! lintang: "+i["lintang"])
        print(" ! bujur: "+i["bujur"])
        print(" ! waktu gempa: "+i["waktu_gempa"].split(" ")[0]+" - "+i["waktu_gempa"].split(" ")[1]+" "+i["waktu_gempa"].split(" ")[2])
except Exception as e:
    print(e)