import time

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:

        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            form_page.remove_ads()
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            time.sleep(5)
            print(p.first_name, p.last_name, p.email, p.mobile)
            print(result[0], result[1], result[3])
            assert [p.first_name + " " + p.last_name, p.email, p.mobile] == [result[0], result[1], result[3]], \
                "the form has not been filled"





