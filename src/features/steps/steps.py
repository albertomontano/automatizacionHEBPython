import sys
sys.path.append('C:\\Users\\AngelAlbertoMontañoP\\PycharmProjects\\miTiendaSelenium\\src')
print(sys.path)

from behave import*
from src.functions.functions import myFunctions



use_step_matcher("re")

@given("test esqueleto class")
def step_impl(context):
    myFunctions.sum(context)