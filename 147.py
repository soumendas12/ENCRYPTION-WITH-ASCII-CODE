from tkinter import *

root = Tk()
root.title("ENCRYPTION WITH ASCII CODE")

root.geometry("400x400")
root.configure(background = 'lightblue1')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root,  text = "Name in ASCII : ", bg="light cyan", fg="black")
label2 = Label(root,  text = "Enctypted Name : ", bg="light cyan", fg="black")

def asciiConverter():
   input_word = str(enter_word.get())

   for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter)) + " "
        encrypted = ascii - 1
        label2["text"] += str(chr(enctypted))

btn = Button(root,text="Display the Ascii Code and Encrypted value", command = asciiConverter, bg = 'blue', fg= 'black')
btn.place(relx=0.5,rely=0.5, anchor = CENTER)

label.place(relx=0.5,rely=0.6,anchor = CENTER)
label2.place(relx=0.5,rely=0.7,anchor = CENTER)

root.mainloop()
from tkinter import *

root = Tk()
root.title("ENCRYPTION WITH ASCII CODE")

root.geometry("400x400")
root.configure(background = 'lightblue1')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root,  text = "Name in ASCII : ", bg="light cyan", fg="black")
label2 = Label(root,  text = "Enctypted Name : ", bg="light cyan", fg="black")

def asciiConverter():
   input_word = str(enter_word.get())

   for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter)) + " "
        encrypted = ascii - 1
        label2["text"] += str(chr(enctypted))

btn = Button(root,text="Display the Ascii Code and Encrypted value", command = asciiConverter, bg = 'blue', fg= 'black')
btn.place(relx=0.5,rely=0.5, anchor = CENTER)

label.place(relx=0.5,rely=0.6,anchor = CENTER)
label2.place(relx=0.5,rely=0.7,anchor = CENTER)

root.mainloop()
