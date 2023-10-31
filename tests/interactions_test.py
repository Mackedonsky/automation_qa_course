import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortablePage:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            sortable_page.remove_ads()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'The order of the list has not been changed'
            assert grid_before != grid_after, 'The order of the grid has not been changed'

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            selectable_page.remove_ads()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "Elements were not selected"
            assert len(item_grid) > 0, "Elements were not selected"

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            resizable_page.remove_ads()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll down
            max_resize, min_resize = resizable_page.change_size_resizable()
            max_box, min_box = resizable_page.change_size_resizable_box()
            assert ('500px', '300px') == max_box, 'maximum size is not equal to 500*300'
            assert ('150px', '150px') == min_box, 'minimum size is not equal to 150*150'
            assert max_resize != min_resize, 'size has not been changed'
