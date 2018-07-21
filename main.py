from bs4 import BeautifulSoup
import requests
import csv
"""
Hello. This scipt outputs a .csv file with a data of all european schools from
https://www.iss.edu/Resources-Center/schools-explore-list/Schools-by-Region/Schools-in-Europe-Eastern-Europe
Result may have something like 'https://' in a site cell, but this happens due to the bad formatting of iss.edu
"""

csvObj = open('log.csv', 'w', newline='') #Or do csvObj = open('log.xlsx', 'w', newline='')
writer = csv.writer(csvObj)#And writer = csv.writer(csvObj, dialect='excel') to create an Excel table instead
writer.writerow(['Site', 'Name', 'Country', 'Enrollment', 'Curriculum', 'SchoolYear', 'Founded', 'AvgClassSize', 'Clubs', 'Campus'])
def parseDetail(url):
	html = requests.get(url)
	bs = BeautifulSoup(html.text, 'lxml')

	try:
		site = bs.find('div', class_ = 'location_website').find('a').attrs['href']
		print(site)
	except AttributeError:
		site = 'None'
	try:
		name = bs.find('div', id = 'container_name').find('div', class_ = 'field').getText().strip()
		print(name)
	except AttributeError:
		name = 'None'
	try:
		country = bs.find('div', id = 'container_country').find('div', class_ = 'field').getText().strip()
		print(country)
	except AttributeError:
		country = 'None'
	try:
		enrollment = bs.find('div', id = 'container_enrollment').find('div', class_ = 'field').getText().strip()
		print(enrollment)
	except AttributeError:
		enrollment = 'None'
	try:
		curriculum = bs.find('div', id = 'container_curriculum').find('div', class_ = 'field').getText().strip()
		print(curriculum)
	except AttributeError:
		curriculum = 'None'
	try:
		schoolYear = bs.find('div', id = 'container_school_year').find('div', class_ = 'field').getText().strip()
		print(schoolYear)
	except AttributeError:
		schoolYear = 'None'
	try:
		founded = bs.find('div', id = 'container_year_founded').find('div', class_ = 'field').getText().strip()
		print(founded)
	except AttributeError:
		founded = 'None'
	try:
		avgClassSize = bs.find('div', id = 'container_average_class_size').find('div', class_ = 'field').getText().strip()
		print(avgClassSize)
	except AttributeError:
		avgClassSize = 'None'

	try:
		clubs = bs.find('div', id = 'container_clubs').find('div', class_ = 'field').getText().strip()
		print(clubs)
	except AttributeError:
		clubs = 'None'

	try:
		campus = bs.find('div', id = 'container_campus_information').find('div', class_ = 'field').getText().strip()
		print(campus)
	except AttributeError:
		campus = 'None'

	try:
		writer.writerow([site, name, country, enrollment, curriculum, schoolYear, founded, avgClassSize, clubs, campus])
	except UnicodeEncodeError:
		pass


def parse():
	html = requests.get('https://www.iss.edu/Resources-Center/schools-explore-list/Schools-by-Region/Schools-in-Europe-Eastern-Europe')
	bs = BeautifulSoup(html.text, 'lxml')
	divs = bs.find('div', id = '115C').findAll('p')
	for p in divs:
		schoolUrl = p.find('a').attrs['href']
		parseDetail(schoolUrl)


parse()
csvObj.close()


#http://water.epa.state.il.us/dww/JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=null&begin_date=6%2F26%2F2016&end_date=6%2F26%2F2018&action=Search+For+Water+Systems
