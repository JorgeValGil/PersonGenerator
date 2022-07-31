import tkinter as tk
from faker import Faker


class Ventana:
    def __init__(self, top=None):
        width = 400
        height = 260
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        top.title("PersonGenerator")
        self.top = top

        self.title = tk.Label(self.top)
        self.title.place(x=10, y=10, height=21, width=380)
        self.title.configure(text='''PersonGenerator''')
        self.title.configure(font=("TkDefaultFont", 16))

        self.label_name = tk.Label(self.top)
        self.label_name.place(x=10, y=50, height=21, width=60)
        self.label_name.configure(text='''Nombre:''')

        self.label_address = tk.Label(self.top)
        self.label_address.place(x=10, y=90, height=21, width=60)
        self.label_address.configure(text='''Dirección:''')

        self.label_email = tk.Label(self.top)
        self.label_email.place(x=10, y=130, height=21, width=110)
        self.label_email.configure(text='''Correo Electrónico:''')

        self.label_phone_number = tk.Label(self.top)
        self.label_phone_number.place(x=10, y=170, height=21, width=60)
        self.label_phone_number.configure(text='''Teléfono:''')

        self.name_text = tk.StringVar()
        self.name = tk.Entry(self.top, textvariable=self.name_text)
        self.name.place(x=70, y=50, height=20, width=320)
        self.name.configure(insertbackground="black")

        self.address_text = tk.StringVar()
        self.address = tk.Entry(self.top, textvariable=self.address_text)
        self.address.place(x=70, y=90, height=20, width=320)
        self.address.configure(insertbackground="black")

        self.email_text = tk.StringVar()
        self.email = tk.Entry(self.top, textvariable=self.email_text)
        self.email.place(x=120, y=130, height=20, width=270)
        self.email.configure(insertbackground="black")

        self.phone_number_text = tk.StringVar()
        self.phone_number = tk.Entry(self.top, textvariable=self.phone_number_text)
        self.phone_number.place(x=70, y=170, height=20, width=320)
        self.phone_number.configure(insertbackground="black")

        self.regenerate = tk.Button(self.top, command=self.fakeperson)
        self.regenerate.place(x=170, y=210, height=24, width=60)
        self.regenerate.configure(text='''Regenerar''')

        self.fakeperson()

    def fakeperson(self):
        fake = Faker(locale='es-ES')
        self.name_text.set(fake.unique.name())
        self.address_text.set(fake.address())
        self.email_text.set(fake.email())
        self.phone_number_text.set(fake.phone_number().replace(' ', ''))


if __name__ == '__main__':
    root = tk.Tk()
    root.iconbitmap('icono.ico')
    app = Ventana(root)
    root.mainloop()
