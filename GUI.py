from Tkinter import *
import Tkinter
import ttk
import tkMessageBox
import speed

#Initialize GUI
root = Tk()
root.title("Network Speed Testing Tool")

def showInfo():
	tkMessageBox.showinfo( "Info", "College of Charleston 2015\nCSCI 440 - Computer Networks\nFinal Project: Network Speed Testing Tool")

def showAbout():
	tkMessageBox.showinfo( "About Us", "Developers:\n- Aaron Allsbrook\n- Marta Pancaldi\n- Matt Piazza")

def speedTest():
	host="162.243.237.100"
	transferSizeList=[10, 100, 1000, 10000, 100000, 1000000]
	totalTransferSize=0
	totalTransferTime=0
	fileNum=0
	
	#progress bars
	uploadPB=ttk.Progressbar(uploadPBLabel, orient="horizontal", length= 100, mode="determinate", value=0, maximum=len(transferSizeList))
	downloadPB=ttk.Progressbar(downloadPBLabel, orient="horizontal", length= 100, mode="determinate", value=0, maximum=len(transferSizeList))
	
	print "Starting speed test"
	uploadPB.pack()
	downloadPB.pack()
	while(fileNum<len(transferSizeList)):
		totalTransferSize+=transferSizeList[fileNum]

   		upload.set("\n  UPLOAD SPEED\nUploading file #"+str(fileNum+1)+"...\n")
   		#totalTransferTime+=speed.test_upload(host, 8080, transferSizeList[fileNum])
   		fileNum += 1
   		uploadPB["value"]+=1
   		



#GUI
#menubar
menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label="Info", command=showInfo)
menu.add_command(label="About Us", command=showAbout)
menubar.add_cascade(label="Menu", menu=menu)

#label strings
text = Text(root)
intro = StringVar()
download = StringVar()
upload= StringVar()
results = StringVar()

whiteLabel = Label(root, width=65)
whiteLabel.pack()

introLabel = Label( root, textvariable=intro, width=55, bg="gray85", relief=RAISED, font=("Arial", 18) )
intro.set("\n  Welcome to Network Speed Testing Tool! \n\n  This program will download and upload some sample files \n  to test how fast your connection is.\n")
introLabel.pack()

whiteLabel = Label(root)
whiteLabel.pack()

downloadLabel = Label (root, textvariable=download, width=55, bg="gray85", anchor="w", relief=FLAT, font=("Arial", 16))
download.set("  DOWNLOAD SPEED")
downloadLabel.pack()

downloadPBLabel = Label (root, width=55, bg="gray85", anchor="w", relief=FLAT, font=("Arial", 16))
downloadPBLabel.pack();

uploadLabel = Label (root, textvariable=upload, width=55, bg="gray85", anchor="w", relief=FLAT, font=("Arial", 16))
upload.set("  UPLOAD SPEED")
uploadLabel.pack()

uploadPBLabel = Label (root, width=55, bg="gray85", anchor="w", relief=FLAT, font=("Arial", 16))
uploadPBLabel.pack();

whiteLabel = Label(root)
whiteLabel.pack()

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
