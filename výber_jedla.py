import tkinter # import plátna
from tkinter import *
canvas = tkinter.Canvas(width=810, height=400, bg='white') # vytvorenie plána (širka, výška, farba pozadia) 
canvas.pack() # nahranie plátna

canvas.create_text(405,50,fill="black",font=("Arial",'40','bold'),text="VÝBER JEDLA") # vytvorenie textu VÝBER JEDLA na súradniciach 405,50, ktorý má čiernu farbu, je tučný a veľkosť má 40 
canvas.create_rectangle(10, 100, 200, 300, fill='green') # vytvorenie zeleného štvorca
canvas.create_rectangle(220, 100, 400, 300, fill='red') # vytvorenie červeného štvorca
canvas.create_rectangle(420, 100, 600, 300, fill='blue') # vytvorenie modrého štvorca
canvas.create_rectangle(620, 100, 800, 300, fill='orange') # vytvorenie oranžového štvorca

button1=tkinter.Button(canvas, text="VYBRAŤ JEDLO", height = 2, width = 20) # vytvorenie tlačitka s nápisom VYBRAŤ JEDLO, ve vysoké 2 a široké 20
button1.place(x=340, y=350) # tlačítko sa nachádza na súradniciach x=340 a y=350
canvas.mainloop() # opakovací cyklus pre tlačítko

canvas.bind('<Button-1>') # bind na ľavé tlačitko myši
