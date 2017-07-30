# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


fixture = None


@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, base_url=base_url)
    elif not fixture.is_valid():
        fixture = Application(browser="firefox")
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finish():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(finish)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
