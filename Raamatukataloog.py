import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Ühenduse loomine andmebaasiga
conn = sqlite3.connect('raamatukogu.sql')
c = conn.cursor()

# Tabelite loomine
c.execute('''
    CREATE TABLE IF NOT EXISTS Autorid (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor_nimi TEXT NOT NULL,
        sunnikuupaev DATE NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS Zanrid (
        Zanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Zanri_nimi TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS Raamatud (
        raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pealkiri TEXT NOT NULL,
        valjaandmise_kuupaev DATE NOT NULL,
        autor_id INTEGER,
        Zanr_id INTEGER,
        FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
        FOREIGN KEY(Zanr_id) REFERENCES Zanrid(Zanr_id)
    )
''')

# Andmete sisestamine tabelitesse
c.execute("INSERT INTO Autorid (autor_nimi, sunnikuupaev) VALUES ('Bret Easton Ellis', '1964-02-03')")
c.execute("INSERT INTO Autorid (autor_nimi, sunnikuupaev) VALUES ('George Orwell', '1950-06-25')")
c.execute("INSERT INTO Zanrid (Zanri_nimi) VALUES ('Dark Comedy')")
c.execute("INSERT INTO Zanrid (Zanri_nimi) VALUES ('Political fiction')")
c.execute("INSERT INTO Raamatud (pealkiri, valjaandmise_kuupaev, autor_id, Zanr_id) VALUES ('American Psycho', '1991-02-03', 1, 1)")
c.execute("INSERT INTO Raamatud (pealkiri, valjaandmise_kuupaev, autor_id, Zanr_id) VALUES ('Nineteen Eighty-Four', '1949-02-07', 2, 2)")
c.execute("INSERT INTO Raamatud (pealkiri, valjaandmise_kuupaev, autor_id, Zanr_id) VALUES ('Animal Farm', '1945-08-17', 2, 2)")


root = tk.Tk()
text = tk.Text(root)
text.pack()

def lisa_autor():
   nimi = simpledialog.askstring("Input", "Sisestage autori nimi:")
   sunnipaev = simpledialog.askstring("Input", "Sisestage autori sunnipaev (YYYY-MM-DD):")
   if nimi is None or sunnipaev is None or nimi.strip() == "" or sunnipaev.strip() == "":
        messagebox.showinfo("Info", "Tegevus tühistatud või sisend puudub")
   else:
       c.execute("INSERT INTO Autorid (autor_nimi, sunnikuupaev) VALUES (?, ?)", (nimi, sunnipaev))
       messagebox.showinfo("Info", "Autor lisatud")
       conn.commit()


def lisa_Zanr():
    nimi = simpledialog.askstring("Input", "Sisestage Zanri nimi:")
    if nimi is None or nimi.strip() == "":
        messagebox.showinfo("Info", "Tegevus tühistatud või sisend puudub")
    else:
        c.execute("INSERT INTO Zanrid (Zanri_nimi) VALUES (?)", (nimi,))
        conn.commit()

def lisa_raamat():
    pealkiri = simpledialog.askstring("Input", "Sisestage raamatu pealkiri:")
    valjaandmise_kuupaev = simpledialog.askstring("Input", "Sisestage raamatu valjaandmise kuupaev (YYYY-MM-DD):")
    autor_id = simpledialog.askinteger("Input", "Sisestage raamatu autori ID:")
    Zanr_id = simpledialog.askinteger("Input", "Sisestage raamatu Zanri ID:")
    c.execute("INSERT INTO Raamatud (pealkiri, valjaandmise_kuupaev, autor_id, Zanr_id) VALUES (?, ?, ?, ?)", (pealkiri, valjaandmise_kuupaev, autor_id, Zanr_id))
    conn.commit()

def muuda_autorit():
    id = simpledialog.askinteger("Input", "Sisestage autori ID, keda soovite muuta:")
    nimi = simpledialog.askstring("Input", "Sisestage uus autori nimi:")
    sunnipaev = simpledialog.askstring("Input", "Sisestage uus autori sunnipaev (YYYY-MM-DD):")
    c.execute("UPDATE Autorid SET autor_nimi = ?, sunnikuupaev = ? WHERE autor_id = ?", (nimi, sunnipaev, id))
    conn.commit()

def muuda_Zanrit():
    id = simpledialog.askinteger("Input", "Sisestage Zanri ID, mida soovite muuta:")
    nimi = simpledialog.askstring("Input", "Sisestage uus Zanri nimi:")
    c.execute("UPDATE Zanrid SET Zanri_nimi = ? WHERE Zanr_id = ?", (nimi, id))
    conn.commit()

def muuda_raamatut():
    id = simpledialog.askinteger("Input", "Sisestage raamatu ID, mida soovite muuta:")
    pealkiri = simpledialog.askstring("Input", "Sisestage uus raamatu pealkiri:")
    valjaandmise_kuupaev = simpledialog.askstring("Input", "Sisestage uus raamatu valjaandmise kuupaev (YYYY-MM-DD):")
    autor_id = simpledialog.askinteger("Input", "Sisestage uus raamatu autori ID:")
    Zanr_id = simpledialog.askinteger("Input", "Sisestage uus raamatu Zanri ID:")
    c.execute("UPDATE Raamatud SET pealkiri = ?, valjaandmise_kuupaev = ?, autor_id = ?, Zanr_id = ? WHERE raamat_id = ?", (pealkiri, valjaandmise_kuupaev, autor_id, Zanr_id, id))
    conn.commit()

