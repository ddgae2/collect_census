#always run python38
#conda activate python38
#!/Users/davidgae/miniconda3/envs/python38/bin/python3 
import numpy as np
import pandas as pd
import csv
import requests
import json
import math 
import zip3
#source:https://www.bls.gov/opub/btn/volume-7/television-capturing-americas-attention.htm

def generation(r):
	#1)always setup variable to use for pandas framework
	renter1 = []
	renter2 = []
	renter3 = []
	house1 = []
	house2 = []
	house3 = []
	population1= []
	population2= []
	population3 = []
	zi1p = []
	zi2p = []
	zi3p = []
	age1 = []
	age2 = []
	age3 = []
	employed = []
	employed_full = []
	employed_part = []
	not_employed  = []
	men = []
	women =[]
	#2) setup the file to open
	file1 = pd.read_csv("Book1.csv")
	#file2 = pd.read_csv("QuickFact_april_29_2022.csv")

	#3) can setup to loops through the file.	
	#file = csv.DictReader(file1)
	#for col in file1.iterrows():
	
	#4)use pandas iloc function to store to variable 
	#zip
	aa = file1.iloc[20]
	a1 = file1.iloc[23]
	b1 = file1.iloc[26]
	c1 = file1.iloc[29]
	bb = file1.iloc[21]
	a2 = file1.iloc[24]
	b2 = file1.iloc[27]
	c2 = file1.iloc[30]
	cc = file1.iloc[22]
	a3 = file1.iloc[25]
	b3 = file1.iloc[28]
	c3 = file1.iloc[31]
	#age
	d1 = file1.iloc[1]
	d2 = file1.iloc[2]
	d3 = file1.iloc[3]
	e = file1.iloc[32]
	f = file1.iloc[33]
	g = file1.iloc[34]
	h = file1.iloc[35]
	#gender
	m = file1.iloc[13]
	n = file1.iloc[14]
	
	#5) create a new data table that is combined into as a new dataframe.
	data1 = {
		"[0]95616": aa[1],
		"[1]population1": a1[1],
		"[2]renter1":  b1[1],
		"[3]house1": c1[1],
		"[4]95618": bb[1],
		"[5]population2": a2[1],
		"[6]renter2":  b2[1],
		"[7]house3": c2[1],
		"[8]95776": cc[1],
		"[9]population3": a3[1],
		"[10]renter3":  b3[1],
		"[11]house3": c3[1]
	     }
	
	data2 = {
		"[0]15-19": d1[1],
		"[1]20-44": d2[1],
		"[2]45-65": d3[1],
		"[3]employed": e[1],
		"[4]employed_full":f[1],
		"[5]employed_part":g[1],
		"[6]not_employed":h[1]}

	data3 = {
		"[0]Men": m[1],
		"[1]Women": n[1]}
	#6) convert data table into dataframe that can be accessed with iloc
	data1 = pd.DataFrame(data1,index=[0,1,2,3,4,5,6,7,8,9,10,11])
	data2 = pd.DataFrame(data2,index=[0,1,2,3,4,5,6])
	data3 = pd.DataFrame(data3,index=[0,1])
	#print(data1.iloc[0,0])
	#7) quick view of the data on the terminal 
	if data1.iloc[0,0] and data2.iloc[0,0]:
			print( "15-19 age group")
			print( "employed",data2.iloc[0,3])
			print( "employed_full",data2.iloc[0,4])
			print( "employed_part",data2.iloc[0,5])
			print( "renter1 95616", data1.iloc[0,2])
			print( "renter2 95618", data1.iloc[0,6])
			print( "renter3 95776", data1.iloc[0,10])
			print('-------------------------------')

	if data1.iloc[0,4] and data2.iloc[0,1]:
			print( "20-44 age group")
			print( "employed",data2.iloc[0,3])
			print( "employed_full",data2.iloc[0,4])
			print( "employed_part",data2.iloc[0,5])
			print( "house_owner1 95616", data1.iloc[0,3])
			print( "house_owner2 95618", data1.iloc[0,7])
			print( "house_owner3 95776", data1.iloc[0,11])
			print('-------------------------------')

	if data1.iloc[0,8] and data2.iloc[0,2]:
			print( "45-65 age group")
			print( "employed",data2.iloc[0,3])
			print( "employed_full",data2.iloc[0,4])
			print( "employed_part",data2.iloc[0,5])
			print( "house_owner1 95616", data1.iloc[0,3])
			print( "house_owner2 95618", data1.iloc[0,7])
			print( "house_owner3 95776", data1.iloc[0,11])
			print('-------------------------------')

	if data1.iloc[0,0]:
			print( "zip 95616, zip 95618, zip 95776")
			print( "not_employed men",data3.iloc[0,0])
			print( "not_employed women",data3.iloc[0,1])
			print('-------------------------------')
	
	#8) convert into json so that can be stored into a json databases
	#result = data1.to_json(orient='table')
	#parsed = json.loads(result)
	#json.dumps(parsed, intent=4)
	print('-------------------------------')
	print('Data Retrieval Complete and "Checked"')
	print('http://www.city-data.com/city/Davis-California.html')
	print('-------------------------------')

	return data1, data2, data3


if __name__ == '__main__':
	r1,r2,r3=generation(1)

