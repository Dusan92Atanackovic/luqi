# import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import subprocess, os, sys, math, codecs
import tkinter.filedialog as fd

object_image = 100;

class Example(Frame):
    def __init__(self, parent, color1, color2):
        Frame.__init__(self, parent)
        self.frame = GradientFrame(parent, color1, color2)
        # self.frame.pack(side='left', expand=1, fill=tk.BOTH)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.frame.grid_propagate(True)

        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def getFrame(self):
        return self.frame


class GradientFrame(Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1, color2, borderwidth=1, relief="sunken" ):
        Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)

        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)


    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")


# pokusati da ovo radi iz klasa

class AutoScrollbar(Scrollbar):

    def set(self, lo, hi):
        self.tk.call("grid", "remove", self)


    def pack(self, **kw):
        raise TclError("cannot use pack with this widget")

    def place(self, **kw):
        raise TclError("cannot use place with this widget")


class ScrollBarWidget():

    def __init__(self, parent, c1, c2):
        self.parent = parent
        self._color1 = c1
        self._color2 = c2
        # self.parent.bind("<Configure>", self._draw_gradient)

        self.vscrollbar = AutoScrollbar(self.parent)
        self.vscrollbar.grid(row=0, column=1, sticky=N+S)
        #//////////////////////////////////////////////////////////////////////////////////////////////////////////

        self.can = Canvas(self.parent,bg='white', yscrollcommand=self.vscrollbar.set)

        self.parent.rowconfigure(0, weight=1)
        self.parent.columnconfigure(0, weight=1)
        #
        # self.can.rowconfigure(0, weight=1)
        # self.can.columnconfigure(0, weight=1)

        self.vscrollbar.config(command=self.can.yview)

        #//////////////////////////////////////////////////////////////////////////////////////////////////////////

        self.parent.create_window(0, 0, anchor=NW, window=self.can, tags='all')
        self.parent.update_idletasks()
        self.parent.config(scrollregion=self.parent.bbox('all'))


    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.can.delete("gradient")
        width = self.can.winfo_width()
        height = self.can.winfo_height()
        limit = width
        (r1,g1,b1) = self.can.winfo_rgb(self._color1)
        (r2,g2,b2) = self.can.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.can.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.can.lower("gradient")


    def updates(self):
        self.parent.update_idletasks()
        self.parent.config(scrollregion=self.parent.bbox('all'))
        self.parent.update_idletasks()


    def get_instance(self):
        return self.can


    def scroll_linux(self, event):
        # print(self.can.winfo_height(), 'cwh')
        # print(self.parent.winfo_height(), 'pwh')

        ch = self.can.winfo_height();
        ph = self.parent.winfo_height()
        if ch >= ph:
            if event.num == 5 or event.delta == -120:
                self.parent.yview('scroll', 1, 'units')
            if event.num == 4 or event.delta == 120:
                self.parent.yview('scroll', -1, 'units')


