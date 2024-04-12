# Course aggregator

#### Video Demo on [YouTube](https://youtu.be/3a0A-B64nNc)

### Description:
With [**Course aggregator**](`#0969DA`) the user is able to look for different courses all over the web,
as it provides an in-search feature for providing the last available online courses.

---

### Purpose
Course aggregator was first based on the content aggregator which, could minimize the search of courses through the web. As it can be sometimes time-taken to look for the right course for which to invest time and money, the software break down the common search scheme.

---

### How it works?
Through a large scrape from the edX APIs using ```getcourses.py```, ```project.py``` using the keyword given by the user, filters out all the information and it returns the course or couses that best matches, followed by its full title and URL to the web page.

---

### Development
- ```getcourses.py```: Generates all the ids and courses URLs
- ```project.py``` : Runs the searcher according to the ```csv``` files
- ```test.py``` : Tests the main functions in the project, running that functions the project must go without troubles.
- ```csv``` files: Each files contains the required data from where to filter the courses on ```project.py```

---

### Installation
1. Install all the pip-installable libraries in the ```requirements.txt```
2. Download each of the csv files containing all the courses data
3. Download ```getcourses.py``` and ```project.py``` as part of the software functionality

---

### Usage
The default platform is edX. You are free to add new ones as [Coursera](https://www.coursera.org/), [Udemy](https://www.udemy.com/), etc. Otherwise, run ```project.py``` and search out the course you are interested in.
For adding new data is needed to run first, ```getcourses.py``` and use the appropiate APIs.

The project requires the ```coursesinfo.csv``` and ```idlist.csv``` as needed for running the content scrapper.

Once opened the project, type ```python project.py```, as always, press enter and you should encounter a message prompt for typing a keyword or full name of the course of your interest. Right after hitting enter, a table will appear containing all the courses available with its URL, according to the input typed.

Now, you can go ahead and look for the course of your need, copy the link and enroll as you find useful and interesting the road to learning.

