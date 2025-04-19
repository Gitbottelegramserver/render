from states import module1, module2, module3, module4, module5, module6, module7

def get_module_content(module_number: str) -> dict:
    modules = {
        "1": {"description": module1.description, "buttons": module1.buttons},
        "2": {"description": module2.description, "buttons": module2.buttons},
        "3": {"description": module3.description, "buttons": module3.buttons},
        "4": {"description": module4.description, "buttons": module4.buttons},
        "5": {"description": module5.description, "buttons": module5.buttons},
        "6": {"description": module6.description, "buttons": module6.buttons},
        "7": {"description": module7.description, "buttons": module7.buttons},
    }
    return modules.get(module_number, {"description": "Введите номер модуля от 1 до 7.", "buttons": []})
