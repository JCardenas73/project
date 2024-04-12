from getcourses import get_pages, main_link, get_info, courseware_link
from project import convert_link, get_title
import pytest

def test_convert():
    assert convert_link('https://www.edx.org/course/cs50s-introduction-to-programming-with-python-course-v1harvardxcs50ppython') == 'edx.org/course/cs50s-introduction-to-programming-with-python-course-v1harvardxcs50ppython'

def test_title():
    with pytest.raises(SystemExit):
        get_title(' ')

def test_pages():
    response = main_link('https://courses.edx.org/api/','courses/v1/courses/?active_only=True','&page=2&page_size=100')
    assert get_pages(response) == 62


def test_info():
    response = courseware_link('https://courses.edx.org/api/','courseware/course/','course-v1:HarvardX+CS50P+Python')
    assert get_info(response) == {'link': 'https://www.edx.org/course/cs50s-introduction-to-programming-with-python-course-v1harvardxcs50ppython', 'name': "CS50's Introduction to Programming with Python", 'enddate': '2024-12-31T23:59:00Z'}
