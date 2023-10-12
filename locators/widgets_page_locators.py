from selenium.webdriver.common.by import By


class AccordianPageLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_DELETE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')




class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id = "datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class = "react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class = "react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')

    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class = "range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id = "sliderValue"]')


class ProgressBarPageLocators:
    START_STOP_BUTTON = (By.CSS_SELECTOR, 'button[id = "startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class = "progress-bar bg-info"]')


class TabsPageLocators:
    TAB_WHAT = (By.CSS_SELECTOR, 'a[id = "demo-tab-what"]')
    TAB_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id = "demo-tabpane-what"]')
    TAB_ORIGIN = (By.CSS_SELECTOR, 'a[id = "demo-tab-origin"]')
    TAB_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id = "demo-tabpane-origin"]')
    TAB_USE = (By.CSS_SELECTOR, 'a[id = "demo-tab-use"]')
    TAB_USE_CONTENT = (By.CSS_SELECTOR, 'div[id = "demo-tabpane-use"]')
    TAB_MORE = (By.CSS_SELECTOR, 'a[id = "demo-tab-more"]')
    TAB_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id = "demo-tabpane-more"]')


class ToolTipsPageLocators:
    DEFAULT_BUTTON = (By.CSS_SELECTOR, 'button[id = "toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    DEFAULT_FIELD = (By.CSS_SELECTOR, 'input[id = "toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, "//a[text()='Contrary']")
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, "//a[text()='1.10.32']")
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIP_INNERS = (By.CSS_SELECTOR, 'div[class= "tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


# class SelectMenuPageLocators:
#     SELECT_VALUE_BUTTON = (By.CSS_SELECTOR, 'div[id = "withOptGroup"]')
#     INPUT_VALUE_BUTTON = (By.XPATH, "(//input[starts-with(@id, 'react-select')])[1]")
#     ALL_VALUES = (By.XPATH, "//div[starts-with(@id, 'react-select-2-option')]")
#
#     SELECT_ONE_BUTTON = (By.CSS_SELECTOR, 'div[id = "selectOne"]')
#     INPUT_ONE_BUTTON = (By.CSS_SELECTOR, 'input[id = "react-select-6-input"]')
#     SELECT_OLD_BUTTON = (By.CSS_SELECTOR, 'select[id = "oldSelectMenu"]')
#     MULTI_INPUT_BUTTON = (By.CSS_SELECTOR, 'input[id = "react-select-23-input"]')
#     MULTI_INPUT_VALUE = (By.CSS_SELECTOR, 'div[class ="css-1rhbuit-multiValue"]')
#     STANDARD_MULTI_BUTTON = (By.CSS_SELECTOR, 'select[id = "cars"]')


