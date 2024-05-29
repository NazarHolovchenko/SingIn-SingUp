from tkinter import*

# Вікно другого рівня вкладеності
window = Tk()
window.title('Головна')
window.geometry('600x400')
window.config(bg='#b3b3b3')

top_tx=Label(window,
            text='Стандартні налаштування',
            bg='#737373',
            fg='black',
            font=('Comic Sans MS',20,'bold'),
            relief=GROOVE,
            bd=1,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=20,
            )
top_tx.place(x=1,y=1,width=598,height=40)

top2_tx=Label(window,
            text='Виберіть команду для редагування',
            bg='#999999',
            # bg='green',
            fg='black',
            font=('Arial',24,'bold'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=20,
            )
top2_tx.place(x=80,y=42,width=435,height=40)

top3_tx=Label(window,
            text='Результат виконання',
            bg='#999999',
            # bg='green',
            fg='black',
            font=('Arial',24,'bold'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=20,
            )
top3_tx.place(x=170,y=245,width=260,height=40)

top4_tx=Label(window,
            text='- фон',
            bg='#00ffff',
            # bg='green',
            fg='#0066cc',
            font=('Arial',20,'italic'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=2,
            )
top4_tx.place(x=15,y=300,width=50,height=30)

top5_tx=Label(window,
            text='- фон',
            # bg='#999999',
            bg='green',
            fg='black',
            font=('Arial',20,'italic'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=2,
            )
top5_tx.place(x=15,y=300,width=50,height=30)

top6_tx=Label(window,
            text='- фон',
            # bg='#999999',
            bg='green',
            fg='black',
            font=('Arial',20,'italic'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=2,
            )
top6_tx.place(x=15,y=300,width=50,height=30)

top7_tx=Label(window,
            text='- фон',
            # bg='#999999',
            bg='green',
            fg='black',
            font=('Arial',20,'italic'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=2,
            )
top7_tx.place(x=15,y=300,width=50,height=30)

top8_tx=Label(window,
            text='- фон',
            # bg='#999999',
            bg='green',
            fg='black',
            font=('Arial',20,'italic'),
            # relief=RAISED,
            # bd=2,
            # width=20,
            # height=4,
            justify=CENTER,
            # anchor=N,
            # padx=50,
            # pady=2,
            )
top8_tx.place(x=15,y=300,width=50,height=30)

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
