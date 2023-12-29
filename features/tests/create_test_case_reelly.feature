# Created by edc_p at 12/19/2023
Feature: Make Test Case for Reelly Webpage

  Scenario: User can go to settings and see the right number of UI elements
    Given Open Reelly webpage
    When  Log into page
    Then  Click on settings option
    Then Verify Connect the company
    Then Verify 11 options

###  behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/main_page_ui.feature ###
###  allure serve test_results/ ##### to put the data in allure webpage