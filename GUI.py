from Tkinter import *
import Tkinter
import ttk
import tkMessageBox
import speed
import time

#Initialize GUI
root = Tk()
root.title("Network Speed Testing Tool")

running= True 

def showInfo():
	tkMessageBox.showinfo( "Info", "College of Charleston 2015\nCSCI 440 - Computer Networks\nFinal Project: Network Speed Testing Tool")

def showAbout():
	tkMessageBox.showinfo( "About Us", "Developers:\n- Aaron Allsbrook\n- Marta Pancaldi\n- Matt Piazza")

def stop():
	global running
	running=False

def speedTest():
	global running
	host="162.243.237.100"
	transferSizeList=[10, 100, 1000, 10000, 100000, 1000000]
	totalTransferSize= sum(transferSizeList)
	totalULTransferTime=0
	totalDLTransferTime=0
	fileNum=0
	button1.pack_forget()
	
	#set button 1 to Stop test 
	button1["command"]= stop 
	button1["text"]="Stop"
	button1.pack()

	button2 = Tkinter.Button(root, text =" Reset ", command = speedTest)
	button2.pack()

	#progress bars
	uploadPB=ttk.Progressbar(uploadPBLabel, orient="horizontal", length= 200, mode="determinate", value=0, maximum=totalTransferSize)
	downloadPB=ttk.Progressbar(downloadPBLabel, orient="horizontal", length= 200, mode="determinate", value=0, maximum=totalTransferSize)
	
	print "Starting speed test"
	time.sleep(1)
	downloadPB.pack()
	while(fileNum<len(transferSizeList) and running):
		
   		download.set("\n  DOWNLOAD SPEED\nDownloading file #"+str(fileNum+1)+"...\n")
   		totalDLTransferTime+=speed.test_download(host, 8080, transferSizeList[fileNum])
   		downloadPB["value"]+=transferSizeList[fileNum]
   		fileNum += 1
   	
   		
   	download.set("\n  DOWNLOAD SPEED\n {0:.2f} Mbps\n".format((totalTransferSize/totalDLTransferTime/1000000)*8)) 

   	fileNum=0
	uploadPB.pack()
   	while(fileNum<len(transferSizeList) and running):
		totalTransferSize+=transferSizeList[fileNum]
   		upload.set("\n  UPLOAD SPEED\nUploading file #"+str(fileNum+1)+"...\n")
   		totalULTransferTime+=speed.test_upload(host, 8080, transferSizeList[fileNum])
   		uploadPB["value"]+=transferSizeList[fileNum]
   		fileNum += 1

   	upload.set("\n  UPLOAD SPEED\n {0:.2f} Mbps\n".format(((totalTransferSize/totalULTransferTime/1000000)*8))) 

   	button1["text"]= "Test Again"
   	button1["command"]= speedTest

   	button2.pack_forget()
   	uploadPB.pack_forget()
   	downloadPB.pack_forget()


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

button1Label= Label(root, width=55, bg="gray85", anchor="w", relief=FLAT)
button1Label.pack()
button2Label= Label(root, width=55, bg="gray85", anchor="w", relief=FLAT)
button2Label.pack()

button1 = Tkinter.Button(button1Label, text =" Start test ", command = speedTest)
button1.pack()

whiteLabel = Label(root)
whiteLabel.pack()

resultLabel = Label (root, textvariable=results, width=55, bg="gray85", anchor="w", relief=RAISED, font=("Arial", 16))
results.set("\n  TEST RESULTS\n  Test #1...\n")
resultLabel.pack()

whiteLabel = Label(root)
whiteLabel.pack()

root.config(menu=menubar)
root.mainloop()
