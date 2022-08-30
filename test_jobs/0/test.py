# Author: Paulo Vinicius - 2022
import requests
import json


print('#################### Consulta ####################')
print()

response = requests.get(
    'https://run.mocky.io/v3/ff723de1-f9c2-44cf-b2d0-7ee020abf7b6')



def fun_1():
    #! 1.Crie uma chamada JsonPath que retorne a Data de Compra de todos os pedidos
    print("1.Chamada JsonPath que retorne a Data de Compra de todos os pedidos")
    for x in response_info['pedidos']:
        # print(x)
        print(x['DataCompra'])
        
    print()


def fun_2():
    #! 2.Crie uma chamada JsonPath que retorne o Status do 1º pedido da lista.
    print("2.Chamada JsonPath que retorne o Status do 1º pedido da lista")
    print(response_info['pedidos'][0]['Status'])
    print()


def fun_3():
    #! 3.Crie uma chamada JsonPath que lista o Número do Pedido dos pedidos com status diferente de Cancelado
    print("3.Chamada JsonPath que lista o Número do Pedido dos pedidos com status diferente de Cancelado")
    for x in response_info['pedidos']:
        # print(x['NumeroPedido'])

        if x['Status'] != "Cancelado":
            #print(x['Status'])
            print(x['NumeroPedido'])
    print()


def fun_4():
    #! 4.Crie uma chamada JsonPath que lista o preço dos pedidos postados
    print("4.Chamada JsonPath que lista o preço dos pedidos postados")
    for x in response_info['pedidos']:
        # print(x['NumeroPedido'])
        if x['Status'] == "Postado":
            print(x['preco'])


if response.status_code == 200:
    # print(response.text)
    response_info = response.json()
    fun_1()
    fun_2()
    fun_3()
    fun_4()
else:
    print(f"Erro: {response.status_code}")
    pass
