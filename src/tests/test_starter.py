import time


def test_example_is_working(page):
    page.goto("http://localhost:3000/signin")
    page.fill('#username', 'Katharina_Bernier')
    page.fill('#password', 's3cret')
    page.click('[data-test="signin-submit"]')
