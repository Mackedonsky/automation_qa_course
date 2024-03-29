import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage, SelectMenuPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            accordian_page.remove_ads()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title or missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title or missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title or missing text'

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.remove_ads()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'Added colors are missing in input'

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.remove_ads()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, 'color was not deleted'

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.remove_ads()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, 'Added color is missing in input'

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_picker_page.remove_ads()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'The date has not been changed'

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_picker_page.remove_ads()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            time.sleep(2)
            assert value_date_before != value_date_after, 'The date and time have not been changed'

    class TestSliderPage:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            slider_page.remove_ads()
            before, after = slider_page.change_slider_value()
            assert before != after, 'the slider value has not been changed'

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            progress_bar_page.remove_ads()
            before, after = progress_bar_page.change_progress_bar_value()
            assert before != after, 'the progress bar value has not been changed'


class TestTabsPage:

    def test_tabs(self, driver):
        tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs_page.open()
        tabs_page.remove_ads()
        what_button, what_content = tabs_page.check_tabs('what')
        origin_button, origin_content = tabs_page.check_tabs('origin')
        use_button, use_content = tabs_page.check_tabs('use')
        # tabs_page.check_tabs('more')
        assert what_button == "What" and what_content != 0, 'tab was not pressed or text is missing'
        assert origin_button == "Origin" and origin_content != 0, 'tab was not pressed or text is missing'
        assert use_button == "Use" and use_content != 0, 'tab was not pressed or text is missing'


class TestToolTipsPage:

    def test_tool_tips(self, driver):
        tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
        tool_tips_page.open()
        tool_tips_page.remove_ads()
        button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
        assert button_text == 'You hovered over the Button', 'Hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'Hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'Hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'


class TestMenuPage:

    def test_menu_items(self, driver):
        menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
        menu_page.open()
        menu_page.remove_ads()
        data = menu_page.check_menu()
        assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
                        'Sub Sub Item 2', 'Main Item 3'], 'Menu item have not been selected'


# class TestSelectMenuPage:
#
#     def test_select_menu(self, driver):
#         select_menu = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
#         select_menu.open()
#         select_menu.remove_ads()
#         result = select_menu.select_value()
#         time.sleep(2)
#         print(result)
