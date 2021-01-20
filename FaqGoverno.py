#!/usr/bin/python3


from platform import system as platform_name
import urllib.request
import time;
from os import system
import ctypes


def apri_cd():
	if platform_name() in platforms_dictionary:
		exec(platforms_dictionary[platform_name()]["open"])
	else:
		print("Caro amico, non riesco ad aprire il vano disco")


def chiudi_cd():
	if platform_name() in platforms_dictionary:
		exec(platforms_dictionary[platform_name()]["close"])
	else:
		print("Caro amico, non riesco a chiudere il vano disco")



platforms_dictionary = {
    "Windows": {                              #
                "open" : 'ctypes.windll.WINMM.mciSendStringW(u"open E: type CDAudio alias E_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set E_drive door open", None, 0, None)',
                "close": 'ctypes.windll.WINMM.mciSendStringW(u"open E: type CDAudio alias E_drive", None, 0, None); ctypes.windll.WINMM.mciSendStringW(u"set E_drive door closed", None, 0, None)'
               },
    "Darwin":  {
                "open" : 'system("drutil tray open")',
                "close": 'system("drutil tray closed")'
               },
    "Linux":   {
                "open" : 'system("eject cdrom")',
                "close": 'system("eject -t cdrom")'
               },
    "NetBSD":  {
                "open" : 'system("eject cd")',
                "close": 'system("eject -t cd")'
               },
    "FreeBSD": {
                "open" : 'system("sudo cdcontrol eject")',
                "close": 'system("sudo cdcontrol close")'
               }
}



while True:
	localtime = time.asctime( time.localtime(time.time()) )
	fp = urllib.request.urlopen("http://www.governo.it/it/articolo/domande-frequenti-sulle-misure-adottate-dal-governo/15638")
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	if "LA SEZIONE FAQ È ATTUALMENTE IN AGGIORNAMENTO IN SEGUITO ALL’ENTRATA IN VIGORE DEI CITATI DECRETI. LE RISPOSTE QUI RIPORTATE SONO RELATIVE ALLE DISPOSIZIONI IN VIGORE FINO ALLO SCORSO 15 GENNAIO" in mystr:
		print(localtime + "   ancora nulla")
	else:
		print(localtime + "   AGGIORNATOOOOOOOOOOOOOOOOOOOOOOO")
		for i in range(12):
			apri_cd()
			time.sleep(4)
			chiudi_cd()
			time.sleep(4)
	time.sleep(60)

