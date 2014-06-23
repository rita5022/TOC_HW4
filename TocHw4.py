# -*- coding:utf8 -*-
# TocHw4:Scan the JSON file fron url and find out which road in a city has house trading records spread in #max_distinct_month”. 
		#And print out the roads name and their cities with their highest sale price and lowest sale price. 
		#Note that the answer may contain several roads.
#Example:python TocHw4.py http://www.datagarage.io/api/538447a07122e8a77dfe2d86

# Name:蘇容德
# Student Number:F74001218

import json
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if(len(sys.argv)==2):
	url = sys.argv[1]
	response = urllib2.urlopen(url)
	data = json.load(response)

	road = [] #存有"哪些路"
	roadget = u""
	
	trade_year = []
	count_year = []
	trade_money = []
	max_money = []
	min_money = []	
	ID = []

	#data_len = len(data)
	count = 0
	most_trade = 0
	
	
	while count < len(data):
		if data[count][u"土地區段位置或建物區門牌"].find(u"大道")!=-1 and data[count][u"土地區段位置或建物區門牌"].find(u"大道")+2!=data[count][u"土地區段位置或建物區門牌"].find(u"路"): #避免有"大道路"的產生
			pos = data[count][u"土地區段位置或建物區門牌"].find(u"大道") #關鍵字出現的位置
			if pos > 0: #關鍵字非第一個
				roadget = data[count][u"土地區段位置或建物區門牌"][0:pos+2]

		elif data[count][u"土地區段位置或建物區門牌"].find(u"路")!=-1 and data[count][u"土地區段位置或建物區門牌"].find(u"路")+2!=data[count][u"土地區段位置或建物區門牌"].find(u"區"):
			pos = data[count][u"土地區段位置或建物區門牌"].find(u"路")
			if pos > 0: 
				roadget = data[count][u"土地區段位置或建物區門牌"][0:pos+1]

		elif data[count][u"土地區段位置或建物區門牌"].find(u"街")!=-1:
			pos = data[count][u"土地區段位置或建物區門牌"].find(u"街")
			if pos > 0: 
				roadget = data[count][u"土地區段位置或建物區門牌"][0:pos+1]

		elif data[count][u"土地區段位置或建物區門牌"].find(u"巷")!=-1:
			pos = data[count][u"土地區段位置或建物區門牌"].find(u"巷")
			if pos > 0: 
				roadget = data[count][u"土地區段位置或建物區門牌"][0:pos+1]

		else:
			roadget = u""


		if cmp(roadget,u"")!=0:	 
			if road.count(roadget)==0:
				road.append(roadget)
		count = count + 1
	#print len(road)
	#for each_road in range(len(road)):
	#	print road[each_road]


	for addr in range(len(road)): #掃每一個需被比對的比對的addr
		del trade_year [:] #暫存有哪些交易年月的lis要被t清空,每個地址要重來
		del trade_money [:] #暫存所有交易總價元的listlist清空重來
		for all_addr in range(len(data)): #掃全部的資料
			if data[all_addr][u"土地區段位置或建物區門牌"].find(road[addr])!=-1: #比對地址 
				year = data[all_addr][u"交易年月"]				
				if(trade_year.count(year)==0):
					trade_year.append(year)

				money = data[all_addr][u"總價元"]
				trade_money.append(money)

		count_year.append(len(trade_year))
		max_money.append(max(trade_money))
		min_money.append(min(trade_money))
	
	
	most_trade = max(count_year) #最大交易次數
	for num in range(len(count_year)):
		if most_trade==count_year[num]:
			ID.append(num)

	
	for a in range(len(ID)):
		print road[ID[a]]+", 最高成交價: "+str(max_money[ID[a]])+", 最低成交價: "+str(min_money[ID[a]])
		#print road[ID[a]],
		#print ", 最高成交價: ",
		#print max_money[ID[a]],
		#print ", 最低成交價: ",
		#print min_money[ID[a]]

else:
	print "The number of input argument is wrong"

