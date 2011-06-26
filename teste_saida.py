#coding:utf-8
import unittest
from should_dsl import should
from datetime import date

class Test_saida(unittest.TestCase)
	def test_criar_saida(self):
		saida1 = Saida( "Almox.Central","Jaqueta Jeans",2) #A sequência é: Nome do almox., produto e quantidade. A data é gerada automaticamente pela classe Saida
		saida1.almoxarifado |should| equal_to("Almox.Central")
		saida1.produto |should| equal_to("Jaqueta Jeans")
		saida1.quantidade |should| equal_to(2)
		saida1.data |should| equal_to(date.today())
		
if __name__=="__main__":
	unittest.main()
