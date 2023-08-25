import pytest


@pytest.fixture()
def url_protocol():
    return "https://"


@pytest.fixture()
def url_domain():
    return "habr.com/"


@pytest.fixture(scope='module')
def rest_params():
    rest_par = "ru/articles/448786/"
    yield rest_par
    rest_par += "666"


def test_protocol(url_protocol):
    assert url_protocol == "https://"


def test_url_domain(url_domain):
    assert url_domain == "habr.com/"


def test_rest_params(rest_params):
    assert rest_params == "ru/articles/448786/"


def test_rest_params_is_str(rest_params):
    assert type(rest_params) == type("ru/articles/448786/")


def test_entire_url(url_protocol, url_domain, rest_params):
    url = f"{url_protocol}{url_domain}{rest_params}"
    assert url == "https://habr.com/ru/articles/448786/"
