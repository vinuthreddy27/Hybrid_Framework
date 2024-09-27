from yourstore.POM.titlepage import Title


def test_title_verification(driver):
    verify=Title(driver)
    verify.title_verification()
    expected_title = "Your Store"
    if driver.title == expected_title:
        assert True


def test_title_verification1(driver):
    verify= Title(driver)
    verify.title_verification()
    expected_title = "our Store"
    if driver.title == expected_title:
        print("test title failed")
    else:
        print("test title passed")