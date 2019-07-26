from trial_of_the_stones.models.page_model import PageModel
import selenium
import unittest
import time


def trial_of_the_stones_automation():
    '''
    Source web page: https://techstepacademy.com/trial-of-the-stones
    :return:
    '''

    # open web page
    page = PageModel(selenium.webdriver.Chrome())
    page.open_page()

    password = solve_riddle_of_stone(page)
    solve_riddle_of_secrets(password, page)
    solve_the_two_merchants(page)
    final_check(page)

    # close web page
    time.sleep(2)
    page.close()


def solve_riddle_of_stone(page):

    # type answer and click on ansswer button
    page.riddle_of_stone_field.send_keys('rock')
    unittest.TestCase().assertFalse(page.password.is_displayed())
    page.riddle_of_stone_button.click()

    # verify is password displayed
    unittest.TestCase().assertTrue(page.password.is_displayed())
    password = page.password.text
    unittest.TestCase().assertEqual('bamboo', password)

    return password


def solve_riddle_of_secrets(password, page):

    # type password and click on Answer button
    page.password_field.send_keys(password)
    unittest.TestCase().assertFalse(page.password_success.is_displayed())
    page.password_answer_button.click()
    unittest.TestCase().assertEqual('Success!', page.password_success.text)
    unittest.TestCase().assertTrue(page.password_success.is_displayed())


def solve_the_two_merchants(page):

    # compare wealth and type the richest merchant name
    page.richest_merchant_field.send_keys(page.bernard_name
                                          if int(page.bernard_wealth) > int(page.jessica_wealth)
                                          else page.jessica_name)
    unittest.TestCase().assertFalse(page.merchant_success.is_displayed())
    page.richest_merchant_button.click()
    unittest.TestCase().assertTrue(page.merchant_success.is_displayed())
    unittest.TestCase().assertEqual('Success!', page.merchant_success.text)


def final_check(page):
    # final check
    unittest.TestCase().assertFalse(page.trial_complete.is_displayed())
    page.check_answers_button.click()
    unittest.TestCase().assertTrue(page.trial_complete.is_displayed())
    unittest.TestCase().assertEqual('Trial Complete', page.trial_complete.text)


if __name__ == '__main__':
    trial_of_the_stones_automation()

