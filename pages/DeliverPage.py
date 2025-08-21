__all__ = [
    "deliverPage"
]
from types import SimpleNamespace
from pathlib import Path

image_path = (Path().absolute()/'images').resolve()


def fillForm(context):
    user = {}
    for row in context.table:
        user.update({
            'name':row[0],
            'cpf': row[1],
            'email':row[2],
            'phone':row[3],
            'cep':row[4],
            'number':row[5],
            'complement':row[6],
            'deliveryMethod':row[7]
        })
        
    context.driver.find_element('css selector','[name=fullName]').send_keys(user['name'])
    context.driver.find_element('css selector','[placeholder="CPF somente números"]').send_keys(user['cpf'])
    context.driver.find_element('css selector','[name=email]').send_keys(user['email'])
    context.driver.find_element('css selector','[name=whatsapp]').send_keys(user['phone'])
    context.driver.find_element('css selector','[placeholder="CEP"]').send_keys(user['cep'])
    context.driver.find_element('css selector','[value="Buscar CEP"]').click()
    context.driver.find_element('css selector','[name=address-number]').send_keys(user['number'])
    context.driver.find_element('css selector','[name=address-details]').send_keys(user['complement'])
    context.driver.find_element('xpath',f'//span[text()="{user['deliveryMethod']}"]/parent::li').click()
    
    assert context.driver.find_element('xpath',f'//span[text()="{user['deliveryMethod']}"]/parent::li').get_attribute('class') == 'selected'

def sendImage(context):
    context.driver.find_element('css selector','.dropzone > input').send_keys(str(image_path/'cnh-image.jpg'))


def sendForm(context):
    context.driver.find_element('css selector','.button-success').click()

def validateErrorMessage(context,text):
    assert context.driver.find_element('css selector', '.alert-error').text == text

deliverPage = SimpleNamespace(
    fillFieldsForm  = fillForm,
    uploadImage     = sendImage,
    submitForm      = sendForm,
    hasErrorMessage = validateErrorMessage
)
