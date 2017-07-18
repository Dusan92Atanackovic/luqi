__author__ = 'atana'

from tkinter import *
import gradient, sqlite
from PIL import ImageTk, Image
import tkinter.filedialog as fd

# globals
programs_instance = None
cat_instance = None
programs_sb = None
cat_sb = None
programs = None
root = None
term = None
cat_list = []
scroll_bar_cat = None
db = 'programs.db'

#   call main to get instance of Tk
#   call gui to setup background containers + menu
#   call fill categories
#   fill programs

def main():
    global root
    root = Tk()
    # w, h = __get_resolution(root)
    # root.geometry("%dx%d" % (w, h))
    root.geometry("%dx%d" % (1366, 768))
    root.resizable(False, False)
    root.minsize(800, 400)
    root.columnconfigure(0, weight=1)
    gui(root)
    root.mainloop()

# OK
def __get_resolution(parent):
    w = parent.winfo_screenwidth()
    h = parent.winfo_screenheight()
    return 1366, 768

# OK ? do i need this ?
def __get_resolution2(root):
    w = root.winfo_width()
    h = root.winfo_height()
    return w, h

# OK
def gui(parent):

    global programs_instance, cat_instance, programs_sb, cat_sb, term, programs, cat_list

    # background
    w, h = __get_resolution(parent)
    # print(w, h)

    top_container = gradient.Example(parent, 'orange', 'white')
    gradient_instance = top_container.getFrame()
    gradient_instance.grid_rowconfigure(1, weight=1)
    gradient_instance.grid_columnconfigure(1, weight=1)

    # adding top menu
    __add_menu(parent)

    #************************************************************************************************************************************************

    # categories section
    categories = Canvas(gradient_instance, bg='white', width=int(w*0.15), height=h-50)
    categories.grid(row=0, column=0, sticky='ns', padx=20, pady=20)
    categories.propagate(False)

    # category scrollbar
    cat_sb = gradient.ScrollBarWidget(categories, 'orange', 'green')
    cat_instance = cat_sb.get_instance()

    # categories extracted from db
    cat_list = sqlite.get_categories(db)

    # for j in range(0, 10):
    for item in cat_list:
        im_path = item[2]
        try:
            imagen = Image.open(im_path)
            imagen = imagen.resize((40, 30), Image.ANTIALIAS)
            imag = ImageTk.PhotoImage(imagen)
        except:
            imag = None

        b = Button(cat_instance,  text=item[1], width=int(w*0.15), compound='left', anchor='w', image=imag, bg='white', command=lambda item=item: categoryFilter(item))
        b.image = imag
        b.bindtags(tagList=['Button', 'tag'])
        b.grid(sticky='nsew')
    cat_sb.updates()

    #************************************************************************************************************************************************

    # programs section
    programs = Canvas(gradient_instance, bg='white', width=int(w*0.60), height=h-50)
    programs.grid(row=0, column=1, sticky='nsew', padx=10, pady=20)
    programs.propagate(False)

    # programs scrollbar
    programs_sb = gradient.ScrollBarWidget(programs, 'white', 'white')
    programs_instance = programs_sb.get_instance()

    #************************************************************************************************************************************************
    #
    termFrame = Frame(gradient_instance, width=int(w*0.25), bg='red')
    termFrame.grid(row=0, column=2, sticky='nsew', padx=10, pady=20)
    termFrame.propagate(False)

    term = Text(termFrame,  bg='purple', fg='white', height=50, wrap=WORD)    # for terminal
    term.pack(expand=1, fill='y')
    term.propagate(False)

    #************************************************************************************************************************************************

    # linux mouse scroll events
    parent.bind_class("tag", "<4>", lambda event: cat_sb.scroll_linux(event))
    parent.bind_class("tag", "<5>", lambda event: cat_sb.scroll_linux(event))

    parent.bind_class("tag2", "<4>", lambda event: programs_sb.scroll_linux(event))
    parent.bind_class("tag2", "<5>", lambda event: programs_sb.scroll_linux(event))

    parent.bind_class("add_cat", "<4>", lambda event: scroll_bar_cat.scroll_linux(event))
    parent.bind_class("add_cat", "<5>", lambda event: scroll_bar_cat.scroll_linux(event))


    #initial fill
    categoryFilter(None)

