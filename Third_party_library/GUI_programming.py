from tkinter import *

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.helloLabel = Label(self, text = 'Hello Claude\n')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Confirm', command=self.quit)
        self.quitButton.pack()
        
app = Application()
app.master.title('Message from system')
app.mainloop()
