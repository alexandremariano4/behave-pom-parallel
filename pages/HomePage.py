__all__ = [
    "homePage"
]
from types import SimpleNamespace


def signupButton(context,text):
    context.driver.find_element('xpath',f'//strong[text()="{text}"]').click()


homePage = SimpleNamespace(
    clickSignupButton =  signupButton
)
