from yourstore.POM.registerpage import Myaccount

# def test_register(driver):
#     my_account=Myaccount(driver)
#     my_account.register("vinuth","reddy",
#                         "rv@gmail.com","7676252914",
#                         "selenium","selenium")

    # assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()


# def test_register_with_invalid_credentials(driver):
#     my_account=Myaccount(driver)
#     my_account.register("vinuth","reddy",
#                         "rv1@gmail.com","7676252914",
#                         "selenium","seleniu")
#
#
#     assert driver.find_element("xpath","//div[@class='text-danger']").is_displayed()


'''firstname'''
# def test_register_with_no_firstname(driver):
#     my_account=Myaccount(driver)
#     my_account.register("","",
#                         "","",
#                         "","")
#
#
#     assert driver.find_element("xpath","(//div[@class='text-danger'])[1]").is_displayed()


# def test_register_firstname_with_cgt_32(driver):
#     my_account=Myaccount(driver)
#     my_account.register("Chinnaswamy Muthuswami venugopal Iyer","",
#                         "","",
#                         "","")
#
#
#     assert driver.find_element("xpath","(//div[@class='text-danger'])[1]").is_displayed()

# def test_register_with_firstname_in_other_language(driver):
#
#     my_account=Myaccount(driver)
#     my_account.register("अय्यर..वेनुगोपाल अय्यर","iyer",
#                         "ncp007@gmail.com","7676252914",
#                         "selenium","selenium")
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()
#
#
# def test_register_with_firstname_space_bw_them(driver):
#     my_account=Myaccount(driver)
#     my_account.register("i y e r","venugopal",
#                         "ncp2@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()
#
# def test_register_firstname__with_specialcharater(driver):
#     my_account=Myaccount(driver)
#     my_account.register("$iyer","venugopal",
#                         "ncp3@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()
#
#
#
# def test_register_with_firstname_alphanumeric(driver):
#     my_account=Myaccount(driver)
#     my_account.register("iyer69","venugopal",
#                         "ncp4@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()
#
#
# def test_register_with_firstname_alphanumeric_with_special_charater(driver):
#     my_account=Myaccount(driver)
#     my_account.register("$iyer69","venugopal",
#                         "ncp5@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()
#
# def test_register_firstname_with_first_charater_uppercase(driver):
#     my_account=Myaccount(driver)
#     my_account.register("Iyer","venugopal",
#                         "ncp6@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()

'''lastname'''
# def test_register_no_lastname(driver):
#     my_account=Myaccount(driver)
#     my_account.register("vinuth","",
#                         "rv@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[.='Last Name must be between 1 and 32 characters!']").is_displayed()

'''f'''
# def test_register_lastname_in_other_language(driver):
#     home_pj = Homepage(driver)
#     home_pj.click_on_myaccount()
#     my_account=Myaccount(driver)
#     my_account.register("vinuth","ರೆಡ್ಡಿ",
#                         "rv@gmail.com","7676252914",
#                         "selenium","selenium")
#     sleep(5)
#     assert driver.find_element("xpath","//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']").is_displayed()

# def test_register_lastname_gt_32(driver):
#     my_account=Myaccount(driver)
#     my_account.register("iyer","Iyer Venugopal Iyer Mutuswamy Venugopal Iyer Innaswamy Mutuswamy Venugopal Iyer",
#                         "rv@gmail.com","7676252914",
#                         "selenium","selenium")
#
#     assert driver.find_element("xpath","//div[.='Last Name must be between 1 and 32 characters!']").is_displayed()


'''email'''
# def test_register_no_email(driver):
#     my_account=Myaccount(driver)
#     my_account.register("iyer","Venugopal",
#                         "","7676252914",
#                         "selenium","selenium")
#     assert driver.find_element("xpath","//div[.='E-Mail Address does not appear to be valid!']").is_displayed()

def test_register_wrong_email(driver):
    my_account = Myaccount(driver)
    my_account.register("iyer", "Venugopal",
                            "reddyvinuthgmail.com", "7676252914",
                            "selenium", "selenium")
    # assert driver.find_element("xpath", "//div[.='E-Mail Address does not appear to be valid!']").is_displayed()

# def test_register_same_email(driver):
#     my_account = Myaccount(driver)
#     my_account.register("iyer", "Venugopal",
#                             "reddyvinuth27@gmail.com", "7676252914",
#                             "selenium", "selenium")
#     assert driver.find_element("xpath", "//div[.='Warning: E-Mail Address is already registered!']").is_displayed()



'''telephone'''
# def test_register_no_telephone(driver):
#     my_account = Myaccount(driver)
#     my_account.register("iyer", "Venugopal",
#                             "rv27@gmail.com", "",
#                             "selenium", "selenium")
#     assert driver.find_element("xpath", "//div[.='Telephone must be between 3 and 32 characters!']").is_displayed()
#
# def test_register_telephone_lt_3(driver):
#     my_account = Myaccount(driver)
#     my_account.register("iyer", "Venugopal",
#                             "rrr27@gmail.com", "69",
#                             "selenium", "selenium")
#     assert driver.find_element("xpath", "//div[.='Telephone must be between 3 and 32 characters!']").is_displayed()
#
#
# def test_register_telephone_gt_32(driver):
#     my_account = Myaccount(driver)
#     my_account.register("iyer", "Venugopal",
#                         "jasongilpese@gmail.com", "123456789101112131415161718192021222324252627282930313233",
#                         "selenium", "selenium")
#
#     assert driver.find_element("xpath", "//div[.='Telephone must be between 3 and 32 characters!']").is_displayed()
#