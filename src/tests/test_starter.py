import time


def test_example_is_working(page):
    page.goto("http://localhost:3000/signin")
    time.sleep(4)
