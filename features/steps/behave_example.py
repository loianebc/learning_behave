from behave import *
import requests
import json

@given(u'I have the product information')
def step_impl(context):
    context.user_data = {
        "title": "iphone 12 64GB",
        "price": 5000.5,
        "description": "Iphone 12 64GB cor preto",
        "image": "https: //i.pravatar.cc",
        "category": "celulares"
        }


@when(u'I register the product')
def step_impl(context):
    response = requests.post('https://fakestoreapi.com/products', json=context.user_data)
    context.response = response


@then(u'the product will be register on the store system')
def step_impl(context):
    response_json = context.response.json()
    assert context.response.status_code == 200
    assert response_json['title'] == "iphone 12 64GB"
    assert response_json['price'] == 5000.5
    assert response_json['description'] == "Iphone 12 64GB cor preto"
    assert response_json['image'] == "https: //i.pravatar.cc"
    assert response_json['category'] == "celulares"  
    assert 'id' in response_json


@given(u'I have access to the store system')
def step_impl(context):
    pass
    # TO DO implement a authentication methoted in the future


@when(u'I consult all the product')
def step_impl(context):
    response = requests.get('https://fakestoreapi.com/products')
    context.response = response


@then(u'all the products will be presented')
def step_impl(context):
    response_json = context.response.json()
    assert context.response.status_code == 200
    assert len(response_json) == 20
    response_filter = [i for i in response_json if i['title'] == 'SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s' and i['price'] == 109]
    assert len(response_filter) > 0
