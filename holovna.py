from tkinter import*
root = Tk()

# назва
root.title('Cтилі')

# ромір, відступ
root.geometry('600x500')

# блок розмірів
# root.minsize(500,400)
# root.resizable(width=true, height=true)

# колір
root.config(bg='#999999')

# прозорість
# root.wm_attributes('-alpha',0.7)

#         Логотип
# photo=PhotoImage(file='logo.ong')
# root.iconbitmap('logo.ico')
#         або
# root.iconbitmap('logo.ico')

# незмінний текст
top_tx=Label(root,
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

top2_tx=Label(root,
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

top3_tx=Label(root,
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

top4_tx=Label(root,
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

top5_tx=Label(root,
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

top6_tx=Label(root,
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

top7_tx=Label(root,
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

top8_tx=Label(root,
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

root.mainloop()


