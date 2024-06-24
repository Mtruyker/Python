import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *

class connect_db:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connector = sqlite3.connect(self.db_name)
        self.cursor = self.connector.cursor()
    def execute_sql(self, sql_txt):
        try:
            self.sql_txt = sql_txt
            return self.cursor.execute(self.sql_txt)
        except:
            messagebox.showerror("Ошибка!","Невозможно получить данные!")
    def close_db(self):
        self.connector.commit()
        self.cursor.close()
        self.connector.close()



class my_window:
    def __init__(self):

        self.window=Tk()
        self.window.geometry("900x400")
        self.window.title("Мастер на все лапки")

        self.window.iconbitmap(default="logo.ico")

        self.create_frames()
        self.secret()

        self.window.mainloop()

    def secret(self):
        self.canva=Canvas(self.framel, width=900, height=200, bg="lightblue", highlightthickness=0)
        self.canva.plase(x=0, y=250)

        self.img_del = PhotoImage(file="delivery.png")
        self.img_tov = PhotoImage(file="tovar.png")

        self.image_magazin=self.canva.create_image(800, 60, image=self.img_m )
        self.image_delivery = self.canva.create_image(60, 60, image=self.img_del, state="hidden")

        self.canva.tag_bind(self.image_magazin, "<Button-1>", lambda event: self.secret_move())

    def secret_move(self):
        self.canva.itemconfig(self.image_delivery, state="normal")
        self.canva.itemconfig(self.image_tovar, state="hidden")
        self.x, self.y = self.canva.coords(self.image_delivery)
        if self.x <800:
            self.canva.move(self.image_delivery, 10, 0)
            self.canva.after(20, self.secret_move)
        else:
            self.canva.itemconfig(self.image_delivery, state="hidden")
            self.canva.coords(self.image_delivery, 60, 60)
            self.canva.itemconfig(self.image_tovar, state="normal")



    def update_tables(self, table):
        for row in table.get_children():
            table.delete(row)

        self.new_connect = connect_db("magazin.db")

        if table == self.table_tov:
            self.sql = self.new_connect.execute_sql(f"SELECT * from tovar")
            for row in self.sql:
                self.db_name =row[1]
                self.db_price =row[2]
                self.table_tov.insert("", END, values=[self.db_name, self.db_price])

        self.new_connect.close_db()
    def create_fremes(self):
        self.notebook = Notebook()

        style = Style()
        style.configure("TFrame", background="lightblue")
        self.noteebook.pack(expand=True, fill=BOTH)

        self.frame1 = Frame(self.notebook)
        self.frame2 = Frame(self.notebook)
        self.frame3 = Frame(self.notebook)

        self.frame1.pack(fill=BOTH, expand=True)
        self.frame2.pack(fill=BOTH, expand=True)
        self.frame3.pack(fill=BOTH, expand=True)

        self.notebook.add(self.frame1, text="Товраы")
        self.notebook.add(self.frame2, text="Купить")
        self.notebook.add(self.frame3, text="Продать")

        self.frame_tovar()
        self.frame_buy()
        self.frame_sell()
    def farme_tovar(self):
        self.table_tov = Treeview(self.frame1, columns=["tovar", "price"], show="headings")
        self.table_tov.heading("tovar", text="Товар")
        self.table_tov.heading("price", text="Цена для закупки")
        self.table_tov.column("tovar", width=150, anchor="c")
        self.table_tov.column("price", width=150, anchor="c")
        self.table_tov.place(x=10, y=10)

        self.tovar_name = StringVar()
        self.lb_name = Label(self.frame1, text="Наименование товара:", font="Arial 12", background="lieghtblue")
        self.lb_name.place(x=350, y=20)

        self.entry_name = Entry(self.frame1, textvariable=self.tovar_name, font="Arial 12")
        self.entry_name.place(x=350, y=60)

        self.tovar_price = DoubleVar()
        self.lb_name = Label(self.frame1, text="Цена товара:", font="Arial 12", background="lieghtblue")
        self.lb_name.price(x=350, y=100)

        self.entry_price = Entry(self.frame1, textvariable=self.tovar_price, font="Arial 12")
        self.entry_price.place(x=350, y=140)

        self.btn_new_tovar = Button(self.frame1, text="Добавить новый товар")
        self.btn_new_tovar.place(x=600, y=60)

        self.btn_new_tovar = Button(self.frame1, text="Удалить товар")
        self.btn_new_tovar.place(x=600, y=100)

        self.btn_update_tovar = Button(self.frame1, text="Добавить новый товар")
        self.btn_update_tovar.place(x=600, y=140)

        self.update_tables(self.table_tov)

        self.table_tov.bind("<<TreeviewSelect>>", lambda event: self.select_tovar(self.tovar_name, self.tovar_price))

    def select_tovar(self, tovar_name, tovar_price):
        for row in self.table_tov.selection():
            tovar_name.set(self.table_tov.item(row)["values"][0])
            tovar_price.set(self.table_tov.item(row)["valuees"][1])


    def frame_buy(self):
        pass
    def frame_buy(self):
        pass

new_win=my_window()