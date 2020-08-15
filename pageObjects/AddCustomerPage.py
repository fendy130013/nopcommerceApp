import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add customer page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuItem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    cbTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txtNewsletter_xpath = "//div[9]//div[2]//div[1]//div[1]//div[1]"
    liTestStore2_xpath = "//li[contains(text(),'Test store 2')]"
    liYourStoreName_xpath = "//li[contains(text(),'Your store name')]"
    txtCustomerRoles_xpath = "//div[10]//div[2]//div[1]//div[1]//div[1]"
    liAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    liForumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    liGuests_xpath = "//li[contains(text(),'Guests')]"
    liRegistered_xpath = "//li[contains(text(),'Registered')]"
    liVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpManagerOfVendor_xpath = "//select[@id='VendorId']"
    cbActive_xpath = "//input[@id='Active']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.liRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.liAdministrators_xpath)
        elif role == "Guests":
            # Here user can be Registered or Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.liGuests_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element_by_xpath(self.liForumModerators_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.liVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.liGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setNewsletter(self, store):
        self.driver.find_element_by_xpath(self.txtNewsletter_xpath).click()
        time.sleep(3)
        if store == "Test store 2":
            self.liststore = self.driver.find_element_by_xpath(self.liTestStore2_xpath)
        elif store == "Your store name":
            self.liststore = self.driver.find_element_by_xpath(self.liYourStoreName_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.liststore)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpManagerOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()