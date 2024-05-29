from tkinter import *
from tkinter import messagebox

# головне вікно
root = Tk()
root.title('Вхід/Реєстрація')
root.geometry('600x400')
root.config(bg='#b3b3b3')

# незмінний текст
top0_tx=Label(root,
            text='Вхід',
            bg='#b3b3b3',
            fg='black',
            font=('Arial',24,'bold'),
            justify=CENTER,
            )
top0_tx.place(x=250,y=42,width=100,height=40)

top1_tx=Label(root,
            text='Логін:',
            bg='#b3b3b3',
            fg='black',
            font=('Arial',24,'bold'),
            justify=CENTER,
            )
top1_tx.place(x=70,y=100,width=100,height=40)

top2_tx=Label(root,
            text='Пароль:',
            bg='#b3b3b3',
            fg='black',
            font=('Arial',24,'bold'),
            justify=CENTER,
            )
top2_tx.place(x=70,y=170,width=100,height=40)

# вхідні дані
ent_1=Entry(root,
           bg='#808080',
           fg='black',
           font=('Arial',20,'italic'),
           justify=LEFT,
           )
ent_1.place(x=180,y=100,width=350,height=40)

ent_2=Entry(root,
           bg='#808080',
           fg='black',
           font=('Arial',20,'italic'),
           justify=LEFT,
           show='•',
           )
ent_2.place(x=180,y=170,width=350,height=40)

# кнопки
kn_1=Button(root,
            text='Увійти',
            font=('Arial',24),
            borderwidth=1,
            command=lambda:login(),
            )
kn_1.place(x=310,y=250,width=250,height=50)

kn_2=Button(root,
            text='Зареєструватися',
            font=('Arial',24),
            borderwidth=1,
            command=lambda:singup(),
            )
kn_2.place(x=35,y=250,width=250,height=50)

users = {
    'admin': 'password',
    'user': '1234',
    '1':'1'
        }
    
def login():
    username = ent_1.get()
    password = ent_2.get()
    
    if username in users and users[username] == password:
        print("Вітаю! Ви успішно увійшли!")
        messagebox.showinfo('Вхід','Вхід виконано')
        print(users)
        ent_1.delete(0,END)
        ent_2.delete(0,END)
        root.destroy()
        
        # вікно другого рівня вкладеності
        window = Tk()
        window.title('Головна')
        window.geometry('1200x800')
        window.config(bg='#b3b3b3')
        window.minsize(1200,800)

        # незмінний текст
        top1_tx=Label(window,
                    text='Говерла – найвища гірська вершина в Україні. \nЗаввишки вона — 2061 м над рівнем моря. \nРозташована в Карпатах, у гірському масиві \nЧорногора, на межі Івано-Франківської та \nЗакарпатської областей. Назва «Говерла» \nпоходить від угорського «hóvár», \nщо означає «снігова гора». ',
                    bg='#b3b3b3',
                    fg='black',
                    font=('Comic Sans MS',18,'bold'),
                    relief=GROOVE,
                    bd=1,
                    width=18,
                    height=4,
                    justify=CENTER,
                    )
        top1_tx.place(x=1,y=400,width=600,height=400)

        top2_tx=Label(window,
                    text='Справді, вершина гори вкрита снігом \nмайже завжди;  сніговий покрив тане в \nлипні, й то не завжди. Говерлою гора \nстала через …помилку. Спочатку гуцули \nназивали її «Говирла», але коли \nавстрійські картографи складали мапу \nмісцевості, котрийся з них записав \n«Говерла». Так і лишилося…',
                    bg='#b3b3b3',
                    fg='black',
                    font=('Comic Sans MS',18,'bold'),
                    relief=GROOVE,
                    bd=1,
                    width=18,
                    height=4,
                    justify=CENTER,
                    )
        top2_tx.place(x=600,y=400,width=600,height=400)

        # фото
        canva=Canvas(window,
                    width=1200,
                    height=400,
                    )
        canva.pack()
        img=PhotoImage(file='hoverla.png')
        canva.create_image(0,0,anchor=NW,image=img)
        
        window.mainloop()
        
    else:
        print("Помилка: Неправильне ім'я користувача або пароль")
        print(users)
        ent_1.delete(0,END)
        ent_2.delete(0,END)
        messagebox.showerror("Помилка","Неправильне ім'я користувача або пароль")

def singup():
    singup = Tk()
    singup.title('Реєстрація')
    singup.geometry('600x400')
    singup.config(bg='#b3b3b3')
    
    # незмінний текст
    top0_tx=Label(singup,
                text='Реєстрація',
                bg='#b3b3b3',
                fg='black',
                font=('Arial',24,'bold'),
                justify=CENTER,
                )
    top0_tx.place(x=250,y=42,width=150,height=40)

    top1_tx=Label(singup,
                text='Логін:',
                bg='#b3b3b3',
                fg='black',
                font=('Arial',24,'bold'),
                justify=CENTER,
                )
    top1_tx.place(x=70,y=100,width=100,height=40)

    top2_tx=Label(singup,
                text='Пароль:',
                bg='#b3b3b3',
                fg='black',
                font=('Arial',24,'bold'),
                justify=CENTER,
                )
    top2_tx.place(x=70,y=170,width=100,height=40)

    # дані реєстрації
    ent_3=Entry(singup,
            bg='#808080',
            fg='black',
            font=('Arial',20,'italic'),
            justify=LEFT,
            )
    ent_3.place(x=180,y=100,width=350,height=40)

    ent_4=Entry(singup,
            bg='#808080',
            fg='black',
            font=('Arial',20,'italic'),
            justify=LEFT,
            )
    ent_4.place(x=180,y=170,width=350,height=40)

    # кнопки реєстрації
    kn_1=Button(singup,
                text='Готово',
                font=('Arial',24),
                borderwidth=1,
                command=lambda:registerRedy(),
                )
    kn_1.place(x=310,y=250,width=250,height=50)

    kn_2=Button(singup,
                text='Скасувати',
                font=('Arial',24),
                borderwidth=1,
                command=lambda:singup.destroy(),
                )
    kn_2.place(x=40,y=250,width=250,height=50)
    
    def registerRedy():
        regusername = ent_3.get()
        regpassword = ent_4.get()
        
        if regusername=='' or regpassword=='':
            print('Помилка: не всі данні введено')
            messagebox.showerror("Помилка","Не всі данні введено")
        else:
            print('Реєстрація успішна')
            messagebox.showinfo('Реєстрація','Реєстрія успішна')
            users[ent_3.get()] = ent_4.get()
            login
            singup.destroy()

    singup.mainloop()

root.mainloop()