class Object():

    def __init__(self, id , name, vers, cmnd, updt, delt, imag, cat):
        self.id = id
        self.name = name
        self.version = vers
        self.img = imag
        self.command = cmnd
        self.delete = delt
        self.update = updt
        self.category = cat

    # OK
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

    # OK
    def pack(self, parent, terminal, top, cc, cr):
        global object_image
        self.parent = parent
        img2 = self.pil_image(self.img, object_image-10, object_image-10)
        img_place = Button(parent, width=object_image-10, height=object_image-10, image=img2, command=lambda: self.img_btn(terminal, top), bg='white')
        img_place.bindtags(tagList=['Button', 'tag2'])
        img_place.image = img2
        img_place.grid(row=cr, column=cc,padx=0, pady=0, ipadx=10, ipady=10, sticky='N'+'S')

    # OK
    def pack_empty(self, parent):

        img2 = self.pil_image('imgs/required/edit.jpg', 150, 150)
        self.img_place = Button(parent, width=140, height=140, image=img2, command='', bg='purple')
        self.img_place.image = img2
        self.img_place.grid(row=0, column=0, padx=10, pady=10, sticky='N'+'S')

    # OK
    def switch(self, cmnd, terminal, top):
        if 'sudo' in cmnd:
            self.sudo(cmnd, terminal, top)
        else:
            self.func(cmnd, terminal, top)


    def sudo(self, cmnd, terminal, top):   # 1

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
                top.updates()
                if not line and p.poll is not None: break

            while True:
                err = p.stderr.readline()
                terminal.insert(END, err)
                terminal.see(END)
                top.updates()
                if not err and p.poll is not None: break
            terminal.insert(END, '\n * END OF PROCESS *')


    def func(self, cmnd, terminal, top): #2

        terminal.delete('1.0', END)

        try:
            proc = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            print(type(str.encode(cmnd)))
            stdout = proc.communicate(str.encode(eval(cmnd)))

            for i in stdout:
                print(i,' i')
                if i is not None:
                    if len(i) > 0:
                        terminal.insert(END, i)
                        top.updates()
            proc.kill()
            terminal.insert(END, '\n * END OF COMMAND *')

        except Exception as e:
            print(e, 'func')

    # NEED CHECK
    def destroys(self):
        self.parent.destroy()

    # OK
    def img_btn(self, terminal, top):

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

        lf2 = LabelFrame(lf)
        lf2.pack(expand=1, side='top', fill=BOTH)
        # l3 = Label(lf, text='Install :', anchor='w')
        # l3.pack(side='left', expand=1, fill=BOTH)

        dir_img = self.pil_image('imgs/required/btns/dir.png', 30, 20)
        dir = Button(lf2, image=dir_img, command=lambda: self.__dir_path(e3))
        dir.image = dir_img
        dir.pack(side='right', expand=0, fill='x')
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        lf3 = LabelFrame(lf)
        lf3.pack(expand=1, side='top')

        b3 = Button(lf3,  width=7, text="Install", command=lambda: self.switch(self.command, terminal, top))
        b3.pack(side='left', expand=1, fill=BOTH)

        l = len(self.command)
        h = math.ceil(l/50.)
        e3 = Text(lf3, width=50, height=h)
        e3.pack(side='left', expand=0, fill=BOTH)
        e3.insert(INSERT, self.command)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        lf4 = LabelFrame(lf)
        lf4.pack(expand=1, side='top')

        l = len(self.delete)
        h = math.ceil(l/50.)

        # l4 = Label(srednji, text='Delete :', anchor='w')
        # l4.pack(side='top', expand=1, fill='x')

        b4 = Button(lf4, width=7,  text="Delete", command=lambda: self.switch(self.delete, terminal, top))
        b4.pack(side='left', expand=1, fill=BOTH)

        e4 = Text(lf4, width=50, height=h)
        e4.pack(side='left', expand=0, fill='x')
        e4.insert(INSERT, self.delete)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        lf5 = LabelFrame(lf)
        lf5.pack(expand=1, side='top')

        l = len(self.update)
        h = math.ceil(l/50.)

        # l5 = Label(srednji, text='Update :', anchor='w')
        # l5.pack(side='top', expand=1, fill='x')

        b5 = Button(lf5, width=7, text="Update", command=lambda: self.switch(self.update, terminal, top))
        b5.pack(side='left', expand=1, fill=BOTH)

        e5 = Text(lf5, width=50, height=h)
        e5.pack(side='left', expand=0, fill='x')
        e5.insert(INSERT, self.update)


        #///////////////////////////////////////////////////////////////////////////////////////////////////
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        donji = Canvas(can, bg='purple', highlightthickness=0)
        donji.pack(side='top', expand=1, fill='x', padx=5, pady=5)
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        img22 = self.pil_image('imgs/required/btns/cancel.png', 30, 30)
        cancel = Button(donji, image=img22, bg='purple', command=lambda: edit.destroy(), highlightthickness=0)
        cancel.image = img22
        cancel.pack(side='left', expand=0, fill='x')
        #///////////////////////////////////////////////////////////////////////////////////////////////////

        img23 = self.pil_image('imgs/required/btns/save.png', 30, 30)
        save = Button(donji, image=img23, bg='purple', command=lambda: self.save_edit('', e1, e2, e3, e4, e5, edit), highlightthickness=0)
        save.image = img23
        save.pack(side='right', expand=0, fill='x')
        #///////////////////////////////////////////////////////////////////////////////////////////////////

    # OK
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

    # NEED CHECK
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

    # NEED CHECK
    def __dir_path(self, e3):
        try:
            fn = fd.askopenfilename()
            if fn:
                e3.focus_set()
                e3.insert(INSERT, fn)
        except Exception as e:
            print(e)

    # NEED CHECK
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

    # NEED CHECK
    def __file_permutation(self, first, second, temp):
        os.rename(first, temp)      # rename first file to temp
        os.rename(second, first)    # rename second file to first
        os.remove(temp)             # remove temp file eg. first

    # NEED CHECK
    def __refresh(self,):

        global lb
        if len(lb) > 0:
            for button in lb:
                bc = button.category.lower()
                if bc == self.category:
                    button.invoke()
