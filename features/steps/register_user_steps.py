import time

from behave import given, then, when


@given(u'I am in Home Page')
def step_impl(context):
    context.driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")


@given(u'I click on "{element}" button')
def step_impl(context, element):
    context.driver.click_link_text(element)


@when(u'I set "{value}" to the input field "{element}"')
def step_impl(context, value, element):
    elem = context.driver.get_element(element, by="id")
    elem.send_keys(value)


@when(u'I checked the Privacy Policy checkbox')
def step_impl(context):
    context.driver.get_element("agree", by="name").click()


@when(u'I submit the form')
def step_impl(context):
    context.driver.submit(".form-horizontal")


@then(u'I expected see the message "{message}"')
def step_impl(context, message):
    assert context.driver.title == message


@then(u'I expect that a alert box contains the text "{message}"')
def step_impl(context, message):
    assert context.driver.element_contains(".alert", message)

