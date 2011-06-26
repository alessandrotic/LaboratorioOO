#coding:utf-8
import unittest
from should_dsl import should
from datetime import date

class Test_entrada(unittest.TestCase)
	def test_criar_entrada(self):
		entrada1 = Entrada("Almox.Norte","Camisa Azul",10) #A sequência é: Nome do almox., produto e quantidade. A data é gerada automaticamente pela classe Entrada
		entrada1.almoxarifado |should| equal_to("Almox.Norte")
		entrada1.produto |should| equal_to("Camiza Azul")
		entrada1.quantidade |should| equal_to(10)
		entrada1.data |should| equal_to(date.today())
		
if __name__=="__main__":
	unittest.main()
