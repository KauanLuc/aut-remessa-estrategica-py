import subprocess
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

filezilla_ppk_file = os.getenv("FILEZILLA_PPK_FILE")
current_date = datetime.today().strftime('%Y%m%d')
remessa_estrategia_file = f'POLITICA_POP_UP/{current_date}*.txt'

def extract_remote_file():
    destination_path = fr'{os.getenv("DESTINATION_PATH")}'

    commands = [
        'C:\\Users\\kauan.lucena\\Desktop\\WinSCP\\WinSCP.com',
        '/command',
        f'open sftp://{os.getenv("SFTP_IP")} -privatekey={filezilla_ppk_file} -hostkey=*',
        f'get {remessa_estrategia_file} {destination_path}',
        'exit'
    ]

    return print(subprocess.run(commands, capture_output=True, text=True).stdout)
        
def move_remote_file():
    commands = [
        'C:\\Users\\kauan.lucena\\Desktop\\WinSCP\\WinSCP.com',
        '/command',
        f'open sftp://{os.getenv("SFTP_IP")} -privatekey={filezilla_ppk_file} -hostkey=*',
        f'mv {remessa_estrategia_file} PROCESSADOS/',
        'exit'
    ]

    subprocess.run(commands) 