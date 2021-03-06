import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"
def extract_indeed_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {"class":"pagination"})
    lists = pagination.find_all('a')
    pages = []

    for list in lists[:-1]:
        pages.append(int(list.string))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find('div', {"class": "title"}).find('a')["title"]
    company = html.find('span', {"class": "company"})
    company_anchor = company.find('a')
    if company_anchor is None:
        company = str(company.string)
    else:
        company = str(company_anchor.string)
    company = company.strip()
    location = html.find('div', {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location, "link": f"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_indeed_jobs(max_page):
    jobs = []
    for page in range(max_page):
        print(f"Indeed Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*50}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    max_page = extract_indeed_page()
    jobs = extract_indeed_jobs(max_page)
    return jobs