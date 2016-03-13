#!/usr/bin/python
#  -*- coding: utf-8 -*-
#  coded by @magic_coding (icoder@mail.com)
#  Twitter: @magic_coding

#For more help please read: https://github.com/magic-coding/shortten-url

import requests
import httplib2
import json

#Add your Goo.gl api key.
Google_API_KEY = ""

#Add your Bit.ly api key.
Bitly_API_KEY = ""

def google():
	longUrl_g = raw_input("longUrl: ")
	try: Google_API_KEY
	except NameError:
		apiUrl = 'https://www.googleapis.com/urlshortener/v1/url'    
	else:
		apiUrl = 'https://www.googleapis.com/urlshortener/v1/url?key=%s' % Google_API_KEY
    
	headers = {"Content-type": "application/json"}
	data = {"longUrl": longUrl_g}
	h = httplib2.Http('.cache')
	try:
		headers, response = h.request(apiUrl, "POST", json.dumps(data), headers)
		short_url = json.loads(response)['id']
		print "|Great work!"
		print "|Short link: "+short_url+"    <==="
		again = raw_input("Short another Link? (y/n): ")
		if again=="y":
			pass
		else:
			print "program exit.."
			print "See you again."
			exit()
	except Exception, e:
		print "[!] unexpected error %s" % e
		google()


def bitly():
	if Bitly_API_KEY:
		longUrl_b = raw_input("longUrl: ")
		query_params = {'access_token': Bitly_API_KEY,'longUrl': longUrl_b} 

		endpoint = 'https://api-ssl.bitly.com/v3/shorten'
		response = requests.get(endpoint, params=query_params, verify=True)

		data = json.loads(response.content)
		status = str(data['status_code'])
		if status=="200":
			print "|Great work!"
			short_link = data['data']['url']
			print "|Short link: "+short_link+"    <==="
			again = raw_input("Short another Link? (y/n): ")
			if again=="y":
				pass
			else:
				print "program exit.."
				print "See you again."
				exit()
		elif status=="403":
			print "[!] Error: RATE LIMIT EXCEEDED. Please try again after 1 hour."
			Error()
		elif status=="503":
			print "[!] Error: TEMPORARILY UNAVAILABLE. Please try again."
			Error()
		elif status=="500":
			print "[!] Error: Please write your url in form with (http://)"
			again = raw_input("Need to try again? (y/n): ")
			if again=="y":
				pass
			else:
				print "See you again."
				bitly()
		else:
			print "[!] Error: UNKNOWN ERROR."
			Error()
	else:
		print "[!] Please add your Bitly API."
		exit()

def Error():
	again = raw_input("Need to try again? (y/n): ")
	if again=="y":
		pass
	else:
		print "program exit.."
		print "See you again."
		exit()

def info():
	print """   _____ __               __                           __
  / ___// /_  ____  _____/ /____  ____     __  _______/ /
  \__ \/ __ \/ __ \/ ___/ __/ _ \/ __ \   / / / / ___/ / 
 ___/ / / / / /_/ / /  / /_/  __/ / / /  / /_/ / /  / /  
/____/_/ /_/\____/_/   \__/\___/_/ /_/   \__,_/_/  /_/\n"""
	print """This program coded by Mahmoud Al-nafei (www.twitter.com/magic_coding)
with Python language and it's free for use.
You can get this programe as open source from my Github account:
www.github.com/magic-coding

Enjoy..
-----
For Help: @magic_coding
	"""
	Enter = raw_input("press (Enter) to go back..")
	if Enter:
		pass

while True:
	print """   _____ __               __                           __
  / ___// /_  ____  _____/ /____  ____     __  _______/ /
  \__ \/ __ \/ __ \/ ___/ __/ _ \/ __ \   / / / / ___/ / 
 ___/ / / / / /_/ / /  / /_/  __/ / / /  / /_/ / /  / /  
/____/_/ /_/\____/_/   \__/\___/_/ /_/   \__,_/_/  /_/

Credit @magic_coding (www.twitter.com/magic_coding)\n"""
	print "1- short url with (goo.gl)"
	print "2- short url with (bit.ly)"
	print "3- about"
	print "4- Exit System"

	decision = input("Please select a number: ")
	if(decision == 1):
		google()
	if(decision == 2):
		bitly()
	if(decision == 3):
		info()
	if(decision == 4):
		print "program exit.."
		print "See you again."
		exit()