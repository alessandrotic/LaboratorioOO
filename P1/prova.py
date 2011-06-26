#coding:utf-8

from datetime import date

class Funcionario(object):
    matricula = 0
    def __init__(self, nome, cpf, salario_base):
        Funcionario.matricula = Funcionario.matricula + 1
        self.nome = nome
        validador = Validador()
        if validador.validar_cpf(cpf):
            self.cpf = cpf
        else:
            self.cpf = None
        self.data_admissao = date.today()
        self.data_demissao = None
        self.salario_base = salario_base


class Validador(object):
    def validar_cpf(self, cpf):
        if (len(cpf) == 11) and (cpf.isdigit()):
            return True
        else:
            return False

    def validar_data_demissao(self, data_admissao, data_demissao):
        if data_demissao > data_admissao:
            return True
        else:
            return False

class Empresa(object):
    def __init__(self, razao_social, cnpj):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.quadro_funcionarios = []

    def admitir_funcionario(self, funcionario):
        self.quadro_funcionarios.append(funcionario)

    def demitir_funcionario(self, nome, ano, mes, dia):
        posicao_funcionario = self.buscar_funcionario(nome)
        validador = Validador()
        if validador.validar_data_demissao(self.quadro_funcionarios[posicao_funcionario].data_admissao, date(ano, mes, dia)):
            self.quadro_funcionarios[posicao_funcionario].data_demissao = date(ano, mes, dia)

    def buscar_funcionario(self, nome):
        total_funcionarios = len(self.quadro_funcionarios)
        numero_funcionario = 0
        while (numero_funcionario < total_funcionarios) and (self.quadro_funcionarios[numero_funcionario].nome != nome):
            numero_funcionario = numero_funcionario + 1
        if numero_funcionario == total_funcionarios:
            return None
        else:
            return numero_funcionario

