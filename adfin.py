#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "############################################"
	Space(9); print "#       +++ Admin Panel Finder v.1 +++     #"
	Space(9); print "#           == Script by L1nUx3R ==        #"
	Space(9); print "#                  ||D45H7||               #"
        Space(9); print "#                  Thanks To :             #"
        Space(9); print "#    Mrc3nd0l||Mr.Red||D45H7||MR.B1GSMOK3  #"
        Space(9); print "#     =================================    #"
        Space(9); print "#        ++ Jangan Di recode Goblok ++     #"
        Space(9); print "#           ======+==+======+======        #"
        Space(9); print "############################################"

Credit()
findAdmin()