def kustuta_autori_raamatud():
    autor_id = simpledialog.askinteger("Input", "Sisestage autori ID, kelle raamatuid soovite kustutada:")
    c.execute("DELETE FROM Raamatud WHERE autor_id = ?", (autor_id,))
    conn.commit()

def kustuta_Zanri_raamatud():
    Zanr_id = simpledialog.askinteger("Input", "Sisestage Zanri ID, mille raamatuid soovite kustutada:")
    c.execute("DELETE FROM Raamatud WHERE Zanr_id = ?", (Zanr_id,))
    conn.commit()

def kustuta_ja_taasta_tabel(selected_table):
    # Kustuta tabel
    c.execute(f'DROP TABLE IF EXISTS {selected_table}')
    messagebox.showinfo("Success", f"Table {selected_table} has been deleted successfully")




def näita_Zanrid():
    text.delete("1.0", "end")
    c.execute("SELECT * FROM Zanrid")
    rows = c.fetchall()
    text.insert(tk.END, 'ID\tZanri nimi\n')  # Add column labels
    for row in rows:
        text.insert(tk.END, '{}\t{}\n'.format(row[0], row[1]))  # Format each row as a tab-separated string
        text.insert(tk.END, '-'*30 + '\n')  # Add a separation line after each row


def näita_raamatud():
    text.delete("1.0", "end")
    c.execute('''
    SELECT Raamatud.raamat_id, Raamatud.pealkiri, Raamatud.valjaandmise_kuupaev, Autorid.autor_nimi, Zanrid.Zanri_nimi
    FROM Raamatud
    INNER JOIN Autorid ON Raamatud.autor_id = Autorid.autor_id
    INNER JOIN Zanrid ON Raamatud.Zanr_id = Zanrid.Zanr_id
''')
    rows = c.fetchall()
    text.insert(tk.END, 'ID | Pealkiri | Väljaandmise kuupäev | Autor | Zanr\n')  # Add column labels
    for row in rows:
        text.insert(tk.END, '{} | {} | {} | {} | {}\n'.format(row[0], row[1], row[2], row[3], row[4]))  # Format each row as a tab-separated string
        text.insert(tk.END, '-'*30 + '\n')  # Add a separator line

def näita_autorid():
    text.delete("1.0", "end")
    c.execute("SELECT * FROM Autorid")
    rows = c.fetchall()
    text.insert(tk.END, 'ID | Autori nimi | Sunnikuupaev\n')  # Add column labels
    for row in rows:
        text.insert(tk.END, '{} | {} | {}\n'.format(row[0], row[1], row[2]))  # Format each row as a tab-separated string
        text.insert(tk.END, '-'*30 + '\n')  # Add a separator line



def create_dialog():
    var = tk.StringVar(root)
    var.set("Select a table") # initial value

    option_list = ["Autorid", "Zanrid", "Raamatud"]
    opt = tk.OptionMenu(root, var, *option_list)
    opt.pack()

    def on_button_delete():
        table_name = var.get()
        if table_name != "Select a table":
            kustuta_ja_taasta_tabel(table_name)

    def on_button_restore():
        table_name = var.get()
        if table_name == "Autorid":
            c.execute('''
            CREATE TABLE IF NOT EXISTS Autorid (
            autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            autor_nimi TEXT NOT NULL,
            sunnikuupaev DATE NOT NULL
    )
''')


    button_delete = tk.Button(root, text="DELETE", command=on_button_delete)
    button_delete.pack()

    button_restore = tk.Button(root, text="RESTORE", command=on_button_restore)
    button_restore.pack()



left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT)

tk.Button(left_frame, text="Lisa autor", command=lisa_autor).pack()
tk.Button(left_frame, text="Lisa Zanr", command=lisa_Zanr).pack()
tk.Button(left_frame, text="Lisa raamat", command=lisa_raamat).pack()
tk.Button(left_frame, text="Muuda autorit", command=muuda_autorit).pack()
tk.Button(left_frame, text="Muuda Zanrit", command=muuda_Zanrit).pack()
tk.Button(left_frame, text="Muuda raamatut", command=muuda_raamatut).pack()

tk.Button(right_frame, text="Kustuta autori raamatud", command=kustuta_autori_raamatud).pack()
tk.Button(right_frame, text="Kustuta Zanri raamatud", command=kustuta_Zanri_raamatud).pack()
tk.Button(right_frame, text="Kustuta ja taasta tabel", command=create_dialog).pack()
tk.Button(right_frame, text="Näita Zanrid", command=näita_Zanrid).pack()
tk.Button(right_frame, text="Näita raamatud", command=näita_raamatud).pack()
tk.Button(right_frame, text="Näita autorid", command=näita_autorid).pack()


root.mainloop()

conn.close()
