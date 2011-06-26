#coding:utf-8
import unittest
from should_dsl import should
from prova import Validador, Funcionario, Empresa
from datetime import date

class Test_funcionario(unittest.TestCase):
    def test_criar_funcionario(self):
        Funcionario.matricula = 0
        funcionario1 = Funcionario("Astrobaldo","02966644729", 3000)
        funcionario1.nome |should| equal_to("Astrobaldo")
        funcionario1.cpf |should| equal_to("02966644729")
        funcionario1.matricula |should| equal_to(1)
        funcionario1.data_admissao |should| equal_to(date.today())
        funcionario1.data_demissao |should| equal_to(None)
        funcionario1.salario_base |should| equal_to(3000)
        funcionario2 = Funcionario("Centreflexiano","086", 2000)
        funcionario2.nome |should| equal_to("Centreflexiano")
        funcionario2.cpf |should| equal_to(None)
        funcionario2.matricula |should| equal_to(2)
        funcionario2.data_admissao |should| equal_to(date.today())
        funcionario2.data_demissao |should| equal_to(None)
        funcionario2.salario_base |should| equal_to(2000)

class Test_empresa(unittest.TestCase):
    def test_criar_empresa(self):
        empresa1 = Empresa("Ricks Rocks","12345678900")
        empresa1.razao_social |should| equal_to("Ricks Rocks")
        empresa1.cnpj |should| equal_to("12345678900")
        empresa1.quadro_funcionarios |should| equal_to([])

    def test_admitir_funcionario(self):
        empresa1 = Empresa("Ricks Rocks","12345678900")
        funcionario1 = Funcionario("Astrobaldo","02966644729", 3000)
        empresa1.admitir_funcionario(funcionario1)
        empresa1.quadro_funcionarios[0].nome |should| equal_to("Astrobaldo")
        funcionario2 = Funcionario("Centreflexiano","086", 2000)
        empresa1.admitir_funcionario(funcionario2)
        empresa1.quadro_funcionarios[1].nome |should| equal_to("Centreflexiano")
        empresa1.quadro_funcionarios |should| have(2).itens

    def test_buscar_funcionario(self):
        empresa1 = Empresa("Ricks Rocks","12345678900")
        funcionario1 = Funcionario("Astrobaldo","02966644729", 3000)
        empresa1.admitir_funcionario(funcionario1)
        funcionario2 = Funcionario("Centreflexiano","086", 2000)
        empresa1.admitir_funcionario(funcionario2)
        empresa1.buscar_funcionario("Centreflexiano") |should| equal_to(1)
        empresa1.buscar_funcionario("Benzocriol") |should| equal_to(None)

    def test_demitir_funcionario(self):
        empresa1 = Empresa("Ricks Rocks","12345678900")
        funcionario1 = Funcionario("Astrobaldo","02966644729", 3000)
        empresa1.admitir_funcionario(funcionario1)
        empresa1.demitir_funcionario("Astrobaldo", 2011, 10, 25)
        empresa1.quadro_funcionarios[0].data_demissao |should| equal_to(date(2011, 10, 25))
        funcionario2 = Funcionario("Centreflexiano","086", 2000)
        empresa1.admitir_funcionario(funcionario2)
        empresa1.demitir_funcionario("Centreflexiano", 2010, 3, 25)
        empresa1.quadro_funcionarios[1].data_demissao |should| equal_to(None)

class Test_validador(unittest.TestCase):
    def test_validar_cpf(self):
        validador = Validador()
        validador.validar_cpf("02966644729") |should| equal_to(True)
        validador = Validador()
        validador.validar_cpf("029") |should| equal_to(False)

    def test_validar_data_demissao(self):
        validador = Validador()
        validador.validar_data_demissao(date(2011, 1, 2), date(2011, 4, 1)) |should| equal_to(True)
        validador.validar_data_demissao(date(2011, 4, 1), date(2011, 1, 2)) |should| equal_to(False)


if __name__=="__main__":
    unittest.main()

