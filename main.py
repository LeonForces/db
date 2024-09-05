from mysql.connector import connect, Error
from getpass import getpass
import PySimpleGUI as sg


# основное окно
def main_layout():
    client_layout = [
        [sg.Text('Клиенты')],
        [sg.Button('Добавить клиента', size=(25, 2))],
        [sg.Button('Изменить клиента', size=(25, 2))],
        [sg.Button('Удалить клиента', size=(25, 2))],
        [sg.Button('Просмотреть всех клиентов', size=(25, 2))]
    ]
    reservation_layout = [
        [sg.Text('Бронирование')],
        [sg.Button('Добавить бронирование', size=(25, 2))],
        [sg.Button('Изменить бронирование', size=(25, 2))],
        [sg.Button('Удалить бронирование', size=(25, 2))],
        [sg.Button('Просмотреть все бронирования', size=(25, 2))]
    ]
    rental_layout = [
        [sg.Text('Аренды')],
        [sg.Button('Добавить аренду', size=(25, 2))],
        [sg.Button('Изменить аренду', size=(25, 2))],
        [sg.Button('Удалить аренду', size=(25, 2))],
        [sg.Button('Просмотреть все аренды', size=(25, 2))]
    ]
    supplement_layout = [
        [sg.Text('Дополнительные функции')],
        [sg.Button('Резервировать оборудование', size=(25, 2))],
        [sg.Button('Арендовать оборудование', size=(25, 2))],
        [sg.Button('Оформить страховку', size=(25, 2))],
        [sg.Button('Поиск клиента', size=(25, 2))]
    ]
    result_layout = [
        [sg.Column(client_layout + reservation_layout), sg.Column(rental_layout + supplement_layout)]
    ]
    # view_layout = [
    #      [sg.Text('Вывести данные по отелям, зданиям')],
    #      [sg.Button('Вывести')]
    # ]
    #result = [sg.Column(client_layout, element_justification='c'), sg.Column(reservation_layout, element_justification='c'), sg.Column(rental_layout, element_justification='c')]
    # return client_layout + reservation_layout + rental_layout
    return result_layout


