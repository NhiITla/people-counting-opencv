#!/usr/bin/python
import Tkinter as tk
import os
import tkFileDialog
import subprocess
#from people_counter import *#totalUp,totalDown 


root = tk.Tk()
root.title('People counting')
root.geometry('400x500')




########goi ham call
def webcam():
		os.system('python3 people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt \--model mobilenet_ssd/MobileNetSSD_deploy.caffemodel \--output output/webcam_output.avi')
		global c
		c = tk.Label(root, text="\n\n People counting from webcam\n",fg="green")
		c.pack()
		with open("test.out", "r") as f:
			global read
			read =tk.Label(root, text=f.read(),fg="red")
			read.pack()
		os.remove("test.out")
		
###################################################
a = tk.Label(root, text="\n ")
a.pack()
NewWinButton = tk.Button(root, text='From webcam', command=webcam)
NewWinButton.pack()

##########################################3

def video():
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
	if file != None:
		data = file.read()
		
		#print "I got %d bytes from this file." % len(data)
		name = os.path.basename(file.name)
		#print "I got file name "+name
		file.close()
		global c
		c = tk.Label(root, text="\n People counting from file: "+name+"\n\n",fg="green")
		c.pack()
		#lay name dem vao goi ham call
		os.system('python3 people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt \--model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/'+name+' \--output output/output_001.avi')
		global read
		with open("test.out", "r") as f:
			read =tk.Label(root, text=f.read(),fg = "red")
			read.pack()
		
		os.remove("test.out")
		##### hien thi 
		#output = subprocess.check_output(cmd)
		#print('>', output)
		#result['text'] = output.decode('utf-8')
##############################################################
a = tk.Label(root, text="\n ")
a.pack()
NewWinButton2 = tk.Button(root, text='From input video', command=video)
NewWinButton2.pack()





label = tk.Label( root, text="\nType q to exit ! ",fg = "darkblue",font = "Verdana 10 bold" )

label.pack()

b = tk.Label(root, text="\n ")
b.pack()
##############################
def clear():
	
	read.pack_forget()
	c.pack_forget()
	


NewWinButton3 = tk.Button(root, text='Clear',command=clear)
NewWinButton3.pack()

##############################################



#result = tk.Label(root)
#result.pack()

root.mainloop()

