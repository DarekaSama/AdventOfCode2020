import os
path = "C:/Users/utilisateur/Desktop/eventInfoCalendrier/Jour1/défi1/"
os.chdir(path)
fichier = open("page.txt","r")
list = fichier.readlines()
for i in range(len(list)):
    list[i] = int(list[i])
    for x in range(len(list)):
        for z in range(i+1,len(list)-1):
            res1 = int(list[x])
            res2 = int(list[z])
            sol = res1 + res2
            if sol == 2020:
                print(res1*res2)