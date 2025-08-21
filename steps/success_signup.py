from behave import given,when,then
from pages import homePage,deliverPage


@given('que estou na página principal')
def step_impl(context):
    assert context.driver.title == 'Buger Eats'

@when('clico no botão de "{text}"')
def step_impl(context,text):
    homePage.clickSignupButton(context,text)
    assert '/deliver' in context.driver.current_url 

@when('preencho o formulário de cadastro com os dados abaixo')
def step_impl(context):
    deliverPage.fillFieldsForm(context)

@when('envio uma imagem da cnh')
def step_impl(context):
    deliverPage.uploadImage(context)

@when('clico no botão "Cadastre-se para fazer entregas"')
def step_impl(context):
    deliverPage.submitForm(context)
    

@then('devo receber a mensagem de confirmação "{text}"')
def step_impl(context,text):
    assert context.driver.find_element('id', 'swal2-html-container').text == text
