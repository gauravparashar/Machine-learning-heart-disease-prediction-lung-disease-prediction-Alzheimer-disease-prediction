from bs4 import BeautifulSoup
import requests
import random
import time
'''
Global Variables
'''

d_file=open('disease.txt')

diseases_list = d_file.readlines()


'''
Prepare the search string with the start(which is number of results per page ), starting year as_ylo parameter and return complete url

'''
def prepare_search_string(start,as_ylo):
	start = str(start)
	as_ylo = str(as_ylo)
	baseurl = 'https://scholar.google.com/scholar?'
#	parameters="hl=en&as_sdt=0%2C5&q='Machine+Learning'+AND+'heart+disease'&btnG="
	parameters='hl=en&as_sdt=0%2C5&q=healthcare+machine+learning&btnG='
	url = baseurl+'as_ylo'+as_ylo+'&start='+start+'&'+parameters
	return url

'''
get the URL and return the html content
'''
def get_respionse_from_google_scholar(url):
#	timeout = random.randint(1,9)
	print (url)
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12) AppleWebKit/601.3.0 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
	response = requests.get(url,headers=headers)
	soup = BeautifulSoup(response.content,'lxml')
	return soup

'''

'''
diseases = {}
start_year=2017
total_results=0
#
file_raw=open('raw.txt','a')
#
for i in range(0,1000,10):
	soup = get_respionse_from_google_scholar(prepare_search_string(i,start_year))
	print("---------------------------------------------------")
	print(soup)

	for item in soup.select('[data-lid]'):
		try:
#			print('----------------------------------------------------------')
			title=item.select('h3')[0].get_text()
			title=title.lower()
			words = title.split()
			total_results = total_results + 1
			title = title + '\n'
			file_raw.write(title)
			print(title)
			for w in words:
				if w in diseases_list:
					if w in diseases:
						diseases[w]=diseases[w]+1
					else:
						diseases[w]=1

		except Exception as e:
			raise e
#		finally:
	time.sleep(60)

'''
Save the output in the file

'''
file = open('scrap.txt','w')
file.write(str(diseases))
file.close()
file_raw.close()
print('____________________________________________')
print(diseases)
print('total results',total_results)
