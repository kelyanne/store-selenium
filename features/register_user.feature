Feature: Register user

    Background:
        Given I am in Home Page
        And I click on "My Account" button
        And I click on "Register" button

    Scenario: Register a user that was already registered
        When I set "Dumb" to the input field "input-firstname"
        And I set "User" to the input field "input-lastname"
        And I set "dumb8@email.com" to the input field "input-email"
        And I set "123-456-7789" to the input field "input-telephone"
        And I set "Senha12345" to the input field "input-password"
        And I set "Senha12345" to the input field "input-confirm"
        And I checked the Privacy Policy checkbox
        And I submit the form
        Then I expect that a alert box contains the text "Warning: E-Mail Address is already registered!"

    Scenario: Register a user successfully
        When I set "Dumb" to the input field "input-firstname"
        And I set "User" to the input field "input-lastname"
        And I set "dumb11@email.com" to the input field "input-email"
        And I set "123-456-7789" to the input field "input-telephone"
        And I set "Senha12345" to the input field "input-password"
        And I set "Senha12345" to the input field "input-confirm"
        And I checked the Privacy Policy checkbox
        And I submit the form
        Then I expected see the message "Your Account Has Been Created!"






