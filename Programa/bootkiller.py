import os
import pyuac
from files import Texto
from files import Tarefa
from files import Operacoes
from pyuac import main_requires_admin

@main_requires_admin
def main():

    def mensagem():
        aviso = Operacoes
        aviso.aviso()

    mensagem()

    def texto_inicial():
        textoInicio = Texto
        textoInicio.texto_inicial()

    def criar_tarefa_agendada():
        tarefa = Tarefa()
        tarefa.criar_tarefa()

    def criar_executar_texto():
        criarTexto = Texto
        criarTexto.criar_e_executar_texto()

    def turnOff():
        desligar = Operacoes
        desligar.desligarPc()

    texto_inicial()
    criar_tarefa_agendada()
    criar_executar_texto()
    turnOff()
    

main()

if __name__ == "__main__":
    main()