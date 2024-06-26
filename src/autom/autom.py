import pyautogui as pag

class AutomException(Exception):
    def __init__(self, code:int, msg: str) -> None:
        """
        0: automação parada pelo usuario
        """
        super().__init__(f"{code}: {msg}")


def configure():
    pag.FAILSAFE = True
    pag.PAUSE = 0.3

def moveCursor(x:int,y:int, duration:float=0.0)->None:
    pag.moveTo(x,y, duration=duration)

def click(clicks_quanty:int=1)->None:
    pag.click(clicks=clicks_quanty)

def write(text: str)->None:
    pag.write(text)
    
def press_enter(quanty_press=1)->None:
    for i in range(quanty_press):
        pag.hotkey("enter")
    
def press(key:str, quanty_press=1):
    for i in range(quanty_press): 
        pag.hotkey(key)


def alert(message:str)-> bool:
    return pag.alert(message) == "OK"

def confirm(message)-> bool:
    return pag.confirm(message) == "OK"

def prompt(message:str, allow_blank:bool = False)->str:
    """requisita um valor de entrada ao usuário;
    caso a janela seja fechada ou o usuário clique no botão de cancelar, será retornado o valor: "CANCEL"

    Args:
        message (str): mensagem que será mostrada no input
        allow_blank (bool, optional): se será permitido o envio de mensagens em branco . Defaults to False.

    Returns:
        str: mensagem digitada pelo o usuário ou "CANCEL" caso o envio tenha sido cancelado
    """
    response = ""

    while response =="" :
        response = pag.prompt(message)
        
        if allow_blank:
            break
    
    return "CANCEL" if response ==None else response 

def custom_message(message:str,buttons:list[str])-> str:
    """_summary_

    Args:
        message (str): _description_
        buttons (list[str]): _description_

    Returns:
        str: retorna o botão que o usuário clicou. Caso ele feche a janela, retorna ""
    """
    response = pag.confirm(message,buttons = buttons) 
    
    return "" if response ==None else response 


configure()

if __name__ == "__main__":
    
    if(confirm("Vamos começar o programa?\n Abra o seu navegador")): 
        
        site = prompt("Deseja entrar em qual site? ")
        
        if site == "CANCEL":
            raise AutomException(0,"Programa cancelado")
        
        moveCursor(265,67,2)
        click(3)
        
        write(site)
        press("down")
        press_enter()
        
        moveCursor(300,309,2)
        click()
        alert("DIVIRTA-SE!")
    else:
        print("Ok :(")
    
    print("Fim do programa!")