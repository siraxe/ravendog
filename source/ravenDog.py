import os
import math
import requests
import time
import sys
import re
from bs4 import BeautifulSoup
from colorama import init
init()
from colorama import Fore, Back, Style
import logging
from time import gmtime, strftime
import smtplib

minerPath=os.path.dirname(os.path.abspath(__file__))
setName="settings.txt"
os.system('title RAVENDOG')

#//////////////// LOGO ///////////////////////////
def logoprint():
	rolltime=0.1
	print(Style.BRIGHT+ Fore.GREEN)
	print("________           _      ____     ___ __________ ___      ___________      ____       ____   ")
	time.sleep(rolltime)
	print("`MMMMMMMb.        dM.     `Mb(     )d' `MMMMMMMMM `MM\     `M'`MMMMMMMb.   6MMMMb     6MMMMb/ ")
	time.sleep(rolltime)
	print(" MM    `Mb       ,MMb      YM.     ,P   MM      \  MMM\     M  MM    `Mb  8P    Y8   8P    YM ")
	time.sleep(rolltime)
	print(" MM     MM       d'YM.     `Mb     d'   MM         M\MM\    M  MM     MM 6M      Mb 6M      Y ")
	time.sleep(rolltime)
	print(" MM     MM      ,P `Mb      YM.   ,P    MM    ,    M \MM\   M  MM     MM MM      MM MM        ")
	time.sleep(rolltime)
	print(" MM    .M9      d'  YM.     `Mb   d'    MMMMMMM    M  \MM\  M  MM     MM MM      MM MM        ")
	time.sleep(rolltime)
	print(" MMMMMMM9'     ,P   `Mb      YM. ,P     MM    `    M   \MM\ M  MM     MM MM      MM MM     ___")
	time.sleep(rolltime)
	print(" MM  \M\       d'    YM.     `Mb d'     MM         M    \MM\M  MM     MM MM      MM MM     `M'")
	time.sleep(rolltime)
	print(" MM   \M\     ,MMMMMMMMb      YM,P      MM         M     \MMM  MM     MM YM      M9 YM      M ")
	time.sleep(rolltime)
	print(" MM    \M\    d'      YM.     `MM'      MM      /  M      \MM  MM    .M9  8b    d8   8b    d9 ")
	time.sleep(rolltime)
	print("_MM_    \M\__dM_     _dMM_     YP      _MMMMMMMMM _M_      \M _MMMMMMM9'   YMMMM9     YMMMM9  ")
	print(Style.RESET_ALL)
#Get minetpath
#//////////////// READ FILE FUNCTION //////////////////// 
def readFile():
	try:
		fp = open( minerPath + "\\" + setName , 'r', encoding="UTF-8") # open file on read mode
		allLines = fp.read().split("\n") # create a list containing all lines
		fp.close() # close file
		return (allLines)
	except:		# If settings are not found
		print("settings.txt - NOT FOUND")
		time.sleep(2)
		sys.exit()

#//////////////// GET SETTINGS INFO //////////////////// 
def getConfig():
	settingsInfo=readFile()
	global MinerAbsPaths_bat
	global GPU_NR
	global retry_sec
	global minerList
	global valATM
	global cheese

	global use_email
	global sender_email
	global recipient_email
	global password_email
	cheese = False
	### Get miners
	for eachLine in settingsInfo:
		if " RTEsqHCxn2HvMjstsr3VRqLuurjZseNCrE" in eachLine:	#find miners list line nymber
			cheese=True	
		elif "minerList:" in eachLine:	#find miners list line nymber
			minerLine=settingsInfo.index(eachLine)
		elif "GPU_checkNR:" in eachLine:
			GPU_NRLine=settingsInfo.index(eachLine)
			GPU_NR=(settingsInfo[GPU_NRLine].replace("GPU_checkNR:", "")).replace(" ","")
		elif "retry_sec:" in eachLine:
			retry_secLine=settingsInfo.index(eachLine)
			retry_sec=int((settingsInfo[retry_secLine].replace("retry_sec:", "")).replace(" ",""))
		### EMAIL
		elif "sendEmail:" in eachLine:
			use_email_L=settingsInfo.index(eachLine)
			use_email=(settingsInfo[use_email_L].replace("sendEmail:", "")).replace(" ","")
		elif "sender:" in eachLine:
			sender_email_L=settingsInfo.index(eachLine)
			sender_email=(settingsInfo[sender_email_L].replace("sender:", "")).replace(" ","")
		elif "recipient:" in eachLine:
			recipient_email_L=settingsInfo.index(eachLine)
			recipient_email=(settingsInfo[recipient_email_L].replace("recipient:", "")).replace(" ","")
		elif "password:" in eachLine:
			password_email_L=settingsInfo.index(eachLine)
			password_email=(settingsInfo[password_email_L].replace("password:", "")).replace(" ","")

	### Check if donation wallet is in place
	if cheese==False:
		print("Where is my cheese human ? KAAAW !")
		time.sleep(2)
		sys.exit()
	### Check if there are miners
	if minerLine==None:		
		sys.exit("No miners found")
	else:
		minerList=(settingsInfo[minerLine].replace("minerList:", "")).replace(" ","")
		minerList=minerList.split(",")
		minerCount=len(minerList)

	### Find miners paths in the list
	MinerAbsPaths_bat=[]
	try:
		for root, dirs, files in os.walk(minerPath):
			for file in files:
				tempFile=file
				if tempFile in minerList:
					mX = (os.path.join(root, file))
					MinerAbsPaths_bat.append(mX)
		if len(MinerAbsPaths_bat)==1:
			print("Found - " + str(minerList[0]))
			valATM=minerList[0]
		else:
			print("No - "+str(minerList[0])+" found!")
			sys.exit()

	except:
		print("oops , I mean... KAAAW!")
		time.sleep(2)
		sys.exit()

