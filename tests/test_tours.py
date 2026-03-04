import pytest
import allure
from pages.home_page import HomePage
from pages.tours_page import ToursPage
from utilities.yaml_reader import read_yaml

@pytest.mark.smoke
@allure.feature("Tours Module")
class TestTours:

    @pytest.mark.usefixtures("setup")
    def test_tours_flow(self):

        data = read_yaml("testdata/testdata.yaml")

        home = HomePage(self.driver, self.timeout, self.logger)
        tours = ToursPage(self.driver, self.timeout, self.logger)

        home.go_to_tours()
        tours.search_destination(data["tours"]["destination"])