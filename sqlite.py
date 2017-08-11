import sqlite3
from sqlite3 import Error
from tkinter import Label, Frame, Button, BOTH
import tkinter.messagebox as mb
import os, sys

# queries
# sve exceptione treba staviti kao modal

program_data = {
    "name": "Google Chrome", \
    "version": "1.2", \
    "install_cmd": "sudo apt-get clean", \
    "update_cmd": "sudo apt-get clean", \
    "remove_cmd": "sudo apt-get clean", \
    "image": "imgs/chrome.jpg",\
}

# SQL FOR CREATING TABLES
#************************************************************************************************************************************************

#create tabel for storing info about programs
def create_table(db_file):
     try:
        conn = sqlite3.connect(db_file)

        query = "CREATE TABLE IF NOT EXISTS programs(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, version TEXT, install_cmd TEXT, update_cmd TEXT, remove_cmd TEXT, image TEXT,categories INTEGER, FOREIGN KEY (categories) REFERENCES categories(id));"
        cur = conn.cursor()
        cur.execute(query)

        query2 = "CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, image TEXT);"
        cur2 = conn.cursor()
        cur2.execute(query2)

     except Error as e:
        print("exception in create table",e)

     finally:
        conn.close()



# SQL FOR TABLE PROGRAM
#************************************************************************************************************************************************

#get programs
def get_programs_data(db_file, category):

    if category is None:
        query = "SELECT * FROM PROGRAMS limit 20"
    else:
        query = "SELECT * FROM PROGRAMS where categories =(%s)" %(category)

    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        # print ("Table -programs-: %s" % data )
        return data

    except Error as e:
        print("exception in get_programs_data", e)

    finally:
        conn.close()

# insert into table programs            ovo radi samo treba dodati u  koju kategoriju da doda
def insert_into_programs(conn, **program_data):

    columns = ', '.join(program_data.keys())
    placeholders = ':'+', :'.join(program_data.keys())
    query = 'INSERT INTO programs (%s) VALUES (%s)' % (columns, placeholders)

    # print (query, 'query')
    cur = conn.cursor()
    cur.execute(query, program_data)
    conn.commit()




# SQL FOR TABLE CATEGORIES
#************************************************************************************************************************************************

# return the list of all categories avaiable
def get_categories(db_file):
    try:
        conn = sqlite3.connect(db_file)

        query = "SELECT * FROM categories order by category;"
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        # print ("Categories : %s" % data )
        return data
    except Error as e:
        print("exception in get_categories", e)

    finally:
        conn.close()

# insert new category
def insert_into_categories(db_file, category):

    structure = {"category": category, "image": ""}

    try:
        conn = sqlite3.connect(db_file)

        columns = ', '.join(structure.keys())
        placeholders = ':'+', :'.join(structure.keys())
        query = 'INSERT INTO categories (%s) VALUES (%s);' % (columns, placeholders)

        cur = conn.cursor()
        cur.execute(query, structure)
        conn.commit()
        resp = True

    except sqlite3.Error as e:
        resp = e

    finally:
        conn.close()
        return resp

# update category
def update_category_name( db_file, item, lbl):

    try:
        conn = sqlite3.connect(db_file)

        query = "UPDATE categories SET category=? WHERE id=?;"
        cur = conn.cursor()
        cur.execute(query, (lbl.text(), item))
        conn.commit()
        resp = True

    except Error as e:
        resp = e

    finally:
        conn.close()
        return resp

# update image
def update_category(db_file, id, img):
    try:
        conn = sqlite3.connect(db_file)

        query = "UPDATE categories SET image=? WHERE id=?;"
        cur = conn.cursor()
        cur.execute(query, (img, id))
        conn.commit()
        ans = True

    except Error as e:
        ans = e

    finally:
        conn.close()
        return ans

# remove category
def remove_category(db_file, id):
    try:

        conn = sqlite3.connect(db_file)

        query = "DELETE from categories WHERE id=?;"
        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()

        resp = True

    except Error as e:
        resp = e

    finally:
        conn.close()
        return resp