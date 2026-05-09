import tkinter as tk

class Calc:
    def __init__(self):

        self.app = tk.Tk()
        self.app.geometry('300x400')
        self.app.resizable(False,False)
        self.text=''
        self.last_was_equal = False
        for i in range(7):
            self.app.grid_rowconfigure(i, weight=1)

        for i in range(4):
            self.app.grid_columnconfigure(i, weight=1)
        self.label = tk.Label(font=(15),anchor="e")
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.buts()
        self.app.mainloop()
        
    def buts(self):
        tk.Button(text='1',command=lambda: self.number(1)).grid(row=5,column=0,sticky="nsew",padx=2, pady=2)
        tk.Button(text='2',command=lambda: self.number(2)).grid(row=5,column=1,sticky="nsew",padx=2, pady=2)
        tk.Button(text='3',command=lambda: self.number(3)).grid(row=5,column=2,sticky="nsew",padx=2, pady=2)
        tk.Button(text='4',command=lambda: self.number(4)).grid(row=4,column=0,sticky="nsew",padx=2, pady=2)
        tk.Button(text='5',command=lambda: self.number(5)).grid(row=4,column=1,sticky="nsew",padx=2, pady=2)
        tk.Button(text='6',command=lambda: self.number(6)).grid(row=4,column=2,sticky="nsew",padx=2, pady=2)
        tk.Button(text='7',command=lambda: self.number(7)).grid(row=3,column=0,sticky="nsew",padx=2, pady=2)
        tk.Button(text='8',command=lambda: self.number(8)).grid(row=3,column=1,sticky="nsew",padx=2, pady=2)
        tk.Button(text='9',command=lambda: self.number(9)).grid(row=3,column=2,sticky="nsew",padx=2, pady=2)
        tk.Button(text='0',command=lambda: self.number(0)).grid(row=6,column=1,sticky="nsew",padx=2, pady=2)
        tk.Button(text='+',command=lambda: self.operator('+')).grid(row=6,column=0,sticky="nsew",padx=2, pady=2)
        tk.Button(text='-',command=lambda: self.operator('-')).grid(row=6,column=2,sticky="nsew",padx=2, pady=2)
        tk.Button(text='*',command=lambda: self.operator('*')).grid(row=4,column=3,sticky="nsew",padx=2, pady=2)
        tk.Button(text='/',command=lambda: self.operator('/')).grid(row=5,column=3,sticky="nsew",padx=2, pady=2)
        tk.Button(text='=',command=lambda: self.eqval('=')).grid(row=6,column=3,sticky="nsew",padx=2, pady=2)
        tk.Button(text='del',command=lambda: self.delete('dele')).grid(row=3,column=3,sticky="nsew",padx=2, pady=2)

    def number(self,num):
        if self.last_was_equal:
            self.text = ""
            self.last_was_equal = False

        self.text += str(num)
        self.label.config(text=self.text)
    def eqval(self,eqvala):
        if eqvala:
            if self.text:
                    result = eval(self.text)
                    self.text = str(result)
                    self.last_was_equal = True
                    self.label.config(text=self.text)
    def operator(self,op):
        if self.last_was_equal:
                self.last_was_equal = False
                
        self.text+=op

        self.label.config(text=self.text)
        
    def delete(self,dele):
        self.text = self.text[:-1]
        self.label.config(text=self.text)

    

lol=Calc()
