def test_home_title(init_driver):
    assert "Snapmint" in init_driver.title