# OK
def __add_menu(root):
    menubar = Menu(root)                                # create top menu with commands
    root.config(menu=menubar)                           # attach menu to root

    fileMenu = Menu(menubar)                            # create dropdown menu
    fileMenu.add_command(label="add category    Ctrl+Shit+A", command=lambda: __add_category())        # some menu functions
    fileMenu.add_command(label="add program    Ctrl+Shit+P", command=lambda: __add_program())          # some menu functions
    fileMenu.add_separator()
    fileMenu.add_command(label="       Exit    Ctrl+Shit+Q", command=lambda: quit())                   # some menu functions
    menubar.add_cascade(label="Options", menu=fileMenu)                                                # some menu functions

    inst = Menu(menubar)
    inst.add_command(label='add +', command='')
    inst.add_command(label='predefined +', command='')
    menubar.add_cascade(label="instalations", menu=inst)

    git = Menu(menubar)
    git.add_command(label='go to Git', command='')
    menubar.add_cascade(label="Git", menu=git)

    root.bind("<Control-Shift-Key-a>", lambda event: __add_category())
    root.bind("<Control-Shift-Key-A>", lambda event: __add_category())

    root.bind("<Control-Shift-Key-p>", lambda event: __add_program())
    root.bind("<Control-Shift-Key-P>", lambda event: __add_program())

    root.bind("<Control-Shift-Key-q>", lambda event: quit())
    root.bind("<Control-Shift-Key-Q>", lambda event: quit())

    #///////////////////////////////////////////////////////////////////////////////////////////////////////

# OK
def __add_category():

    global cat_list, scroll_bar_cat
     # used to mainpulate categories
    cats = Toplevel()                                           # create top level window (pop-up)
    cats.geometry("350x400")                                    # its size
    cats.resizable(False, False)
    ft = Frame(cats, width=300, bg='orange')                    # container
    ft.pack(side='top', expand=0, fill=BOTH)
    ft.bindtags(tagList=['add_cat'])

    entry = Entry(ft, width=30, fg='purple')                    # used to get the name of category that you want to add
    entry.pack(side='left', expand=1, fill=BOTH, pady=5, padx=5)
    entry.bind("<Return>", lambda event: __add_cat_2(event, entry, ft))  # bind Enter event

    img = pil_image('imgs/required/add.png', 30, 30)               # just picture for better looking
    btn = Button(ft, text='add', image=img, compound='right', height=20, command=lambda: __add_cat_2('', entry, ft), fg='purple')
    btn.image = img                                                # button to add category
    btn.pack(side='left', pady=5, padx=5, expand=0, fill=BOTH)

    fb = Canvas(cats, width=300, bg='orange')                        # container
    fb.pack(side='top', expand=1, fill=BOTH)
    fb.bindtags(tagList=['add_cat'])

    scroll_bar_cat = gradient.ScrollBarWidget(fb, 'white', 'orange')
    ft = scroll_bar_cat.get_instance()

    try:
        _add_gui_category(ft)

    except Exception as e:
        print(e, '__add_category')

# OK
def __add_cat_2(event, entry, parent):
    var = entry.get()                                       # get text from entry
    var2 = var.title()                                      # format string as title
    ans = False
    try:
        if len(var2) > 0:
            ans = sqlite.insert_into_categories(db, var2)

    except Exception as e:
        print('exception in add cat 2', e)

    finally:
        if ans is True:
            _add_gui_category(parent)

