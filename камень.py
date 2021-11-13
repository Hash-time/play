import easygui as gui
title = "Application"

gui.ccbox("Выберите игру:", title, choices = ("Камень, ножницы, бумага", "Угадай число"))
out = gui.ccbox("Выберите", title, choices=("Камень", "Ножницы", "Бумага"), image="0.png")
gui.msgbox(out, "Application", image="0.png")

out = gui.buttonbox("", title, choices=[str(i) for i in range(1,5)])
gui.msgbox(out, "hgg", "iuj", image="0.png")

images = ('0.png', '0.png')
out = gui.buttonbox("", title, choise = ['rhf' + str(i) for i in range(1,6)], images = images)
images = ('0.png', '0.png')
out = gui.buttonbox("", title, choices=['Ryjgrf'])