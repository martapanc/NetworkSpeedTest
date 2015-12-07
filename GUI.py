#!/usr/bin/python

#import Tkinter
#top = Tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()


#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from Tkinter import *
import Tkinter
import tkMessageBox

root = Tk()
root.title("Network Speed Testing Tool")

def showInfo():
	tkMessageBox.showinfo( "Info", "College of Charleston 2015\nCSCI 440 - Computer Networks\nFinal Project: Network Speed Testing Tool")

def showAbout():
	tkMessageBox.showinfo( "About Us", "Developers:\n- Aaron Allsbrook\n- Marta Pancaldi\n- Matt Piazza")
menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Info", command=showInfo)
menu.add_command(label="About Us", command=showAbout)
menubar.add_cascade(label="Menu", menu=menu)

text = Text(root)
intro = StringVar()
info = StringVar()
results = StringVar()

whiteLabel = Label(root, width=65)
whiteLabel.pack()

introLabel = Label( root, textvariable=intro, width=55, bg="gray85", relief=RAISED, font=("Arial", 18) )
intro.set("\n  Welcome to Network Speed Testing Tool! \n\n  This program will download and upload some sample files \n  to test how fast your connection is.\n")
introLabel.pack()

whiteLabel = Label(root)
whiteLabel.pack()

testLabel = Label (root, textvariable=info, width=55, bg="gray85", anchor="w", relief=RAISED, font=("Arial", 16))
info.set("\n  DOWNLOAD SPEED\n  Downloading sample file... 		\n\n  UPLOAD SPEED\n  Uploading sample file... 	 	 \n")
testLabel.pack()

whiteLabel = Label(root)
whiteLabel.pack()

def speedTest():
   print "Starting speed test"
   #implement with tester method, which downloads/uploads the sample files and shows the results

startB = Tkinter.Button(root, text =" Start test ", command = speedTest)
startB.pack()

whiteLabel = Label(root)
whiteLabel.pack()

resultLabel = Label (root, textvariable=results, width=55, bg="gray85", anchor="w", relief=RAISED, font=("Arial", 16))
results.set("\n  TEST RESULTS\n  Test #1...\n")
resultLabel.pack()

whiteLabel = Label(root)
whiteLabel.pack()

root.config(menu=menubar)
root.mainloop()
