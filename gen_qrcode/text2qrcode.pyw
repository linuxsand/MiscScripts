from Tkinter import *
import qrcode

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.label = Label(self, text='Input plain text:')
        self.text = Text(self, height=20, width=40)
        self.button = Button(self, text='Confirm', command=self.convert)
        self.pack()
        self.label.pack()
        self.text.pack()
        self.button.pack()

        self.image_object = None
        
    def convert(self):
        text = self.text.get(1.0, 'end-1c')
        if not text.isspace():
            self.image_object = qrcode.make(data=text)
            self.show()
            
    def show(self):
        self.image_object.show()

        
def main():
    window = Window()
    window.master.title('Make QRcode')
    window.mainloop()

if __name__ == '__main__':
    main()
