from exos import exos

# Входные данные для поключения
account = {
    "host": "ip-address",
    "port": 22,
    "login": "admin",
    "pass": "admin",
}

# Парсинг файл
def parse_file(path_file):
    buffer_data = []
    with open(path_file, 'r') as my_file:
        data = my_file.read()
        buffer_data = data.split('\n')
    return buffer_data


def program():
    device = exos(account['host'], account['port'], account['login'], account['pass'])

    # Открыть сессию
    device.init_connect_device()
    # Список vlan c устройства
    list_vlan_dev = device.get_vlans_device()
    # Закрыть сессию
    device.close_connect_device()

    data = parse_file('s1.txt')
    index = 0
    #Проходим по всем существующим Vlan находящиеся на Switch
    for i_vlan in list_vlan_dev:
        #Проходим по всем Vlan находящиеся в текстовом файле
        for k_vlan in data:
            if int(i_vlan[1]) == int(k_vlan.split(',')[1]):
                try:
                    data.pop(index)
                except IndexError:
                    pass
            index = index + 1

    # Открыть сессию
    device.init_connect_device()
    # Список vlan c устройства
    for vlan in data:
        device.create_vlan(vlan.split(',')[0], vlan.split(',')[1])
    # Закрыть сессию
    device.close_connect_device()
    print("The task is completed!!!")


if __name__ == '__main__':
    program()