# окно добавления клиента
def add_client():
    return [
        [sg.Text('Введите данные:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='clientID')],
        [sg.Text('ФИО', size=(15, 2)), sg.InputText(key='clientName')],
        [sg.Text('Дата рождения', size=(15, 2)), sg.InputText(key='clientBirthday')],
        [sg.Text('Номер водительских прав', size=(15, 2)), sg.InputText(key='clientDrivingLicense')],
        [sg.Text('Дата получения водительских прав', size=(15, 2)), sg.InputText(key='clientIssueDate')],
        [sg.Button('Добавить'), sg.Button('Отмена')]
    ]


# окно изменения клиента
def edit_client():
    return [
        [sg.Text('Введите данные:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='clientID')],
        [sg.Text('ФИО', size=(15, 2)), sg.InputText(key='clientName')],
        [sg.Text('Дата рождения', size=(15, 2)), sg.InputText(key='clientBirthday')],
        [sg.Text('Номер водительских прав', size=(15, 2)), sg.InputText(key='clientDrivingLicense')],
        [sg.Text('Дата получения водительских прав', size=(15, 2)), sg.InputText(key='clientIssueDate')],
        [sg.Button('Изменить')]
    ]


# окно удаления клиента
def delete_client():
    return [
        [sg.Text('Введите номер:', size=(15, 2))],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='clientID')],
        [sg.Button('Удалить')]
    ]


# сотрудники
# окно добавления бронирования
def add_reservation():
    address = []
    db_query = "SELECT street_address FROM location"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            address.append(list(row))
    category = []
    db_query = "SELECT name FROM car_category"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            category.append(list(row))
    users = []
    db_query = "SELECT name FROM customer"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            users.append(list(row))
    return [
        [sg.Text('Введите данные:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='reservationID')],
        [sg.Text('Место получения', size=(15, 2)), sg.OptionMenu(address, key='reservationPickUp')],
        [sg.Text('Место остановки', size=(15, 2)), sg.OptionMenu(address, key='reservationDropOff')],
        [sg.Text('Категория автомобиля', size=(15, 2)), sg.OptionMenu(category, key='reservationCategoryAuto')],
        [sg.Text('Имя клиента', size=(15, 2)), sg.OptionMenu(users, key='reservationClient')],
        [sg.Button('Добавить'), sg.Button('Отмена')]
    ]


# окно изменения бронирования
def edit_reservation():
    address = []
    db_query = "SELECT street_address FROM location"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            address.append(list(row))
    category = []
    db_query = "SELECT name FROM car_category"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            category.append(list(row))
    users = []
    db_query = "SELECT name FROM customer"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            users.append(list(row))
    return [
        [sg.Text('Введите данные:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='reservationID')],
        [sg.Text('Место получения', size=(15, 2)), sg.OptionMenu(address, key='reservationPickUp')],
        [sg.Text('Место остановки', size=(15, 2)), sg.OptionMenu(address, key='reservationDropOff')],
        [sg.Text('Категория автомобиля', size=(15, 2)), sg.OptionMenu(category, key='reservationCategoryAuto')],
        [sg.Text('Имя клиента', size=(15, 2)), sg.OptionMenu(users, key='reservationClient')],
        [sg.Button('Изменить')]
    ]


# окно удаления бронирования
def delete_reservation():
    return [
        [sg.Text('Введите номер:', size=(15, 2))],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='reservationID')],
        [sg.Button('Удалить')]
    ]


# услуга
# окно добавления аренды
def add_rental():
    address = []
    db_query = "SELECT street_address FROM location"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            address.append(list(row))
    cars = []
    db_query = "SELECT model FROM car"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            cars.append(list(row))
    users = []
    db_query = "SELECT name FROM customer"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            users.append(list(row))
    return [
        [sg.Text('Введите данные:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='rentalID')],
        [sg.Text('Имя клиента', size=(15, 2)), sg.OptionMenu(users, key='rentalClient')],
        [sg.Text('Автомобиль', size=(15, 2)), sg.OptionMenu(cars, key='rentalAuto')],
        [sg.Text('Место получения', size=(15, 2)), sg.OptionMenu(address, key='rentalPickUp')],
        [sg.Text('Место остановки', size=(15, 2)), sg.OptionMenu(address, key='rentalDropOff')],
        [sg.Text('Дата получения', size=(15, 2)), sg.InputText(key='rentalStart')],
        [sg.Text('Дата остановки', size=(15, 2)), sg.InputText(key='rentalEnd')],
        [sg.Button('Добавить'), sg.Button('Отмена')]
    ]


# окно изменения аренды
def edit_rental():
    address = []
    db_query = "SELECT street_address FROM location"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            address.append(list(row))
    cars = []
    db_query = "SELECT model FROM car"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            cars.append(list(row))
    users = []
    db_query = "SELECT name FROM customer"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            users.append(list(row))
    return [
        [sg.Text('Введите данные:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='rentalID')],
        [sg.Text('Имя клиента', size=(15, 2)), sg.OptionMenu(users, key='rentalClient')],
        [sg.Text('Автомобиль', size=(15, 2)), sg.OptionMenu(cars, key='rentalAuto')],
        [sg.Text('Место получения', size=(15, 2)), sg.OptionMenu(address, key='rentalPickUp')],
        [sg.Text('Место остановки', size=(15, 2)), sg.OptionMenu(address, key='rentalDropOff')],
        [sg.Text('Дата получения', size=(15, 2)), sg.InputText(key='rentalStart')],
        [sg.Text('Дата остановки', size=(15, 2)), sg.InputText(key='rentalEnd')],
        [sg.Button('Изменить')]
    ]


# окно удаления аренды
def delete_rental():
    return [
        [sg.Text('Введите номер:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='rentalID')],
        [sg.Button('Удалить')]
    ]

def reserve_equipment():
    equipment_category = []
    db_query = "SELECT name FROM equipment_category"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            equipment_category.append(list(row))
    return [
        [sg.Text('Введите номер:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='reservID')],
        [sg.Text('id бронирования', size=(15, 2)), sg.InputText(key='reservationID')],
        [sg.Text('Оборудование', size=(15, 2)), sg.OptionMenu(equipment_category, key='categoryEquipment')],
        [sg.Button('Добавить'), sg.Button('Отмена')]
    ]

def rent_equipment():
    return [
        [sg.Text('Введите номер:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='rentID')],
        [sg.Text('id автомобиля', size=(15, 2)), sg.InputText(key='carID')],
        [sg.Text('id оборудования', size=(15, 2)), sg.InputText(key='equipmentID')],
        [sg.Text('Дата получения', size=(15, 2)), sg.InputText(key='equipmentStart')],
        [sg.Text('Дата возврата', size=(15, 2)), sg.InputText(key='equipmentEnd')],
        [sg.Button('Добавить'), sg.Button('Отмена')]
    ]

def add_insurance():
    insurances = []
    db_query = "SELECT name FROM insurance"
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        for row in cursor:
            insurances.append(list(row))
    return [
        [sg.Text('Введите номер:')],
        [sg.Text('id', size=(15, 2)), sg.InputText(key='rentalInsuranceID')],
        [sg.Text('id аренды', size=(15, 2)), sg.InputText(key='rentalID')],
        [sg.Text('Страховка', size=(15, 2)), sg.OptionMenu(insurances, key='insuranceID')],
        [sg.Button('Добавить'), sg.Button('Отмена')]
    ]

def find_client():
    return [
        [sg.Text('Введите:')],
        [sg.Text('Имя клиента', size=(15, 2)), sg.InputText(key='findName')],
        [sg.Button('Найти'), sg.Button('Отмена')]
    ]

try:
    with connect(
            host="localhost",
            user="root",
            password="",
            database="car-rental",
    ) as connection:

        print("\n")

        def show_client():
            result = []
            db_query = "SELECT * FROM customer"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "ФИО", "Дата рождения", "Номер водительских прав", "Дата получения лицензии"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
                [sg.Button('Отмена')]
            ]
            return content

        def show_reservation():
            result = []
            db_query = "SELECT r.id, l1.city, l2.city, cc.name, c.name FROM reservation r, customer c, car_category cc, location l1, location l2 WHERE r.customer_id = c.id AND r.car_category_id = cc.id AND r.pick_up_location_id = l1.id AND r.drop_off_location_id = l2.id"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "Место получения", "Место остановки", "Категория автомобиля", "Имя клиента"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
                [sg.Button('Отмена')]
            ]
            return content

        def show_rental():
            result = []
            db_query = "SELECT r.id, c.name, car.model, l1.city, l2.city, r.start_date, r.end_date FROM rental r, customer c, car, location l1, location l2 WHERE r.customer_id = c.id AND r.car_id = car.id AND r.pick_up_location_id = l1.id AND r.drop_off_location_id = l2.id"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "Имя клиента", "Модель автомобиля", "Место получения", "Место остановки", "Дата получения", "Дата остановки"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
                [sg.Button('Отмена')]
            ]
            return content

        def show_user():
            result = []
            str = values['findName']
            db_query = f"SELECT * FROM customer WHERE name LIKE '%{str}%'"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "ФИО", "Дата рождения", "Номер водительских прав", "Дата получения лицензии"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
            ]
            return content

        """def show_car_category():
            result = []
            db_query = "SELECT * FROM car_category"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "Название", "Стоимость"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
                [sg.Button('Отмена')]
            ]
            return content

        def show_client_id():
            result = []
            db_query = "SELECT id, name FROM customer"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "ФИО"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
                [sg.Button('Отмена')]
            ]
            return content

        def show_location():
            result = []
            db_query = "SELECT id, street_address, city FROM location"
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                for row in cursor:
                    result.append(list(row))
            print(result)
            header = ["id", "Адресс", "Город"]
            content = [
                [sg.Table(values=result, headings=header, max_col_width=35,
                          auto_size_columns=True, display_row_numbers=False)],
                [sg.Button('Отмена')]
            ]
            return content"""

        sg.theme('DarkTeal9')  # Add a touch of color
        window = sg.Window("Прокат автомобилей", main_layout(), margins=(150, 50))  # Create the Window

        while True:  # Event Loop to process "events" and get the "values" of the inputs
            event, values = window.read()
            if event == sg.WIN_CLOSED:  # if user closes window
                break
            # выбор действия
            if event == "Добавить клиента":
                window.close()
                window = sg.Window("Добавить клиента", add_client(), margins=(150, 50))  # Create the Window
                action = 11
            if event == "Изменить клиента":
                window.close()
                window = sg.Window("Изменить клиента", edit_client() + show_client(), margins=(150, 50))
                action = 12
            if event == "Удалить клиента":
                window.close()
                window = sg.Window("Удалить клиента", delete_client() + show_client(), margins=(150, 50))
                action = 13
            if event == "Просмотреть всех клиентов":
                window.close()
                window = sg.Window("Просмотреть клиентов", show_client(), margins=(150, 50))
                action = 14

            if event == "Добавить бронирование":
                window.close()
                window = sg.Window("Добавить бронирование", add_reservation(), margins=(150, 50))
                action = 21
            if event == "Изменить бронирование":
                window.close()
                window = sg.Window("Изменить бронирование", edit_reservation() + show_reservation(), margins=(150, 50))
                action = 22
            if event == "Удалить бронирование":
                window.close()
                window = sg.Window("Удалить бронирование", delete_reservation() + show_reservation(), margins=(150, 50))
                action = 23
            if event == "Просмотреть все бронирования":
                window.close()
                window = sg.Window("Все бронирования", show_reservation(), margins=(150, 50))
                action = 24

            if event == "Добавить аренду":
                window.close()
                window = sg.Window("Добавить аренду", add_rental(), margins=(150, 50))  # Create the Window
                action = 31
            if event == "Изменить аренду":
                window.close()
                window = sg.Window("Изменить аренду", edit_rental() + show_rental(), margins=(150, 50))
                action = 32
            if event == "Удалить аренду":
                window.close()
                window = sg.Window("Удалить аренду", delete_rental() + show_rental(), margins=(150, 50))
                action = 33
            if event == "Просмотреть все аренды":
                window.close()
                window = sg.Window("Все аренды", show_rental(), margins=(150, 50))
                action = 34

            if event == "Резервировать оборудование":
                window.close()
                window = sg.Window("Резервировать оборудование", reserve_equipment(), margins=(150, 50))
                action = 41
            if event == "Арендовать оборудование":
                window.close()
                window = sg.Window("Арендовать оборудование", rent_equipment(), margins=(150, 50))
                action = 51
            if event == "Оформить страховку":
                window.close()
                window = sg.Window("Оформить страховку", add_insurance(), margins=(150, 50))
                action = 61
            if event == "Поиск клиента":
                window.close()
                window = sg.Window("Поиск клиента", find_client(), margins=(150, 50))
            # if event == "Вывести":
            #     window.close()
            #     window = sg.Window("Все услуги", show_view(), margins=(150, 50))

            # adding code

            if event == "Добавить":
                if action == 11:


                    db = "customer"
                    add_query = "INSERT " + db + " VALUES(" + values['clientID'] \
                                + ", \"" + values['clientName'] + "\", \"" + values['clientBirthday'] \
                                + "\", \"" + values['clientDrivingLicense'] + "\", \"" + values['clientIssueDate'] + "\")"
                    with connection.cursor() as cursor:
                        cursor.execute(add_query)
                        connection.commit()

                if action == 21:
                    val = []
                    str = values['reservationPickUp']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['reservationDropOff']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['reservationCategoryAuto']
                    db_query = "SELECT id FROM car_category WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['reservationClient']
                    db_query = "SELECT id FROM customer WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    db = "reservation"
                    add_query = "INSERT " + db + " VALUES(" + values['reservationID'] \
                                + ", " + val[0][1:-2] + ", " + val[1][1:-2] \
                                + ", " + val[2][1:-2] \
                                + ", " + val[3][1:-2] + ")"
                    with connection.cursor() as cursor:
                        cursor.execute(add_query)
                        connection.commit()

                if action == 31:
                    val = []
                    str = values['rentalClient']
                    db_query = "SELECT id FROM customer WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['rentalAuto']
                    db_query = "SELECT id FROM car WHERE model = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['rentalPickUp']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['rentalDropOff']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))


                    db = "rental"
                    add_query = "INSERT " + db + " VALUES(" + values['rentalID'] \
                                + ", " + val[0][1:-2] + ", " + val[1][1:-2] \
                                + ", " + val[2][1:-2] + ""\
                                + ", " + val[3][1:-2] + ""\
                                + ", \'" + values['rentalStart'] + "\'"\
                                + ", \'" + values['rentalEnd'] + "\')"
                    with connection.cursor() as cursor:
                        cursor.execute(add_query)
                        connection.commit()
                    ##

                if action == 41:
                    val = []
                    str = values['categoryEquipment']
                    db_query = "SELECT id FROM equipment_category WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    db = "reservation_equipment"
                    add_query = "INSERT " + db + " VALUES("+ values['reservID'] + ", " + values['reservationID'] \
                                + ", " + val[0][1:-2] + ")"
                    with connection.cursor() as cursor:
                        cursor.execute(add_query)
                        connection.commit()

                if action == 51:

                    db = "car_equipment"
                    add_query = "INSERT " + db + " VALUES(" + values['rentID'] + ", " + values['equipmentID'] \
                                + ", " + values['carID'] + ", '" + values['equipmentStart'] \
                                + "', '" + values['equipmentEnd'] + "')"
                    with connection.cursor() as cursor:
                        cursor.execute(add_query)
                        connection.commit()

                if action == 61:
                    val = []
                    str = values['insuranceID']
                    db_query = "SELECT id FROM insurance WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    db = "rental_insurance"
                    add_query = "INSERT " + db + " VALUES(" + values['rentalInsuranceID'] + ", " + values['rentalID'] \
                                + ", " + val[0][1:-2] + ")"
                    with connection.cursor() as cursor:
                        cursor.execute(add_query)
                        connection.commit()

                print(add_query)
                window.close()
                window = sg.Window("Прокат автомобилей", main_layout(), margins=(100, 50))  # Create the Window
                db = ""
                action = 0
                print("data was added")

            # editing code
            if event == "Изменить":
                if action == 12:
                    db = "client"
                    edit_query = "UPDATE " + db + " SET " \
                                 + "name = '" + values['clientName'] \
                                 + "', birth_date = '" + values['clientBirthday'] \
                                 + "', driving_license_number = '" + values['clientDrivingLicense'] \
                                 + "', driving_license_issue_dt = '" + values['clientIssueDate'] \
                                 + "' WHERE" + " id = " + values['clientID']
                    with connection.cursor() as cursor:
                        cursor.execute(edit_query)
                        connection.commit()

                if action == 22:
                    val = []
                    str = values['reservationPickUp']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['reservationDropOff']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['reservationCategoryAuto']
                    db_query = "SELECT id FROM car_category WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['reservationClient']
                    db_query = "SELECT id FROM customer WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    db = "reservation"
                    edit_query = "UPDATE " + db + " SET " \
                                 + "pick_up_location_id = " + val[0][1:-2] \
                                 + ", drop_off_location_id = " + val[1][1:-2] \
                                 + ", car_category_id = " + val[2][1:-2] \
                                 + ", customer_id = '" + val[3][1:-2] \
                                 + "' WHERE" + " id = " + values['reservationID']
                    with connection.cursor() as cursor:
                        cursor.execute(edit_query)
                        connection.commit()

                if action == 32:
                    val = []
                    str = values['rentalClient']
                    db_query = "SELECT id FROM customer WHERE name = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['rentalAuto']
                    db_query = "SELECT id FROM car WHERE model = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['rentalPickUp']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))
                    str = values['rentalDropOff']
                    db_query = "SELECT id FROM location WHERE street_address = " + str[1:-2]
                    with connection.cursor() as cursor:
                        cursor.execute(db_query)
                        for row in cursor:
                            val.append("{}".format(row))

                    db = "rental"
                    edit_query = "UPDATE " + db + " SET " \
                                 + "customer_id = " + val[0][1:-2] \
                                 + ", car_id = " + val[1][1:-2] \
                                 + ", pick_up_location_id = " + val[2][1:-2] \
                                 + ", drop_off_location_id = " + val[3][1:-2] \
                                 + ", start_date = '" + values['rentalStart'] \
                                 + "', end_date = '" + values['rentalEnd'] \
                                 + "' WHERE" + " id = " + values['rentalID']
                    print(edit_query)
                    with connection.cursor() as cursor:
                        cursor.execute(edit_query)
                        connection.commit()
                window.close()
                window = sg.Window("Прокат автомобилей", main_layout(), margins=(100, 50))  # Create the Window
                db = ""
                action = 0
                print("data was edited")

            # deleting code
            if event == "Удалить":
                if action == 13:
                    db = "customer"
                    delete_query = "DELETE FROM " + db + " WHERE " \
                                   + "(id = " + values['clientID'] + ")"
                    with connection.cursor() as cursor:
                        cursor.execute(delete_query)
                        connection.commit()
                if action == 23:
                    db = "reservation"
                    delete_query = "DELETE FROM " + db + " WHERE " \
                                   + "(id = " + values['reservationID'] + ")"
                    with connection.cursor() as cursor:
                        cursor.execute(delete_query)
                        connection.commit()
                if action == 33:
                    db = "rental"
                    delete_query = "DELETE FROM " + db + " WHERE " \
                                   + "(id = " + values['rentalID'] + ")"
                    with connection.cursor() as cursor:
                        cursor.execute(delete_query)
                        connection.commit()
                print(delete_query)
                window.close()
                window = sg.Window("Прокат автомобилей", main_layout(), margins=(100, 50))  # Create the Window
                db = ""
                action = 0
                print("data was deleted")

            if event == "Отмена":
                window.close()
                window = sg.Window("Прокат автомобилей", main_layout(), margins=(100, 50))  # Create the Window
                db = ""
                action = 0
                print("canceled")

            if event == "Найти":
                window.close()
                window = sg.Window("Поиск клиента", find_client() + show_user(), margins=(150, 50))

        window.close()

except Error as e:
    print("Error:", e)
