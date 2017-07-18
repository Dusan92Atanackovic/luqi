__author__ = 'atana'

import os, sys
lib_path = os.path.abspath(os.path.join(''))
sys.path.append(lib_path)

from tkinter import *
from PIL import ImageTk, Image
import subprocess, os, sys, math, codecs
import tkinter.filedialog as fd
import gradient

hlt = 0        # highlightickness
hlb = 'black'  # highlightbackgorund
lst = []       # list of objects , needded for destroying  (obj.destroy())
kwargs1 = {'wd': 14, 'ht': 2,  'bg': 'white', 'side': 'top', 'pady': 2,  'padx': 5, 'fill': 'x'} # for CustomButton
kwargs2 = {'hlb': hlb, 'hlt': 0, 'side': 'left', 'padx': 0, 'pady': 0, 'fill': BOTH, 'exp': 1, 'tag': 'kat'}
kwargs3 = {'hlb': hlb, 'hlt': 0, 'side': 'left', 'padx': 0, 'pady': 0, 'fill': BOTH, 'exp': 1, 'tag': 'programs'}

obj_field = None
glavni = None  # just initialisation
srch = None    # just initialisation
can = None     # just initialisation
pan = None     # just initialisation
w2 = None      # just initialisation
of = None      # just initialisation
lb = []        # list of CustomButtons (for categories)



#1
def main():
    root = Tk()
    gui(root)
    root.mainloop()

#2
def gui(root):

    global w2, can, glavni , obj_field, pan, of
                                    # create global varibles
    w, h = __get_resolution(root)                                             # get resolution
    root.geometry("%dx%d" % (w, h))                                           # set w and h of root
    root.minsize(800, 400)                                                    # set min size of root
    root.protocol("WM_DELETE_WINDOW", lambda: quit())
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

    menubar = Menu(root)                                # create top menu with commands
    root.config(menu=menubar)                           # attach menu to root

    fileMenu = Menu(menubar)                            # create dropdown menu
    fileMenu.add_command(label="add category", command=lambda: __add_category())        # some menu functions
    fileMenu.add_command(label="add program", command=lambda: __add_program())          # some menu functions
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=lambda: quit())                          # some menu functions
    menubar.add_cascade(label="Options", menu=fileMenu)                                 # some menu functions
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

    root.bind_class("kat", "<4>", lambda event: pan.scroll_linux(event))
    root.bind_class("kat", "<5>", lambda event: pan.scroll_linux(event))

    root.bind_class("programs", "<4>", lambda event: of.scroll_linux(event))
    root.bind_class("programs", "<5>", lambda event: of.scroll_linux(event))
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

    # make the canvas expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    #////////////////////////////////////////////////////////////////////////////////////////////////////////

    #podkontejner top-a, i glavni za elemente
    w, h = __get_resolution(root)

    imagebg = 'imgs/required/purple2.jpg'
    bgs = pil_image(imagebg, w, h)

    can = Canvas(root)
    can.create_image(w/2, h/2-25, image=bgs)
    can.image = bgs
    can.rowconfigure(1, weight=1)
    can.columnconfigure(2, weight=1)
    can.pack(expand=1, fill=BOTH)
    #////////////////////////////////////////////////////////////////////////////////////////////////////////

    #kateogrije - levi panel                        # container for categories
    kat = Canvas(can, width=150, height=h-50, bg='light green')
    kat.pack(side='left', padx=10, pady=10, expand=0, fill=BOTH)
    kat.bindtags(tagList=['kat'])

    imgs = ImageTk.PhotoImage(Image.open("imgs/kate.jpg"))     # background of previous Canvas (kategorije)
    img_dict = {'image': imgs}
    kwargs2.update(img_dict)

    pan = ScrollBarWidget(kat, 178, h-50, kwargs2)
    panel = pan.get_instance()
    panel.bindtags(tagList=['kat'])
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////

    #desni panel                                                       # right side of screen
    w2 = int((w-275)/3*2)
    glavni = Canvas(can, width=w-270, height=h-50)           # container for porgramms and virtual terminal
    glavni.pack(side='left', padx=5, pady=10, fill=BOTH, expand=1)
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////

    img_dict = {'image': imgs}
    kwargs3.update(img_dict)

    of = ScrollBarWidget(glavni, w2, h-50, kwargs3)
    obj_field = of.get_instance()
    obj_field.bindtags(tagList=['programs'])

    terminal = Text(glavni, width=45, bg='purple', fg='white', height=50, wrap=WORD)    # for terminal
    terminal.pack(side='right', fill=BOTH)
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////

    fill_label(panel, obj_field, terminal)

