from selenium.webdriver.common.by import By


class PracticeFormPageLocators:
    # ------------------ Поля ввода ------------------
    NAME_INPUT = By.ID, "firstName"
    LAST_NAME_INPUT = By.ID, "lastName"
    EMAIL_INPUT = By.ID, "userEmail"
    MOBILE_INPUT = By.ID, "userNumber"
    DATE_OF_BIRTH = By.ID, "dateOfBirthInput"
    SUBJECTS_INPUT = By.XPATH, "//input[@id='subjectsInput']"
    SUBJECTS_OPTION_ONE = By.XPATH, "//div[@id='react-select-2-option-0']"
    CURRENT_ADDRESS_INPUT = By.ID, "currentAddress"
    PICTURE_UPLOAD = By.ID, "uploadPicture"

    # ------------------ Радио-кнопки ------------------
    MALE_RADIO = By.XPATH, "//input[@id='gender-radio-1']/following-sibling::label"
    FEMALE_RADIO = By.XPATH, "//input[@id='gender-radio-2']/following-sibling::label"
    OTHER_RADIO = By.XPATH, "//input[@id='gender-radio-3']/following-sibling::label"

    # ------------------ Чекбоксы ------------------
    SPORTS_CHECKBOX = By.XPATH, "//input[@id='hobbies-checkbox-1']/following-sibling::label"
    READING_CHECKBOX = By.XPATH, "//input[@id='hobbies-checkbox-2']/following-sibling::label"
    MUSIC_CHECKBOX = By.XPATH, "//input[@id='hobbies-checkbox-3']/following-sibling::label"

    # ------------------ State & City ------------------
    SELECT_STATE = By.XPATH, "//div[text()='Select State']"
    NCR_STATE = By.XPATH, "//div[text()='NCR']"
    UTTAR_PRADESH_STATE = By.XPATH, "//div[text()='Uttar Pradesh']"
    HARYANA_STATE = By.XPATH, "//div[text()='Haryana']"
    RAJASTHAN_STATE = By.XPATH, "//div[text()='Rajasthan']"

    SELECT_CITY = By.XPATH, "//div[text()='Select City']"
    DELHI_CITY = By.XPATH, "//div[text()='Delhi']"
    GURGAON_CITY = By.XPATH, "//div[text()='Gurgaon']"
    NOIDA_CITY = By.XPATH, "//div[text()='Noida']"

    # ------------------ Кнопка отправки ------------------
    SUBMIT_BUTTON = By.ID, "submit"

    # ------------------ Результаты заполненной формы ------------------
    RESULT_STUDENT_NAME = By.XPATH, "//td[text()='Student Name']/following-sibling::td"
    RESULT_STUDENT_EMAIL = By.XPATH, "//td[text()='Student Email']/following-sibling::td"
    RESULT_GENDER = By.XPATH, "//td[text()='Gender']/following-sibling::td"
    RESULT_MOBILE = By.XPATH, "//td[text()='Mobile']/following-sibling::td"
    RESULT_DATE_OF_BIRTH = By.XPATH, "//td[text()='Date of Birth']/following-sibling::td"
    RESULT_SUBJECTS = By.XPATH, "//td[text()='Subjects']/following-sibling::td"
    RESULT_HOBBIES = By.XPATH, "//td[text()='Hobbies']/following-sibling::td"
    RESULT_PICTURE = By.XPATH, "//td[text()='Picture']/following-sibling::td"
    RESULT_ADDRESS = By.XPATH, "//td[text()='Address']/following-sibling::td"
    RESULT_STATE_AND_CITY = By.XPATH, "//td[text()='State and City']/following-sibling::td"
