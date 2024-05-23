from tkinter import*
from tkinter import messagebox
root = Tk()

# головне вікно
root.title('Вхід/Реєстрація')
root.geometry('600x500')
root.minsize(500,400)
root.config(bg='#b3b3b3')

# незмінний текст
top1_tx=Label(root,
            text='Вхід',
            # bg='#b3b3b3',
            bg='red',
            fg='black',
            font=('Arial',24,'bold'),
            justify=CENTER,
            )
top1_tx.place(x=80,y=42,width=100,height=40)

top2_tx=Label(root,
            text='Логін:',
            # bg='#b3b3b3',
            bg='red',
            fg='black',
            font=('Arial',24,'bold'),
            justify=CENTER,
            )
top2_tx.place(x=170,y=245,width=100,height=40)

top3_tx=Label(root,
            text='Пароль:',
            # bg='#b3b3b3',
            bg='red',
            fg='black',
            font=('Arial',24,'bold'),
            justify=CENTER,
            )
top3_tx.place(x=15,y=300,width=100,height=40)

# top5_tx=Label(root,
#             text='- текст',
#             bg='#b3b3b3',
#             fg='black',
#             font=('Arial',20,'italic'),
#             justify=LEFT,
#             )
# top5_tx.place(x=15,y=340,width=90,height=30)

# top6_tx=Label(root,
#             text='- заливка',
#             bg='#b3b3b3',
#             fg='black',
#             font=('Arial',20,'italic'),
#             justify=LEFT,
#             )
# top6_tx.place(x=15,y=380,width=100,height=30)

# top7_tx=Label(root,
#             text='- обраний стиль',
#             bg='#b3b3b3',
#             fg='black',
#             font=('Arial',20,'italic'),
#             justify=LEFT,
#             )
# top7_tx.place(x=15,y=420,width=165,height=30)

# вхідні дані
et_1=Entry(
    
)

# кнопки
# kn_1=Button(root,
#             text='Зареєструватися',
#             font=('Arial',20,'bold'),
#             borderwidth=1,
#             # command=lambda:pushButton(0),
#             )
# kn_1.place(x=1,y=2,width=598,height=40)

kn_2=Button(root,
            text='Увійти',
            font=('Arial',24),
            borderwidth=1,
            # command=lambda:pushButton(1),
            command=lambda:login(),
            )
kn_2.place(x=30,y=100,width=250,height=50)

kn_3=Button(root,
            text='Зареєструватися',
            font=('Arial',24),
            borderwidth=1,
            # command=lambda:pushButton(2),
            )
kn_3.place(x=30,y=170,width=250,height=50)

# kn_4=Button(root,
#             text='Стиль "Море"',
#             font=('Arial',24),
#             borderwidth=1,
#             command=lambda:pushButton(3),
#             )
# kn_4.place(x=315,y=100,width=250,height=50)

# kn_5=Button(root,
#             text='Стиль "Бузковий"',
#             font=('Arial',24),
#             borderwidth=1,
#             command=lambda:pushButton(4),
#             )
# kn_5.place(x=315,y=170,width=250,height=50)

# # функція натискання кнопки
# def pushButton (buttonNumber):
#     print('Button #', buttonNumber),
#     bgColor = '#000000', 
#     fgColor = '#ffffff'
#     if buttonNumber == 0:
#         bgColor = '#b3b3b3',
#         fgColor = 'black',
#         root.config(bg='#b3b3b3')
#         messagebox.showinfo('Стилі','Стиль змінено на "Стадартні налаштування"')
#     elif buttonNumber == 1:
#         bgColor = '#000000', 
#         fgColor = '#ffffff'
#         root.config(bg='#000000')
#         messagebox.showinfo('Стилі','Стиль змінено на "Ніч"')
#     elif buttonNumber == 2:
#         bgColor = '#cc9900',
#         fgColor = '#990000'
#         root['background']='#009999'
#         messagebox.showinfo('Стилі','Стиль змінено "Мілітарі"')
#     elif buttonNumber == 3:
#         bgColor = '#990099', 
#         fgColor = '#33cc33'
#         root['background']='#ff00ff'
#         messagebox.showinfo('Стилі','Стиль змінено на "Море"')
#     elif buttonNumber == 4:
#         bgColor = '#00ffff', 
#         fgColor = '#0066cc'
#         root['background']='#99ccff'
#         messagebox.showinfo('Стилі','Стиль змінено на "Бузковий"')
#     else : print('Error'),messagebox.showerror('Стилі','Такого стилю немає')
#     top2_tx.config(
#                 bg=bgColor,
#                 fg=fgColor,
#                 ),
#     top3_tx.config(
#                 bg=bgColor,
#                 fg=fgColor,
#                 )
#     top4_tx.config(
#                 bg=bgColor,
#                 fg=fgColor,
#                 )
#     top5_tx.config(
#                 bg=bgColor,
#                 fg=fgColor,
#                 )
#     top6_tx.config(
#                 bg=bgColor,
#                 fg=fgColor,
#                 )
#     top7_tx.config(
#                 bg=bgColor,
#                 fg=fgColor,
#                 )

users = {
    'admin': 'password',
    'user': '1234'
    }

def login():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    if username in users and users[username] == password:
        print("Вітаю! Ви успішно увійшли!")
    else:
        print("Помилка: Неправильне ім'я користувача або пароль")

login()


root.mainloop()

root2 = Tk()
root2.title('Реєстрація')
root2.geometry('600x500')
root2.minsize(500,400)
root2.config(bg='#b3b3b3')
root2.mainloop()