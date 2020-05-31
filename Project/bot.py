# Display Entry in a Label
import os
from tkinter import * 
import script
root = Tk()
 
def returnEntry(arg=None):

    """Gets the result from Entry and return it to the Label"""
    file = open("history.txt","w+")
    result = myEntry.get()
    
    script.main(result)
    resultLabel.config(text=file.read(),font=("Arial",16))
    os.remove("history.txt")
    
    
    myEntry.delete(0,END)
 
# Create the Entry widget
myEntry = Entry(root, width=300,font=("Fira Code",16))
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()
 
# Create the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry)
enterEntry.pack(fill=X)
 
# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)
 
 
root.geometry("350x100+750+400")
root.title("BotChat")
 
root.mainloop()