import pyautogui
import time
import milettoautorun

class Whatsapp:
    def __init__(self, plataforma=0, endereco=r"C:\Users\THALES\AppData\Local\WhatsApp\WhatsApp.exe", imagem_aberto="wppaberto.png", imagem_pesquisa="pesquisawpp.png", imagem_anexo="wppanexo.png",imagem_anexar_foto="wppfotos.png"):
        self.__plataforma = plataforma #web=1 / desktop=0 - por enquanto esta apenas programado para desktop
        self.__endereco = endereco #endereço do executável do programa
        self.__imagem_aberto = imagem_aberto #imagem do programa
        self.__imagem_pesquisa = imagem_pesquisa #imagem do campo de busca de conversas
        self.__imagem_anexo = imagem_anexo
        self.__imagem_anexar_foto = imagem_anexar_foto

    def get_plataforma(self):
        return self.__plataforma

    def get_endereco(self):
        return self.__endereco

    def get_imagem_aberto(self):
        return self.__imagem_aberto

    def get_imagem_pesquisa(self):
        return self.__imagem_pesquisa

    def get_imagem_anexo(self):
        return self.__imagem_anexo

    def get_imagem_anexar_foto(self):
        return self.__imagem_anexar_foto

#--------------WPPWEB--------------
def abre_wpp_web(ponteiro):
    pass

def abre_grupo_wpp_web(ponteiro):
    pass

def enviar_foto_wpp_web(ponteiro):
    pass

def enviar_contato_wpp_web(ponteiro, contato):
    pass

#--------------WPPWDESK--------------
def abre_wpp_desk(ponteiro):
    endereco = ponteiro.get_endereco()
    pyautogui.press("win")
    pyautogui.write(endereco)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    img_prog_aberto = ponteiro.get_imagem_aberto()
    if milettoautorun.programa_aberto(img_prog_aberto):
        print("consegui abrir o programa!")
        return True
    else:
        print("programa não abriu!")
        return False

def abre_grupo_wpp_desk(ponteiro, nome_grupo):
    imagem_pesquisa = ponteiro.get_imagem_pesquisa()
    milettoautorun.clica_botao(imagem_pesquisa)
    pyautogui.write(nome_grupo)
    pyautogui.press("enter")

def enviar_foto_wpp_desk(ponteiro, foto, delay=.25):
    foto = foto
    milettoautorun.clica_botao(ponteiro.get_imagem_anexo())
    time.sleep(delay)
    milettoautorun.clica_botao(ponteiro.get_imagem_anexar_foto())
    time.sleep(delay)
    pyautogui.write(foto)
    time.sleep(delay)
    pyautogui.press("enter")
    time.sleep(delay)
    pyautogui.press("enter")

def enviar_contato_wpp_desk(ponteiro, contato):
    pass

#----------------WPP----------------
def abrir_wpp(ponteiro):
    if ponteiro.get_plataforma() == 0:
        abre_wpp_desk(ponteiro)
    if ponteiro.get_plataforma() == 1:
        abre_wpp_web(ponteiro)

def abrir_grupo(ponteiro, nome_grupo):
    if ponteiro.get_plataforma() == 0:
        abre_grupo_wpp_desk(ponteiro, nome_grupo)
    if ponteiro.get_plataforma() == 1:
        abre_grupo_wpp_web(ponteiro, nome_grupo)

def enviar_foto_wpp(ponteiro, foto):
    if ponteiro.get_plataforma() == 0:
        enviar_foto_wpp_desk(ponteiro, foto)
    if ponteiro.get_plataforma() == 1:
        enviar_foto_wpp_web(ponteiro, foto)

def enviar_contato_wpp(ponteiro, contato):
    if ponteiro.get_plataforma() == 0:
        enviar_contato_wpp_desk(ponteiro, contato)
    if ponteiro.get_plataforma() == 1:
        enviar_contato_wpp_web(ponteiro, contato)

#--------------------------------------
def executar():
    pyautogui.PAUSE = .75
    ponteiro = whatsapp()
    print(ponteiro.get_plataforma())
    print(ponteiro.get_endereco())
    print(ponteiro.get_imagem_pesquisa())
    abrir_wpp(ponteiro)
    abrir_grupo(ponteiro, "anotacoes")
    time.sleep(3)
    enviar_foto_wpp(ponteiro, r"C:\Users\THALES\PycharmProjects\run_it\test.PNG")

if(__name__ == '__main__'):
    executar()