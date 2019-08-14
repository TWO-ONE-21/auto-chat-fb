#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Ardo Rianda
#eh mau ngapain? mau recode ya? tinggal pake apa susahnya sih. Hargai usaha org, cape2 ngoding, ujung2nya di recode. recode = kencing nanah :v

import mechanize
import re,time,os,sys
br = mechanize.Browser()
os.system('color')

class warna:
	merah = '\033[31m'
	hijau = '\033[32m'
	kuning = '\033[33m'
	biru = '\033[34m'

br = 0
IdTeman = []
email = ''
password = ''

def membuka(link):
	try:
		x = br.open(link)
		br._factory.is_html = True
		x = x.read()
	except:
		print warna.merah + "Periksa koneksi internet anda"
		sys.exit()
	if '<link rel="redirect" href="' in x:
		return membuka(br.find_link().url)
	else:
		return x

def loading():
	for i in range(33, 100, 33):
		time.sleep(0.5)
		print warna.kuning + 'LOADING... ' + '[' + str(i) + '%' + ']'

import cookielib,re,urllib2,urllib,threading

def browser():
	global br
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_cookiejar(cookielib.LWPCookieJar())
	br.set_handle_redirect(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
	br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def ulangi():
	ulang = raw_input(warna.biru + "Apakah anda ingin mencoba login kembali?[y/n] " + warna.kuning)
	ulang = ulang.upper()
	if ulang == 'Y':
		os.system('cls')
		return masuk()
	elif ulang != 'Y' and ulang != 'N':
		print warna.merah + 'TEKAN ' + warna.biru + '[y]' + warna.merah + ' UNTUK MENCOBA LAGI, ATAU TEKAN ' + warna.biru + '[y]' + warna.merah + ' UNTUK MEMBATALKAN!!!'
		return ulangi()
	else:
		sys.exit()

def id_terkumpul(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		IdTeman.append(i)

def masuk():
	email = raw_input(warna.hijau + 'Email: ' + warna.kuning)
	password = raw_input(warna.hijau + 'Password: ' + warna.kuning)
	loading()
	membuka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email'] = email
	br.form['pass'] = password
	time.sleep(7)
	br.submit()
	link = br.geturl()
	if 'save-device' in link:
		membuka('https://mobile.facebook.com/home.php')
		print warna.hijau + '\nBerhasil Masuk'
	elif 'checkpoint' in link:
		print warna.merah + 'Akun anda terkena checkpoint,\nHarap login dan mengkonfirmasikan identitas anda\nmelalui opera mini'
		ulangi()
	else:
		print warna.merah + 'Email/Password anda salah'
		ulangi()

def id():
	print warna.kuning + '\nMengumpulkan id teman...'
	membuka('https://m.facebook.com/friends/center/mbasic/?fb_ref=bm&sr=1&ref_component=mbasic_bookmark&ref_page=XMenuController')
	id_terkumpul(membuka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	next = br.find_link(url_regex='friends_center_main').url
	try:
		next
	except:
		if len(IdTeman) != 0:
			print warna.hijau + '\nBerhasil mengumpulkan' + warna.kuning + str(len(IdTeman)) + warna.hijau + " ID Teman"
		else:
			sys.exit()
	while 1:
		id_terkumpul(membuka(next))
		print warna.biru + str(len(IdTeman)) + warna.hijau + ' ID terambil'
		sys.stdout.flush()
		try:
			next = br.find_link(url_regex='friends_center_main').url
		except:
			print warna.kuning + '\nBerhasil mengumpulkan ' + warna.merah + str(len(IdTeman)) + warna.kuning + ' ID Teman'
			break
	if len(IdTeman) != 0:
		print warna.kuning + "\nMenyimpan ID teman"
		File = 0
		try:
			open(os.sys.path[0]+'/id_terkumpul.txt','w').write('\n'.join(IdTeman))
			print warna.hijau + '\nBerhasil menyimpan ID teman'
			File += 1
		except:
			print warna.merah + '\nGagal menyimpan'
		if File == 1:
			chat()
		else:
			sys.exit()

def chat():
	try:
		teman = open(os.sys.path[0]+'/id_terkumpul.txt','r')
	except:
		print '\n' + warna.merah + 'Anda belum mengumpulkan ID,\nHarap kumpulkan ID terlebih dahulu!!!\n'
		return id()
	idteman = teman.readlines()
	teman.close()
	pesan = raw_input(warna.hijau + 'Ketikkan Pesan Anda: ' + warna.kuning) + '\nDikirimkan melalui auto-chat-fb.\ngithub.com/TWO-ONE-21/auto-chat-fb'
	print '\n'
	terkirim = 0
	for i in idteman:
		ID_teman = i.strip("\n")
		membuka("https://mbasic.facebook.com/messages/thread/" + ID_teman)
		try:
			br.select_form(nr=1)
		except:
			continue
		br.form['body'] = pesan
		br.submit()
		terkirim += 1
		print warna.merah + str(terkirim) + warna.hijau + ' chat telah terkirim'

def cover():
	print warna.hijau + " ____  _     _____  ____               |\ |\ \n/  _ \/ \ /\/__ __\/  _ \CHAT          \ \| |\n| / \|| | ||  / \  | / \|               \ | |\n| |-||| \_/|  | |  | \_/|             .--''/\n\_/ \|\____/  \_/  \____/FACEBOOK    /o     \ \n                                     \      /\n===================================== {>o<}='",'\n'
	print warna.kuning + "+=========================================+\n|..........."+warna.merah + "AUTO CHAT FACEBOOK" + warna.kuning + "............|\n+-----------------------------------------+\n|#Github: https://github.com/TWO-ONE-12   |\n|#Contact: www.facebook.com/controI.panel |\n|#From: Bukittinggi, Sumatera Barat       |\n|#Date: 09 August 2019                    |\n|#Tool ini berguna untuk mengirim         |\n| chat ke semua friendlist anda secara    |\n| otomatis :v                             |\n|                                         |\n|#SORRY GAN, KODE AGAK BERANTAKAN, ANE    |\n| MASIH PEMULA H3H3 :Voss                 |\n+=========================================+\n|..............." + warna.merah+"ARDO RIANDA" + warna.kuning + "...............|\n+-----------------------------------------+\n"
	print warna.merah + 'NB: LU BISA AJA DAPETIN NOMER WA DIA.\n    TAPI TIDAK UNTUK MENDAPATKAN HATINYA :")\n'

def pilih():
	pilihan = raw_input(warna.biru+"Apakah anda telah mengumpulkan ID teman anda sebelumnya?? [y/n] " + warna.kuning)
	pilihan = pilihan.upper()
	if pilihan == 'Y':
		chat()
	elif pilihan != 'Y' and pilihan != 'N':
		print (warna.merah + "HARAP MEMASUKKAN PILIHAN YANG BENAR!!!")
		return pilih()
	else:
		id()

browser()
cover()
masuk()
pilih()
