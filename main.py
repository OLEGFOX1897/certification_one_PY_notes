import interface_module
import save_load_csv
list_in=save_load_csv.load_notes()
interface_module.main_menu(list_in)