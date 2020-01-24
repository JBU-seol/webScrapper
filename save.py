import csv

def save_csv_file(jobs):
    file = open("jobs.csv", "w", encoding='UTF-8')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
