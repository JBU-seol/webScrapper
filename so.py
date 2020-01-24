import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {'class': 's-pagination'})
    lists = pagination.find_all('a')
    last_page = lists[-2].get_text(strip=True)
    return int(last_page)

def get_job(html):
    title = html.find('h2').find('a')['title']
    companyInfo = html.find('h3').find_all('span')
    company = companyInfo[0].get_text(strip=True)
    location = companyInfo[1].get_text(strip=True)
    job_id = html['data-jobid']
    return {'title': title, 'company': company, 'location': location, 'link': f"https://stackoverflow.com/jobs/{job_id}"}

def extract_job(max_page):
    jobs = []
    for page in range(max_page):
        print(f"StackOverflow Scrapping page {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        print(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        listJobs = soup.find_all('div', {'class': '-job'})
        for list in listJobs:
            job = get_job(list)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    return extract_job(last_page)


