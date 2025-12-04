from datetime import datetime
from random import randrange
from tkinter import *  

date = datetime.today()
x = 1
y = date.minute+5

#Функция часов/дней недели/месяца и эмоций
def clock():
    global x, y
    mother = {1:"Январь", 2:"Февраль", 3:"Март", 4:"Апрель", 5:"Май", 6:"Июнь", 7:"Июль", 8:"Август", 9:"Сентябрь", 10:"Октябрь", 11:"Ноябрь", 12:"Декабрь"}
    weekday = {1:"Понедельник", 2:"Вторник", 3:"Среда", 4:"Четверг", 5:"Пятница", 6:"Суббота", 7:"Воскресенье"}
    emotions = {1:"^_^", 2:"\^o^/", 3:">.<", 4:"-_-", 5:";_;", 6:":O", 7:">:(", 8:"-_^"}
    date = datetime.today()
    if date.minute == y or y>60:
        x = randrange(1, 9, 1)
        y = 0 if y>60 else y+5

    
    return f"""
        {date.hour}{":" if date.second%2 == 0 else " "}{"0" if date.minute <= 9 else ""}{date.minute}{"" if date.second%2 == 0 else " "}{emotions[x]: ^20} 

Месяц:        {mother[date.month]: ^20}
День:         {date.day: ^20}
День недели: {weekday[date.isoweekday()]: ^20}\n\n"""

def clicked():
    print("click!")

def update_text():
    lbl.config(text=clock())
    window.after(1000, update_text)



# Обработка окна с часами
window = Tk()   
var = StringVar(value="—")
window.title("yamaflip")
window.geometry("210x120")

lbl = Label(window)
lbl.place(x=0, y=0)

update_text()
window.mainloop()