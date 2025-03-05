import pyautogui as pygui
import time
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

pygui.PAUSE = 3

# coordenada x, y botão 'Operacional' = Point(x=413, y=153)
# coordenada x, y campo 'Processos Agendados' = Point(x=379, y=450)
# coordenada x, y campo 'Agendar Importação de Carga' = Point(x=625, y=613)
# coordenada x, y campo 'Data Agendamento' = Point(x=531, y=140)
# coordenada x, y campo 'E-mail [...]' = Point(x=437, y=236)
# coordenada x, y campo 'Empresa' = Point(x=402, y=405)
# coordenada x, y campo 'Empresa' empresa VVarejo 18 = Point(x=346, y=516)
# coordenada x, y campo ' ' = Point(x=373, y=442)
# coordenada x, y campo ' ' arquivo Remessa Estrategica = Point(x=335, y=538)
# coordenada x, y botão 'Agendar' = Point(x=811, y=596)
# coordenada x, y botão 'Ok' - Confirmar agendamento = Point(x=520, y=414)
# coordenada x, y ícone do Teams = Point(x=442, y=742)

def show_status_task():
    pygui.alert(title="SUCESSO", text="Tarefa funcionando!")

def show_coordinates():
    time.sleep(5)
    print(pygui.position())

#show_coordinates()

def schedule_remessa():
    pygui.hotkey('Win', 'r')
    pygui.typewrite(fr'{os.getenv("NECTAR_SERVICES")}')
    pygui.hotkey('Enter')
    pygui.hotkey('Tab')
    pygui.hotkey('Tab')
    pygui.typewrite('Enter')
    pygui.typewrite('kauan')
    pygui.hotkey('Tab')
    pygui.typewrite(os.getenv("PASSWORD"))
    pygui.hotkey(['Tab', 'Enter'])

    #Operacional
    pygui.click(x=413, y=153, button='left')

    #Processos Agendados
    pygui.click(x=379, y=450, button='left')
    time.sleep(5)

    #Agendar importação de carga
    pygui.click(x=625, y=613, button='left')

    #Email
    pygui.click(x=437, y=236, button='left')
    pygui.typewrite('kauan.lucena@grupotalentos.com.br')

    #Empresa
    pygui.click(x=402, y=405, button='left')
    #VVarejo 18
    pygui.click(x=346, y=516, button='left')

    #' '
    pygui.click(x=373, y=442, button='left')
    #Arquivo Remessa Estrategica
    pygui.click(x=335, y=538, button='left')

    #Data Agendamento
    pygui.click(x=531, y=140, button='left')
    schedule_hour = datetime.now() + timedelta(minutes=3)
    pygui.typewrite(f'{schedule_hour.minute:02d}')

    #Agendar
    pygui.click(x=811, y=596, button='left')

    #Ok
    pygui.click(x=520, y=414, button='left')

    time.sleep(2)

    #Teams
    pygui.click(x=442, y=742, button='left')

def send_message():
    pass

def show_result(extracted: bool):
    if extracted:    
        pygui.alert(title='Agendamento concluído', text='REMESSA ESTRATÉGICA agendada com sucesso.')
    else:
        pygui.alert(title='Falha no agendamento', text='Ocorreu uma falha durante o processo de agendamento.')