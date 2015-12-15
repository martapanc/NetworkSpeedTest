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
import speed

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
info.set("\n  DOWNLOAD SPEED\n\n\n UPLOAD SPEED\n\n")
testLabel.pack()

whiteLabel = Label(root)
whiteLabel.pack()

def speedTest():
	transferSizeList=[10, 100, 1000, 10000, 100000, 1000000]
	totalTransferSize=0
	totalTransferTime=0
	fileNum=1
	print "Starting speed test"

	while(fileNum<len(transferSizeList)):
		totalTransferSize+=transferSizeList[fileNum]
   		info.set("\n  DOWNLOAD SPEED\nDone.\n\n UPLOAD SPEED\nUploading file"+str(fileNum)+"...\n")
   		totalTransferTime+=speed.test_upload("162.243.237.100", 8080, transferSizeList[1])
	
   	#implement with tester method, which downloads/uploads the sample files and shows the results
   	#info.set("\n  DOWNLOAD SPEED\nDownloading files...\n\n UPLOAD SPEED\n\n")
   	#speed.test_download()

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