# OK
def _add_gui_category(sb):

    global cat_list, scroll_bar_cat, cat_instance, root

    # part for adding categories

    for child in sb.winfo_children():
        child.destroy()

    ft = scroll_bar_cat.get_instance()
    cat_list = sqlite.get_categories(db)


    for line in cat_list:                                                       # insert category into Text widget
        fr = Frame(ft, bg='purple', width=200)
        fr.pack(expand=1, fill=BOTH)

        ent = Entry(fr, width=35, bg='orange', fg='white')
        ent.pack(side='left', expand=1, fill=BOTH)

        ent.insert(0, line[1])

        ent.bindtags(tagList=['Entry', 'add_cat'])
        ent.bind_class('add_cat', "<Return>", lambda event, line=line, ent=ent: sqlite.update_category_name(event, db, line, ent))

        imgsd = pil_image('imgs/required/btns/ch_pic.png', 30, 30)
        img_location = Button(fr, image=imgsd, borderwidth=2, relief="groove", fg='white', anchor='w', command=lambda line3=line:chPic(line3))
        img_location.image = imgsd
        img_location.pack(side='left', expand=0, fill=BOTH)
        img_location.bindtags(tagList=['Button', 'add_cat'])

    scroll_bar_cat.updates()


    # part for original categories
    w, h = __get_resolution(root)

    for child in cat_instance.winfo_children():
        child.destroy()

    # for j in range(0, 10):
    for item in cat_list:
        im_path = item[2]
        try:
            imagen = Image.open(im_path)
            imagen = imagen.resize((40, 30), Image.ANTIALIAS)
            imag = ImageTk.PhotoImage(imagen)
        except:
            imag = None

        b = Button(cat_instance,  text=item[1], width=int(w*0.15), compound='left', anchor='w', image=imag, bg='white', command=lambda item=item: categoryFilter(item))
        b.image = imag
        b.bindtags(tagList=['Button', 'tag'])
        b.grid(sticky='nsew')
    cat_sb.updates()

# NOT FINISHED
def __add_program():
    print('i am here')
    pass


# OK
def categoryFilter(param):

    global programs_instance
    tlist = []

    if param is None:
        prog_list = sqlite.get_programs_data(db, param)
    else:
        prog_list = sqlite.get_programs_data(db, param[0])

    # print('pl', prog_list)

    for j in prog_list:
        obj = gradient.Object(j[0], j[1], j[2], j[3], j[4], j[5], j[6], j[7])
        tlist.append(obj)

    draw_objects(tlist)

# OK
def chPic(param):
    # change picture for
    global  scroll_bar_cat
    fp = fd.askopenfilename(initialdir='imgs/')
    if len(fp) > 0:
        resp = sqlite.update_category(db, param[0], fp)
        if resp is True:
            _add_gui_category(scroll_bar_cat.get_instance())

# OK
def draw_objects(lst):

    global programs_instance, cat_instance, programs_sb, root, term, programs

    img_size= gradient.object_image

    w2, h = __get_resolution(root)

    for child in programs_instance.winfo_children():
        child.destroy()

    tw = int((w2*0.6 -20) / img_size)

    cc = 0
    cr = 0
    # for j in range(0, 10):
    if len(lst) > 1:
        for obj in lst:                                       # place holder for img and 3 buttons (install, delete, update)
            obj.pack(programs_instance, term, programs_sb, cc, cr)
            programs_sb.updates()
            cc += 1
            if cc == tw-1:
                cr += 1
                cc = 0
    #
    if len(lst) < 1:      # if there are less than 4 programms (3 ... 0) fill with empty ones, if this is ommited it will shrink
        for i in range(0, 1):
            o = gradient.Object('', '', '', '', '', '', '', '')
            o.pack_empty(programs_instance)


    update()               # update content

def gotoGit(url):
    print ('this should take you to git page')

# OK
def update():
    global programs_sb
    programs_sb.updates()

# OK
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




main()