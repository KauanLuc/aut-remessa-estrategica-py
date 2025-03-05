import sftp_manager as sftpm
import gui_manager as guim

extracted = sftpm.extract_remote_file()

if extracted:
    sftpm.move_remote_file()
    guim.schedule_remessa()

guim.show_result(extracted)