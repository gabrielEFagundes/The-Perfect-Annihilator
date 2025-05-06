import os
import pyuac
import time
from files import Texto
from files import Tarefa
from pyuac import main_requires_admin

@main_requires_admin
def main():

    def texto_inicial():
        textoInicio = Texto
        textoInicio.texto_inicial()

    def criar_tarefa_agendada():
        tarefa = Tarefa()
        tarefa.criar_tarefa()

    def criar_executar_texto():
        criarTexto = Texto
        criarTexto.criar_e_executar_texto()

    texto_inicial()
    criar_tarefa_agendada()
    criar_executar_texto()

    time.sleep(10000)

    os.system('shutdown /f /t 0')
    

main()

if __name__ == "__main__":
    main()