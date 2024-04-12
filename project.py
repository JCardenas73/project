import re
import sys
import argparse as argp
import pandas as pd
from tabulate import tabulate
import re


def get_title(title):
    if title.isspace():
        sys.exit('Invalid data')
    else:
        return title

def convert_link(url):
    matches = re.search(r'https://www.edx.org/course/(.+)', url)
    return f'edx.org/course/{matches.group(1)}'



def get_course():
    courses = pd.read_csv('coursesinfo.csv')
    pd.options.display.max_colwidth = 200
    df = pd.DataFrame(courses)

    coursename = get_title(input('Enter a keyword or a course name: ')).lower()

    result_df = df['name'].str.lower().str.contains(coursename, na=False)
    link1 = df.loc[result_df, 'link']
    names = df.loc[result_df, 'name']
    ends = df.loc[result_df, 'enddate']

    # for char in coursename:
    #     result_df = df['name'].str.lower().str.contains(char, na=False)
    #     link1 = df.loc[result_df, 'link']
    #     names = df.loc[result_df, 'name']
    #     ends = df.loc[result_df, 'enddate']

    links = link1.to_list()
    titles = names.to_list()
    dates = ends.to_list()
    shorturl = []
    for link in links:
        try:
            shorturl.append(convert_link(link))
            continue
        except TypeError:
            shorturl.append('Not link')
            continue

    shortnames = []
    for title in titles:
        titlesplit = title.split(' ')
        if len(titlesplit) > 8:
            titlesplit[8:] = ''
            rlist = ' '.join(titlesplit)
            shortnames.append(str(rlist))
            continue
        else:
            shortnames.append(title)
            continue

    table = {'Title':shortnames, 'URL':shorturl}
    return pd.DataFrame(table).set_index('Title')




def main():
    df = get_course()
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))


if __name__ == '__main__':
    main()
