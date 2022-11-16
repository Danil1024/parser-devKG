import requests
from bs4 import BeautifulSoup


MAIN_URL = 'https://devkg.com'
KEY_WORDS = ('python','backend', 'django')

def get_jobs():
	for el in range(1, 100):
		print(el)

		url = f'{MAIN_URL}/ru/jobs?page={el}'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		jobs = soup.find('div', class_= 'jobs-list').find_all('article', class_='item')
		for job in jobs:
			yield job

def get_info_job():
	for job in get_jobs():
		if job.find('a', class_='link archived'):
			print(job)
			raise KeyboardInterrupt

		job_position = job.find('div', class_='jobs-item-field position').text\
						.replace('\n', '').replace(' ', '').replace('Должность', '')
		job_url = job.find('a', class_='link').get('href')
		for key_word in KEY_WORDS:
			if key_word in job_position.lower():
				print(job_position, MAIN_URL + job_url, sep='\n' ,end='\n\n\n')

get_info_job()
