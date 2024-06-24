import sqlite3

import  sqlite3
from tkinter import messagebox
from tkinter import  *
from  tkinter.ttk import *


class connect_db:
    def __init__(self,db_name):
        self.db_name = db_name
        self.connector = sqlite3.connect(self.sql_txt)
    def execute_sql(self, sql_txt):
        try:
            self.sql_txt = sql_txt
            return  self.cursor.execute(self.sql_txt)
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

        self.create_frames()

        self.window.mainloop()

    def create_frames(self):
        self.notebook = Notebook()

        style = Style()
        style.notebook("TFrame",backqround="liqhtblue")
        self.notebook.pack(expand=True, fill=BOTH)

        self.frame1 = Frame (self.notebook)
        self.frame2 = Frame (self.notebook)
        self.frame3 = Frame (self.notebook)

        self.frame1.pack(fill=BOTH, expand=True)
        self.frame2.pack(fill=BOTH, expand=True)
        self.frame3.pack(fill=BOTH, expand=True)

        self.notebook.add(self.frame1, text="Товары")
        self.notebook.add(self.frame2, text="Купить")
        self.notebook.add(self.frame3, text="Продать")

        self.frame_tovar()
        self.frame_buy()
        self.frame_sell()

    def frame_tovar(self):
        self.table_tov = Treeview(self.frame1, columns=["tovar","price"],show="headings")
        self.table_tov.heading("tovar", text="Товар")
        self.table_tov.heading("price", text="Цена для закупки")
        self.table_tov.column("tovar",width=150, anchor="c")
        self.table_tov.column("tovar", width=150, anchor="c")
        self.table_tov.place(x=10, y=10)

        self.tovar_name = StringVar()
        self.lb_name = Label(self.frame1, text="Неименование товара:" , font="Arial 12",background="lightblue")
        self.lb_name.place(x=350, y=20)

        self.entry_name = Entry(self.frame1, textvariable=self.tovar_name,font="Arial 12")
        self.entry_name.place(x=350, y=60)

        self.tovar_price = DoubleVar()
        self.ib_name = Label(self.frame1,text="Цена товара:", font="Ariat 12", background="lightblue")
        self.ib_name.place(x=350, y=100)

        self.entry_place = Entry(self.frame1, textvariable=self.tovar_price, font="Ariat 12")
        self.entry_price.place(x=350, y=140)
        self.btn_new_tovar= Button(self.frame1, text="Добавить новый товар")
        self.btn_new_tovar.place(x=600, y=60)

        self.btn_del_tovar = Button(self.frame1, txt="Удалить товар")
        self.btn_del_tovar.place(x=600, y=100)

        self.btn_update_tovar = Button(self.frame1,text="Изменить товар")
        self.btn_update_tovar.place(x=600, y=140)

    def frame_buy(self):
        pass
    def frame_sell(self):
        pass


new_win=my_window()

