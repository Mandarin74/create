import pytest
import yaml
from mod import Site


with open("testdata.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def sel_log():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def sel_pass():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def sel_button():
    return """button"""

@pytest.fixture()
def sel_err():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def prov():
    return """//*[@id="app"]/main/nav/ul/li[1]/a"""


@pytest.fixture()
def sel_button2():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def title():
    return  """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def description():
    return  """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def content():
    return  """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def sel_button3():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def head_s():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def site():
    site_class = Site(data["address"])
    yield site_class
    site_class.close()