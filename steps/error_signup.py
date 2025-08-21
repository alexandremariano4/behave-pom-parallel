from behave import given,when,then
from pages import deliverPage


@then('devo receber a mensagem de erro "{text}"')
def step_impl(context,text):
    deliverPage.hasErrorMessage(context,text)
