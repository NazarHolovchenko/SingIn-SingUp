from tkinter import*
# Вікно другого рівня вкладеності
window = Tk()
window.title('Головна')
window.geometry('1200x800')
window.config(bg='#b3b3b3')


#window.iconbitmap('hoverla.ico')


top_tx=Label(window,
            text='Говерла – найвища гірська вершина в Україні. \nЗаввишки вона — 2061 м над рівнем моря. \nРозташована в Карпатах, у гірському масиві \nЧорногора, на межі Івано-Франківської та \nЗакарпатської областей. Назва «Говерла» \nпоходить від угорського «hóvár», \nщо означає «снігова гора». ',
            bg='#737373',
            fg='black',
            font=('Comic Sans MS',18,'bold'),
            relief=GROOVE,
            bd=1,
             width=18,
             height=4,
            justify=CENTER,
            # anchor=N,
             #pady=20,
            )
top_tx.place(x=1,y=1,width=600,height=400)

wwww_tx=Label(window,
            text='Справді, вершина гори вкрита снігом \nмайже завжди;  сніговий покрив тане в \nлипні,й то не завжди. Говерлою гора \nстала через …помилку. Спочатку гуцули \nназивали її «Говирла», але коли \nавстрійські картографи складали мапу \nмісцевості, котрийся з них записав \n«Говерла». Так і лишилося…',
            bg='#737373',
            fg='black',
            font=('Comic Sans MS',18,'bold'),
            relief=GROOVE,
            bd=1,
             width=18,
             
            justify=CENTER,
            )
wwww_tx.place(x=600,y=1,width=600,height=400)
# кнопки 2-го рівня
# kn_1=Button(window,
#             text='Увійти',
#             font=('Arial',24),
#             borderwidth=1,
#             # command=lambda:pushButton(1),
#             # command=lambda:login(),
#             )
# kn_1.place(x=310,y=250,width=250,height=50)

# kn_2=Button(window,
#             # window.destroy(),
#             # os.system('singup.py'),
#             text='Зареєструватися',
#             font=('Arial',24),
#             borderwidth=1,
#             command=lambda:window.destroy(),
#             )
# kn_2.place(x=40,y=250,width=250,height=50)

window.mainloop()