#3
def __get_resolution(root):
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    return w, h

#4
def pil_image(path, x, y):
    # return image object with custom size, mainly for buttons
    try:
        imagen = Image.open(path)
        imagen = imagen.resize((x, y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imagen)
        return img
    except:
        imagen = Image.open('imgs/required/default.jpg')
        imagen = imagen.resize((x, y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(imagen)
        return img

#5
def __add_category():
    # used to mainpulate categories
    cats = Toplevel()                                           # create top level window (pop-up)
    cats.geometry("350x400")                                    # its size

    ft = Frame(cats, width=300, bg='purple')                    # container
    ft.pack(side='top', expand=0, fill=BOTH)

    entry = Entry(ft, width=30, fg='purple')                    # used to get the name of category that you want to add
    entry.pack(side='left', expand=1, fill=BOTH, pady=5, padx=5)

    img = pil_image('imgs/required/add.png', 30, 30)               # just picture for better looking
    btn = Button(ft, text='add', image=img, compound='right', height=20, command=lambda: __add_cat_2('', entry), fg='purple')
    btn.image = img                                                # button to add category
    btn.pack(side='left', pady=5, padx=5, expand=0, fill=BOTH)
    btn.bind("<Return>", lambda event: __add_cat_2(event, entry))  # bind Enter event

    fb = Frame(cats, width=300, bg='purple')                        # container
    fb.pack(side='top', expand=1, fill=BOTH)
    txt = Text(fb, wrap='word', width=49, fg='purple')              # Text widget used to contain categories
    txt.pack(pady=5, padx=5, expand=1, fill=BOTH)
    try:
        cats = open('configs/category.txt', 'r')                    # open file with categories
        text = cats.read()                                          # read file
        text_list = text.split("\n")                                # split into list
        text_list.sort()                                            # alphabeticaly sort list
        for line in text_list:
                txt.insert(END, line+'\n')                          # insert category into Text widget
        cats.close()                                                # close file
    except Exception as e:
        print(e, '__add_category')

#6
def __add_cat_2(event, entry):
    # function called from btn in 3a
    var = entry.get()                                       # get text from entry
    var2 = var.title()                                      # format string as title
    try:
        cats = open('configs/category.txt', 'a+')           # open file
        cats.write('\n'+var2)                               # write text from entry into new line
        with open("configs/" + var + ".txt", "a+") as f:    # make new file for added category
            f.write('')
        f.close()
        cats.close()
    except:
        pass
    python = sys.executable                                 # restart app
    os.execl(python, python, * sys.argv)                    #

#7
def __add_program():
    pass


#9
def fill_label(panel, obj_field, terminal):
    # function called as continuation of gui(root) (1)
    global  srch
    srch = Entry(panel)
    srch.pack(side='top', fill='x', padx=5, pady=5)
    srch.bind("<KeyRelease>", lambda event: __cat_search(event, srch, panel, obj_field, terminal))

    __cat_search('', srch, panel, obj_field, terminal)        # initial fill (all categories without filtering)

#10
def __cat_search(event, srch, panel, obj_field, terminal):
    global lb, pan        # list of category buttons
    if len(lb) > 0:       # destroy old category buttons
        for ijk in lb:
            ijk.destroys()
    lb = lb[:0]

    pattern = srch.get()                                    # get text from entry, for filtering
    pattern = pattern.title()                               # first letter to be Capital
    try:
        cats = open('configs/category.txt', 'r')            # open file with categories
        text = cats.read()                                  # read
        text_list = text.split("\n")                        # split to list on new line
        text_list.sort()                                    # sort alph.

        if len(pattern) > 0:                                # if there is filtering
            temp = []                                       # temporary list
            for item in text_list:                          # list iteration
                if pattern in item:                         # if pattern matching
                    temp.append(item)                       # fill temp list with categories that have passed filtering
            text_list = temp[:]                             # truncate original list with filtered one

        for line in text_list:
            if line != '':                                  # if there is any letter
                b = CustomButton(panel, line, kwargs1, lambda line=line: query(line.lower(), obj_field, terminal))
                lb.append(b)                                # create button from  and append to lb
        pan.updates()                                       # update bbox

    except Exception as e:
        print(e, 'cat search')

#11
def query(num, obj_field, terminal):
    # called from CustomButtons in fill_label (4)
    obj_field.update()                          # update program container
    file_txt = 'configs/' + num + '.txt'        # select file for choosen category

    try:
        f = open(file_txt, 'r')                 # open that file
        text = f.read()                         # read
        text = text.replace('\n', '')           # truncate new lines
        text_list = text.split(";")             # split into list of lines on ' ; '

        create_obj_list(text_list, obj_field, terminal, num)  # call next function
        f.close()                               # close file
    except Exception as e:
        print(e, 'query')

#12
def create_obj_list(text_list, obj_field, terminal, num):
    global lst              # this is list from next func which contains widgets
    if len(lst) > 0:
        for x in lst:
            x.destroys()    # destroy old widgets
        lst = lst[:0]

    object_list = []        # create local list

    for i in range(0, len(text_list)-1, 9):  # create chunks (entirety) of 9 lines as list, from <object> to </object>
        tmp_lst = text_list[i:i+9]
        object_list.append(tmp_lst)          # append that list of 9 lines to local list [[9 x lines],[9 x lines],[]...]

    get_objects(object_list, obj_field, terminal, num)   # call next function to manipulate this lists

#13
def get_objects(object_list, obj_field, terminal, num):
    # extract data from object_list (list of nine-line lists)
    global lst
    for j in object_list:
        obj = Object(j[1][6:], j[2][6:], j[3][6:], j[4][6:], j[5][6:], j[6][6:], j[7][6:], num)
                                                        # Create Object (class Object from klase.py)   , num is category
        lst.append(obj)                                 # list of obejcts
    draw_objects(lst, obj_field, terminal)              # call next function

#14
def draw_objects(lst, off, term):
    # continuation of 7
    global w2, glavni, can, of
    tw = int(w2/4)
    cc = 0
    cr = 0
    for obj in lst:                                       # place holder for img and 3 buttons (install, delete, update)
        can2 = Canvas(off, width=tw, height=100, bg='purple')
        can2.grid(row=cr, column=cc, padx=5, pady=10, sticky='N'+'S'+'E'+'W')
        can2.bindtags(tagList=['programs'])
        obj.pack(can2, term, glavni, can)
        of.updates()
        cc += 1
        if cc == 4:
            cr += 1
            cc = 0

    if len(lst) < 4:      # if there are less than 4 programms (3 ... 0) fill with empty ones, if this is ommited it will shrink
        for i in range(0, 4-len(lst)):
            can3 = Canvas(off, bg='purple', width=tw, height=100)
            can3.grid(row=cr, column=cc, padx=5, pady=10, sticky='N'+'S'+'E'+'W')
            o = Object('', '', '', '', '', '', '', '')
            o.pack_empty(can3)
            cc += 1
        if cc == 4:
            cr += 1
            cc = 0

    update()               # update content

#15
def update():
    global can, glavni, obj_field
    obj_field.update_idletasks()
    glavni.config(scrollregion=glavni.bbox("all"))


#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////
# CLASSES

class AutoScrollbar(Scrollbar):

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.tk.call("grid", "remove", self)


    def pack(self, **kw):
        raise TclError("cannot use pack with this widget")

    def place(self, **kw):
        raise TclError("cannot use place with this widget")


class ScrollBarWidget():

    def __init__(self, parent, w, h, kwargs2):
        self.parent = parent
        self.image = kwargs2['image']
        self.tag = kwargs2['tag']
        print(w, h, kwargs2['tag'])

        self.glavni = Canvas(self.parent, bg='white', width=w, height=h, highlightbackground=kwargs2['hlb'], highlightthickness=kwargs2['hlt'])
        self.glavni.pack(side=kwargs2['side'], padx=kwargs2['padx'], pady=kwargs2['pady'], fill=kwargs2['fill'], expand=kwargs2['exp'])
        self.glavni.bindtags(tagList=[kwargs2['tag']])

        self.vscrollbar = AutoScrollbar(self.glavni)
        self.vscrollbar.grid(row=0, column=1, sticky=N+S)
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////

        # self.can = gradient.Example(parent).pack(fill="both", expand=True)
        if self.image is None:
            self.can = Canvas(self.glavni, width=w+100, height=h, yscrollcommand=self.vscrollbar.set)
        else:
            self.can = Canvas(self.glavni, width=w, height=h, yscrollcommand=self.vscrollbar.set)
            self.can.create_image(w/2, h/2, image=self.image)
            self.can.image = self.image
            self.can.bindtags(tagList=[self.tag])



        self.glavni.rowconfigure(0, weight=1)
        self.glavni.columnconfigure(0, weight=1)

        # self.can.rowconfigure(0, weight=1)
        # self.can.columnconfigure(0, weight=1)

        self.vscrollbar.config(command=self.glavni.yview)
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////

        self.glavni.create_window(0, 0, anchor=NW, window=self.can, tags=self.tag)
        self.parent.update_idletasks()
        self.glavni.config(scrollregion=self.glavni.bbox(self.tag))


    def updates(self):
        self.parent.update_idletasks()
        self.glavni.config(scrollregion=self.glavni.bbox(self.tag))
        self.parent.update_idletasks()


    def get_instance(self):
        return self.can


    def scroll_linux(self, event):
        if event.num == 5 or event.delta == -120:
            self.glavni.yview('scroll', 1, 'units')
        if event.num == 4 or event.delta == 120:
            self.glavni.yview('scroll', -1, 'units')

    def resolution(self):
        w = self.can.winfo_width()
        h = self.can.winfo_height()
        h2 = self.glavni.winfo_height()
        print(w, h , h2)
        if h > h2:return False, h, w
        else:     return True, h, w


class CustomButton(Button):

    def __init__(self, parent, texts, kwargs, cmnd):

        try:
            im_path = 'imgs/required/'+texts.lower()+'.jpg'
            imagen = Image.open(im_path)
            imagen = imagen.resize((40, 30), Image.ANTIALIAS)
            imag = ImageTk.PhotoImage(imagen)
        except:
            im_path = 'imgs/required/default.jpg'
            imagen = Image.open(im_path)
            imagen = imagen.resize((40, 30), Image.ANTIALIAS)
            imag = ImageTk.PhotoImage(imagen)

        self.category = texts
        self.btn = Button(parent, text=texts, image=imag, compound='left', anchor='w',
            width=kwargs['wd']*10, height=kwargs['ht']*10, bg=kwargs['bg'], command=cmnd)
        self.btn.bindtags(tagList=['Button', 'kat'])
        self.btn.image = imag
        self.btn.pack(side=kwargs['side'], padx=kwargs['padx'], pady=kwargs['pady'], fill=kwargs['fill'])


    def destroys(self):
        self.btn.destroy()

    def invoke(self):
        self.btn.invoke()


class Object():

    def __init__(self, id , name, vers, imag, cmnd, delt, updt, cat):
        self.id = id
        self.name = name
        self.version = vers
        self.img = imag
        self.command = cmnd
        self.delete = delt
        self.update = updt
        self.category = cat

    def get_data(self):
        print('           data ')
        print('id      ', self.id)
        print('name    ', self.name)
        print('version ', self.version)
        print('image   ', self.img, type(self.img))
        print('command ', self.command, type(self.command))
        print('delete  ', self.delete)
        print('update  ', self.update)
        print('end data ')

    def pack(self, parent, terminal, top, can):
        self.parent = parent
        img2 = self.pil_image(self.img, 90, 90)
        img_place = Button(parent, width=100, height=100, image=img2, command=lambda: self.img_btn(), bg='purple')
        img_place.bindtags(tagList=['Button', 'programs'])
        img_place.image = img2
        img_place.pack(side='left', expand=0, fill=BOTH)

        kont = Canvas(parent, bg='purple')
        kont.bindtags(tagList=['programs'])
        kont.pack(side='left', expand=1, fill=BOTH)

        b1 = Button(kont, text='install', command=lambda: self.switch(self.command, terminal, top, can))
        b1.bindtags(tagList=['Button', 'programs'])
        b1.pack(side='top', expand=1, fill='x')

        b2 = Button(kont, text='uninstall', command=lambda: self.switch(self.delete, terminal, top, can))
        b2.bindtags(tagList=['Button', 'programs'])
        b2.pack(side='top', expand=1, fill='x')

        b3 = Button(kont, text='update', command=lambda: self.switch(self.update, terminal, top, can))
        b3.bindtags(tagList=['Button', 'programs'])
        b3.pack(side='top', expand=1, fill='x')

    def pack_empty(self, parent):
        img2 = self.pil_image('imgs/required/edit.jpg', 90, 90)
        self.img_place = Button(parent, width=100, height=100, image=img2, command='', bg='purple')
        self.img_place.image = img2
        self.img_place.pack(side='left', expand=0, fill=BOTH)

        kont = Canvas(parent, bg='purple')
        kont.pack(side='left', expand=1, fill=BOTH)

        b1 = Button(kont, text='install', state='disabled')
        b1.pack(side='top', expand=1, fill='x')
        b2 = Button(kont, text='uninstall', state='disabled')
        b2.pack(side='top', expand=1, fill='x')
        b3 = Button(kont, text='update', state='disabled')
        b3.pack(side='top', expand=1, fill='x')

    def switch(self, cmnd, terminal, top, can):
        if 'sudo' in cmnd:
            self.sudo(cmnd, terminal, top, can)
        else:
            self.func(cmnd, terminal, top, can)

    def sudo(self, cmnd, terminal, top, can):   # 1

        sudo_password = 'your sudo code' + '\n'
        sudos = ['sudo', '-S']

        terminal.delete('1.0', END)

        for item in eval(cmnd):
            cmd = sudos + item.split()

            p = subprocess.Popen(cmd,  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
            p.stdin.write(sudo_password)
            p.poll()

            while True:
                line = p.stdout.readline()
                terminal.insert(END, line)
                terminal.see(END)
                can.update_idletasks()
                top.config(scrollregion=top.bbox("all"))
                if not line and p.poll is not None: break

            while True:
                err = p.stderr.readline()
                terminal.insert(END, err)
                terminal.see(END)
                can.update_idletasks()
                top.config(scrollregion=top.bbox("all"))
                if not err and p.poll is not None: break
            terminal.insert(END, '\n * END OF PROCESS *')

    def func(self, cmnd): #2
        try:
            proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = proc.communicate(str.encode(cmnd))

            for i in stdout:
                if i is not None:
                    if len(i) > 0:
                        pass
            proc.kill()
        except Exception as e:
            print(e, 'func')

    def destroys(self):
        self.parent.destroy()

    def img_btn(self):

        edit = Toplevel()
        edit.resizable(width=FALSE, height=FALSE)
        edit.bind("<Return>", lambda event: self.save_edit(event, e1, e2, e3, e4, e5, edit) )
        can = Canvas(edit, width=700, height=500, bg='purple')
        can.pack(expand=1, fill=BOTH)
        can.bind("<Return>", lambda event: self.save_edit(event, e1, e2, e3, e4, e5, edit) )
        #///////////////////////////////////////////////////////////////////////////////////////////////////
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        gornji = Canvas(can, height=110, bg='purple')
        gornji.pack(side='top', expand=1, fill='x', pady=5, padx=5)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        slika = self.pil_image(self.img, 90, 90)
        img_place = Button(gornji, width=100, height=100, image=slika, command=lambda: self.__inner_image(img_place, edit), bg='purple')
        img_place.image = slika
        img_place.pack(side='left', expand=0, fill=BOTH)

        mid_can = Canvas(gornji)
        mid_can.pack(side='right', expand=1, fill=BOTH)

        l = len(self.name)
        h = math.ceil(l/50.)
        l1 = Label(mid_can, text='Name :', anchor='w')
        l1.pack(side='top', expand=1, fill='x')
        e1 = Text(mid_can, width=50, height=h)
        e1.pack(side='top', expand=1, fill='x')
        e1.insert(INSERT, self.name)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        l = len(self.version)
        h = math.ceil(l/50.)
        l2 = Label(mid_can, text='Version :', anchor='w')
        l2.pack(side='top', expand=1, fill='x')
        e2 = Text(mid_can, width=50, height=h)
        e2.pack(side='top', expand=1, fill='x')
        e2.insert(INSERT, self.version)
        #///////////////////////////////////////////////////////////////////////////////////////////////////
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        srednji = Canvas(can, bg='purple')
        srednji.pack(side='top', expand=1, fill='x', padx=5, pady=5)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        lf = LabelFrame(srednji)
        lf.pack(side='top', expand=1, fill='x')

        l3 = Label(lf, text='Install :', anchor='w')
        l3.pack(side='left', expand=1, fill=BOTH)
        l = len(self.command)
        h = math.ceil(l/50.)
        e3 = Text(srednji, width=50, height=h)
        e3.pack(side='top', expand=0, fill=BOTH)
        e3.insert(INSERT, self.command)

        dir_img = self.pil_image('imgs/required/dir.png', 30, 20)
        dir = Button(lf, image=dir_img, command=lambda: self.__dir_path(e3))
        dir.image = dir_img
        dir.pack(side='right', expand=0, fill='x')
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        l = len(self.delete)
        h = math.ceil(l/50.)
        l4 = Label(srednji, text='Delete :', anchor='w')
        l4.pack(side='top', expand=1, fill='x')
        e4 = Text(srednji, width=50, height=h)
        e4.pack(side='top', expand=1, fill='x')
        e4.insert(INSERT, self.delete)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        l = len(self.update)
        h = math.ceil(l/50.)
        l5 = Label(srednji, text='Update :', anchor='w')
        l5.pack(side='top', expand=1, fill='x')
        e5 = Text(srednji, width=50, height=h)
        e5.pack(side='top', expand=1, fill='x')
        e5.insert(INSERT, self.update)
        #///////////////////////////////////////////////////////////////////////////////////////////////////
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        donji = Canvas(can, bg='purple', highlightthickness=0)
        donji.pack(side='top', expand=1, fill='x', padx=5, pady=5)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        img22 = self.pil_image('imgs/required/cancel.png', 30, 30)
        cancel = Button(donji, image=img22, bg='purple', command=lambda: edit.destroy(), highlightthickness=0)
        cancel.image = img22
        cancel.pack(side='left', expand=0, fill='x')
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        img23 = self.pil_image('imgs/required/save.png', 30, 30)
        save = Button(donji, image=img23, bg='purple', command=lambda: self.save_edit('', e1, e2, e3, e4, e5, edit), highlightthickness=0)
        save.image = img23
        save.pack(side='right', expand=0, fill='x')
        #///////////////////////////////////////////////////////////////////////////////////////////////////

    def pil_image(self, path, x, y):
        try:
            imagen = Image.open(path)
            imagen = imagen.resize((x, y), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(imagen)
            return img
        except Exception:
            imagen = Image.open('imgs/required/default.jpg')
            imagen = imagen.resize((x, y), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(imagen)
            return img

    def save_edit(self, event, e1, e2, e3, e4, e5, edit):
        file_txt = 'configs/' + self.category + '.txt'
        f_temp = 'configs/' + self.category + '_temp' + '.txt'
        temp = 'configs/' + 'temp.txt'

        try:
            e1v = e1.get('1.0', END).replace('\n', '')
            e2v = e2.get('1.0', END).replace('\n', '')
            e3v = e3.get('1.0', END).replace('\n', '')
            e4v = e4.get('1.0', END).replace('\n', '')
            e5v = e5.get('1.0', END).replace('\n', '')



            f_imag = '$imag:' + self.img + ';\n'
            f_id   = '$ajdi:' + self.id  + ';\n'
            f_name = '$name:' + e1v + ';\n'
            f_vers = '$vers:' + e2v + ';\n'
            f_inst = '$cmnd:' + e3v + ';\n'
            f_delt = '$delt:' + e4v + ';\n'
            f_updt = '$updt:' + e5v + ';\n'


            f = open(file_txt, 'r+')
            ft = open(f_temp, 'w')

            for line1 in f:
                if line1 == f_id:
                    ft.write(f_id)
                    ft.write(f_name)
                    ft.write(f_vers)
                    ft.write(f_imag)
                    ft.write(f_inst)
                    ft.write(f_delt)
                    ft.write(f_updt)
                    for i in range(0, 6):
                        f.__next__()
                else:
                    ft.write(line1)

            ft.close()
            f.close()

            self.__file_permutation(file_txt, f_temp, temp)

            edit.destroy()
            self.__refresh()                # re-read data


        except Exception as e:
            print('save_edit', e)

    def __dir_path(self, e3):
        try:
            fn = fd.askopenfilename()
            if fn:
                e3.focus_set()
                e3.insert(INSERT, fn)
        except Exception as e:
            print(e)

    def __inner_image(self, btn, top):

        try:
            f_imag = '$imag:' + self.img + ';\n'                        # patterns for lines
            f_id   = '$ajdi:' + self.id  + ';\n'                        # patterns for lines

            file_txt = 'configs/' + self.category + '.txt'              # patterns for files
            f_temp = 'configs/' + self.category + '_temp' + '.txt'      # patterns for files
            temp = 'configs/' + 'temp.txt'                              # temp name for rename

            f = open(file_txt, 'r+')                                    # open regular file
            ft = open(f_temp, 'w')                                      # open temp file identical to regular file ...
                                                                        # except for changes

            for line1 in f:                                             # check each line in file
                if line1 == f_id:                                       # check id (ajdi)
                    ft.write(line1)                                     # write to ft
                    for i in range(0, 2):                               # write name and vers to ft
                        a = f.__next__()                                #
                        ft.write(a)                                     #

                    b = f.__next__()                                    # read imag line
                    if b == f_imag:                                     # if img path is ok
                        fo = fd.askopenfilename(initialdir='imgs/')     # search for image
                        fo = fo.replace(' ', '\ ')                      # bcs terminal reads space as "\ "
                        fb = os.path.basename(fo)                       # get file name

                        cwd = os.getcwd()                               # get cwd - current working directory
                        cwd = cwd.replace(' ', '\ ')                    # bcs terminal reads space as "\ "

                        imp = os.path.dirname(os.path.dirname(fo))      # get parent dir of choosen img

                        if cwd == imp:                                  # check if img is alredy in img dir
                            ttt = '$imag:imgs/' + fb + ';\n'            # just temp. variable
                            ft.write(ttt)                               # write to ft
                        else:
                            fun = "cp -i " + fo + " "  + cwd + "/imgs/" # cp -i image  folder + /imgs
                            fun = codecs.decode(fun, 'unicode_escape')  # decoding "\\" to "\"
                            self.func(fun)                              # if not in imgs/  dir then copy
                            ttt = '$imag:imgs/' + fb + ';\n'            # just temp. variable
                            ft.write(ttt)                               # write in ft path of copied image

                else:                                                   # write everyth. that isn't necessary
                    ft.write(line1)                                     # write to ft

            f.close()
            ft.close()

            self.__file_permutation(file_txt, f_temp, temp)
            top.destroy()


        except Exception as e:
           print( e, '__inner_image')

    def __file_permutation(self, first, second, temp):
        os.rename(first, temp)      # rename first file to temp
        os.rename(second, first)    # rename second file to first
        os.remove(temp)             # remove temp file eg. first

    def __refresh(self,):

        global lb
        if len(lb) > 0:
            for button in lb:
                bc = button.category.lower()
                if bc == self.category:
                    button.invoke()



main()


# probati resiti da se pravi canvas.create_window za svaki program
