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
Through a large scrape from the edX APIs using ```getcourses.py```, ```project.py``` using the keyword given by the user, filters out all the information and return the course that best matches.

---

### Development
- ```getcourses.py```: Generates all the ids and courses URLs
- ```project.py``` : Runs the searcher according to the ```csv``` files
- ```test.py``` : Tests the main functions in the project, running that functions the project must go without troubles.
- ```csv``` files: Each files contains the required data from where to filter the courses on ```project.py```

---

### Installation
1. Install all the pip-installable libraries in the ```requirements.txt```
2. Run ```project.py```

---

### Usage
The default platform is edX. You are free to add new ones as [Coursera](https://www.coursera.org/), [Udemy](https://www.udemy.com/), etc. Otherwise, run ```project.py``` and search out the course you are interested in.
For adding new data is needed to run first, ```getcourses.py``` and use the appropiate APIs.

The project requires the ```coursesinfo.csv``` and ```idlist.csv``` as needed for running the content scrapper.