#//////////////// SEND EMAIL NOTIFICATION //////////////////// 
def email_notify():
	if use_email=="True":
		subject = ("MINER RESTARTED ["+ minerList[0]+"]")
		text = ("Your miner ["+ minerList[0] +"] has restarted")

		try:
			smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
			smtp_server.login(sender_email, password_email)
			message = "Subject: {}\n\n{}".format(subject, text)
			smtp_server.sendmail(sender_email, recipient_email, message)
			smtp_server.close()
			print("Email sent !")
		except:
			print("Error! Email not sent !")

#//////////////// GET CLOCK SPEED //////////////////// 
def clockSpeed():
	global gpuMhz
	nvpath="C:\\Program Files\\NVIDIA Corporation\\NVSMI"
	os.chdir(nvpath)
	clockLine=str(os.popen('nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader --id='+str(GPU_NR)).read())
	gpuMhz=int(clockLine[:-2])

#//////////////// GET RAVEN NET HASH //////////////////// 
def ravenHash():
	try:
		global raven_hash
		global raven_diff
		link = ("http://threeeyed.info/api/getnetworkhashps")
		linkD = ("http://threeeyed.info/api/getdifficulty")

		raven_info = requests.get(link)
		raven_diff_info = requests.get(linkD)

		raven_info = (raven_info.text).split(".") # create a list containing all lines
		raven_diff_info = (raven_diff_info.text).split(".") # create a list containing all lines

		raven_hash=round(float(int(raven_info[0])*0.000000001),2)
		raven_diff=raven_diff_info[0]
	except:
		raven_hash="unknown"
		raven_diff="unknown"

#### COMBINE GET INFO INTO ONE LINE ##################
def getAllInfo():
	clockSpeed() # Get GPU Clock atm
	ravenHash()

#### START MINER FUNC ##################
def openMiner(minerName):
	minerLoc=MinerAbsPaths_bat[0].replace(minerName,"")
	os.chdir(minerLoc) # Miner location
	os.startfile(minerName) # Miner file

#### STOP MINER FUNC ##################
def stopMiner(curMiner):
	global miner_w
	miner_w=curMiner[:-4]
	os.system("taskkill /FI "+'"WINDOWTITLE eq "'+miner_w+" /T /F"+" >NUL 2>&1") # kill miner
#### MINER INFO FUNC ##################
def infoPrintLine():
	getAllInfo()
	ravenInfo=" [NETHASH - " + str(raven_hash) +" Gh/s]"
	ravenInfo_D=" [DIFF - " + str(raven_diff) +"]"
	print("[LOAD "+ str(gpuMhz) + "%]"+ ravenInfo + ravenInfo_D)

##### BODY #####
def getTime():
	global cDate
	cDate=(time.strftime('%m/%d/%Y %H:%M:%S')) #get date

getTime()
#//////////////// LOGGING BODY ///////////////////
logDate=cDate.replace(":","-")
logDate=logDate.replace("/","_")
logDate=("RAVENDOG_" + logDate.replace(" ","_") + ".log")

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler(logDate, 'a'))
print = logger.info


##### FIRST START #####
getConfig()#Get settings
getAllInfo()#Get Net Hash and gpu clock
# START MESSAGE
logoprint()

print('\n')
print(Style.BRIGHT+ Fore.GREEN + " RAVENDOG started at [" + cDate+"]"+ Style.RESET_ALL)
openMiner(minerList[0])
print('\n')

time.sleep(10)#EXTRA TIME TO heat up

try:
	while True:
		time.sleep(retry_sec)
		infoPrintLine()#Print info
		time.sleep(2)

		if int(gpuMhz) <=15:
			time.sleep(3)
			clockSpeed()
			if int(gpuMhz) <=15:
				stopMiner(minerList[0])
				getTime()
				print (Style.BRIGHT+ Fore.YELLOW + "Restarting miner[" + cDate+"]" + Style.RESET_ALL)
				email_notify()#SEND EMAIL NOTIFICATION IF TRUE
				print('\n')

				time.sleep(3)
				openMiner(minerList[0])
				time.sleep(15)#EXTRA TIME TO heat up
except:
	getTime()
	print (Style.BRIGHT+ Fore.YELLOW + "Something went wrong KAAAAAWWW ! [" + cDate+"]" + Style.RESET_ALL) 
