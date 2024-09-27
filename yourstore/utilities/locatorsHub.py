from yourstore.library.library import Base

class RegisterPagelocators(Base):
    my_account_locator = ("xpath", "//span[.='My Account']")
    register_locator = ("xpath", "//a[.='Register']")
    first_name_locator = ("id", "input-firstname")
    last_name_locator = ("id", "input-lastname")
    email_locator = ("id", "input-email")
    telephone_locator = ("id", "input-telephone")
    password_locator = ("id", "input-password")
    conform_password_locator = ("id", "input-confirm")
    radio_btn = ("xpath", "//label[@class='radio-inline']/input[@value = '1']")
    privacy_policy_check_box_btn = ("xpath", "//input[@type='checkbox']")
    register_btn = ("xpath", "//input[@value='Continue']")

class LoginPage_locators(Base):
    my_account_locator = ("xpath", "//span[.='My Account']")
    login_locator = ("xpath", "//a[.='Login']")
    email_locator = ("id", "input-email")
    password_locator = ("id", "input-password")
    login_btn = ("xpath", "//input[@value='Login']")

class search_page_locators(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")

class affilicate_account_locators(Base):
    account_link=("xpath","//a[.='Edit your affiliate information']")
    company_text_field=("name","company")
    website_textfield=("name","website")
    tax_textfield=("name","tax")
    payment_mode_btn=("xpath","//input[@value='paypal']")
    paypal_textfield=("name","paypal")
    agree_checkbox=("name","agree")
    continue_btn=("xpath","//input[@type='submit']")

class SearchProduct_locators(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")
    add_to_cart_btn = ("xpath", "//span[.='Add to Cart']")
    wishislist_btn = ("xpath", "//span[.='Add to Cart']/../..//i[@class='fa fa-heart']")

class Password_change(Base):
    my_account_locator = ("xpath", "//span[.='My Account']")
    login_locator = ("xpath", "//a[.='Login']")
    email_locator = ("id", "input-email")
    password_locator = ("id", "input-password")
    login_btn = ("xpath", "//input[@value='Login']")
    changepassowrd_locator = ("xpath", "//ul[@class='list-unstyled']/..//a[.='Change your password']")
    password = ("name", "password")
    c_password = ("name", "confirm")
    conform_btn = ("xpath", "//input[@value='Continue']")
    logout_btn = ("xpath", "//ul[@class='dropdown-menu dropdown-menu-right']/..//a[.='Logout']")

class Modify_wishlist(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")
    product_link=("xpath","//p[@class='price']/..//a[.='Samsung Galaxy Tab 10.1']")
    wishlist_symbol=("xpath","//button[@data-original-title='Add to Wish List']")
    modify_btn = ("id","wishlist-total")
    add_2_cart_btn = ("xpath", "//button[@data-original-title='Add to Cart']")
    remove_btn = ("xpath", "//a[@data-original-title='Remove']")

class Modify_Accountdetails(Base):
    edit_link = ("xpath", "//a[.='Edit your account information']")
    telephone_locator = ("name", "telephone")
    continue_btn = ("xpath", "//input[@value='Continue']")

class Add_2_cart_locaters(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")
    product_locator = ("xpath", "//img[contains(@src,'samsung_syncmaster_941bw-228x228.jpg')]")
    add_to_cart_locator = ("id", "button-cart")
    quantity_locator = ("name", "quantity")
    cart_locator = ("id", "cart")
    remove_btn = ("xpath","//button[@title='Remove']")

class Add_review_for_product(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")
    product_link=("xpath","//a[.='iPod Touch']")
    image1=("xpath","//img[contains(@src,'ipod_touch_1-228x228.jpg')]")
    next_btn=("xpath","//button[@title='Next (Right arrow key)']")
    prev_btn=("xpath","//button[@title='Previous (Left arrow key)']")
    image2=("xpath","//img[contains(@src,'ipod_touch_6-74x74.jpg')]")
    close_btn=("class name","mfp-close")
    review_link=("xpath","//a[.='Write a review']")
    yourname_tf=("id","input-name")
    text_area=("name","text")
    rating_rb=("xpath","//input[@value='5']")
    continue_btn=("id","button-review")

class Add_a_query(Base):
    contact_us_locator=("xpath","//a[.='Contact Us']")
    text_area_locator=("name","enquiry")
    submit_btn=("xpath","//input[@value='Submit']")
    continue_btn=("xpath","//a[.='Continue']")
    my_account_locator = ("xpath", "//span[.='My Account']")
    logout_btn=("xpath","//a[.='Logout']")

class Giftpage_locators(Base):
    gift_locator=("xpath","//a[.='Gift Certificates']")
    receipient_locator=("id","input-to-name")
    receipient_email=("id","input-to-email")
    your_name=("id","input-from-name")
    your_email=("id","input-from-email")
    birthday_btn=("xpath","//input[@value='7']")
    messeage=("xpath","//textarea[@id='input-message']")
    amount=("xpath","//input[@name='amount']")
    agree_checkbox=("xpath","//input[@name='agree']")
    continue_btn=("xpath","//input[@value='Continue']")

class compare_page_locators(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")
    product_locator=("xpath","//img[contains(@src,'palm_treo_pro_1-228x228.jpg')]")
    product_locator2=("xpath","//a[.='Sony VAIO']")
    compare_btn=("xpath","//button[@data-original-title='Compare this Product']")
    compare_link=("id","compare-total")
    remove_btn=("xpath","//a[contains(@href,'compare&remove=46')]/..//a")
    add_to_cart_btn=("xpath","//a[contains(@href,'compare&remove=29')]/..//input")


class anchor_link(Base):
    locator=("xpath","//div[@class='col-sm-3']//h5[.='Extras']/..//a[.='Brands']")

class date(Base):
    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")
    product_link=("xpath","//a[.='HP LP3065']")

class Brands(Base):
    ...