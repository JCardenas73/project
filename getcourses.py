import requests
import pandas as pd
import time

baseurl = 'https://courses.edx.org/api/'
endpoint = 'courses/v1/courses/?page_size=100&active_only=True'
endpoint2 = 'courseware/course/'

def main_link(baseurl, endpoint, x):
    response = requests.get(baseurl + endpoint + f'&page={x}') # Get the link of the page from its page parameter
    return response.json()


def get_pages(response):
    return response["pagination"]["num_pages"] # Access the pagination dict and the num_pages value for obtaining the int


def parse_json(response):
    idlist = []
    for item in response["results"]: # Iterating over the dicts within the results dict (4)
        course = {
            'id' : item['id']
            }
        idlist.append(course) # Append the info obtained
    return idlist



def get_ids():
    mainlist = []
    data = main_link(baseurl, endpoint, 1) # First page for getting the pages
    try:
        for x in range(1, get_pages(data)+1): # Iterate over the num of pages
            print(x)
            mainlist.extend(parse_json(main_link(baseurl, endpoint, x))) # Adding the id of each course
    except KeyError: # Last pages without any courses
        df = pd.DataFrame(mainlist)
        df.to_csv('idslist.csv')
        print(len(mainlist)) # Check the length of the final list

'''Getting the info from the courses ids, using the courseware api'''

def courseware_link(baseurl, endpoint, courseid):
    r = requests.get(baseurl + endpoint + courseid)
    try:
        return r.json()
    except requests.exceptions.JSONDecodeError: # Some courses aren't in JSON format
        r = requests.get(baseurl + endpoint + 'ccx-v1:adam+Mac_APccx+e0d+ccx@4')
        return r.json()


def get_info(response):
    try:
        info = { # Getting some of courses data
            'link': response['marketing_url'],
            'name': response['name'],
            'enddate' : response['end']
        }
        return info
    except KeyError: # If the course does not have one of the keys above
        info = {'link': 'None','name': 'None','enddate' : 'None'}
        return info

def get_courses_file():
    start = time.perf_counter()

    csv_path = 'idslist.csv'
    df = pd.read_csv(csv_path) # Read the ids file
    infos = [] # List of courses info
    for n in range(0, len(df['id']+1)): # Iterating over the number of ids obtained
        print(n)
        courseid = df.iloc[n,1] # Access each of the ids in the csv file
        infos.append(get_info(courseware_link(baseurl, endpoint2, courseid))) # Append each info
        continue

    # Finished the loop, all data goes to a csv file
    df1 = pd.DataFrame(infos)
    df1.to_csv('coursesinfo.csv', index=False, na_rep='None', mode='a', header=False) # (na_rep for empty spaces)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start,2)} seconds(s)')

