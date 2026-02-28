import pytest
from pages.login_page import LoginPage
from utils.excel_reader import read_excel

@pytest.mark.parametrize("email,_", read_excel("Login"))
def test_login(init_driver, email, _):
    lp = LoginPage(init_driver)
    lp.enter_email(email)
    assert "Snapmint" in init_driver.title
