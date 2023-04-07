"""
Вариант 4
Кобелев, Касьянов, Кмета, Пермяков
"""

import sqlite3 as sq

with sq.connect('dekanat.db') as con:
    cursor = con.cursor()

    # Создание таблицы facults (факультеты) 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS facults (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

    # Создание таблицы departments (кафедры)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        id_facults INT NOT NULL,
        FOREIGN KEY (id_facults) REFERENCES facults(id)
    )
    """)
    con.commit()

    # Создание таблицы spec (специальности)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS spec (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        id_departments INT NOT NULL,
        FOREIGN KEY (id_departments) REFERENCES departments(id)
    )
    """)
    con.commit()

    # Создание таблицы subject (предметы)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subject (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

    # Создание таблицы sub_form (форма сдачи предмета) 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sub_form (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

    # Создание таблицы curriculum (учебный план)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS curriculum (
        id INT AUTO_INCREMENT PRIMARY KEY,
        spec_id INT NOT NULL,
        subject_id INT NOT NULL,
        sub_form_id INT NOT NULL,
        lec_hours INT NOT NULL,
        pract_hours INT NOT NULL,
        lab_hours INT NOT NULL,
        course_work BOOLEAN NOT NULL,
        FOREIGN KEY (spec_id) REFERENCES spec(id),
        FOREIGN KEY (subject_id) REFERENCES subject(id),
        FOREIGN KEY (sub_form_id) REFERENCES sub_form(id)
    )
    """)
    con.commit()

    # Создание таблицы applicants (абитуриенты)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applicants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        sex VARCHAR(1) NOT NULL,
        birth_date DATE NOT NULL,
        address VARCHAR(255) NOT NULL,
        phone_number VARCHAR(20) NOT NULL,
        email VARCHAR(255) NOT NULL,
        receipt_date DATE NOT NULL,
        speciality VARCHAR(255) NOT NULL
    )
    """)
    con.commit()

with sq.connect('dekanat.db') as con:
    cursor = con.cursor()

    # Заполнение факультетов
    cursor.execute("""INSERT INTO facults VALUES (1, "Информационные технологии")""")
    cursor.execute("""INSERT INTO facults VALUES (2, "Экономика")""")
    con.commit()

    # Заполнение кафедр
    cursor.execute("""INSERT INTO departments VALUES (1, "Информационные системы и программирование", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (2, "Обеспечение информационной безопасности телекоммуникационных систем", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (3, "Обеспечение информационной безопасности автоматизированных систем", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (4, "Сетевое и системное администрирование", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (5, "Инфокоммуникационные сети и системы связи", 1)""")
    cursor.execute("""INSERT INTO departments VALUES (6, "Экономика и бухгалтерский учет", 2)""")
    cursor.execute("""INSERT INTO departments VALUES (7, "Банковское дело", 2)""")
    cursor.execute("""INSERT INTO departments VALUES (8, "Коммерция", 2)""")
    con.commit()

    # Заполнение специальностей
    cursor.execute("""INSERT INTO spec VALUES (1, "Разработчик Web-мультимедийных приложений", 1)""")
    cursor.execute("""INSERT INTO spec VALUES (2, "Разработчик мобильных/десктопных приложений", 1)""")
    cursor.execute("""INSERT INTO spec VALUES (3, "Прикладной программист", 1)""")
    cursor.execute("""INSERT INTO spec VALUES (4, "Безопасник телекоммуникационных систем", 2)""")
    cursor.execute("""INSERT INTO spec VALUES (5, "Безопасник автоматизированных систем", 3)""")
    cursor.execute("""INSERT INTO spec VALUES (6, "Системный администратор", 4)""")
    cursor.execute("""INSERT INTO spec VALUES (7, "Связист", 5)""")
    cursor.execute("""INSERT INTO spec VALUES (8, "Экономист", 6)""")
    cursor.execute("""INSERT INTO spec VALUES (9, "Бухгалтер", 6)""")
    cursor.execute("""INSERT INTO spec VALUES (10, "Банкир", 7)""")
    cursor.execute("""INSERT INTO spec VALUES (11, "Менеджер", 8)""")
    con.commit()

    # Заполнение предметов
    cursor.execute("""INSERT INTO subject VALUES (1, "Основы алгоритмизации и программирования")""")
    cursor.execute("""INSERT INTO subject VALUES (2, "Основы проектирования баз данных")""")
    cursor.execute("""INSERT INTO subject VALUES (3, "Основы web-технологий")""")
    cursor.execute("""INSERT INTO subject VALUES (4, "Компьютерные сети")""")
    cursor.execute("""INSERT INTO subject VALUES (5, "Архитектура аппаратных средств и технические средства информатизации")""")
    cursor.execute("""INSERT INTO subject VALUES (6, "Физическая культура")""")
    cursor.execute("""INSERT INTO subject VALUES (7, "История")""")
    cursor.execute("""INSERT INTO subject VALUES (8, "Стандартизация, сертификация и техническое документирование")""")
    cursor.execute("""INSERT INTO subject VALUES (9, "Дискретная математика с элементами математической логики")""")
    cursor.execute("""INSERT INTO subject VALUES (10, "Теория вероятностей")""")
    con.commit()

    # Заполнение формы сдачи предметов
    cursor.execute("""INSERT INTO sub_form VALUES (1, "Я в душе не знаю что тут должно быть")""")
    con.commit()

    # Заполнение формы сдачи предметов
    cursor.execute("""INSERT INTO curriculum VALUES (1, 1, 1, 1, 1, 1, 1, 1)""")
    con.commit()

    # Заполнение абитуриентов
    cursor.execute("""INSERT INTO applicants VALUES (1, "Кобелев", "Евгений", "Николаевич", "М", "2005-04-21", "г. Ростов-на-Дону", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
    cursor.execute("""INSERT INTO applicants VALUES (2, "Касьянов", "Максим", "Юрьевич", "М", "2005-06-15", "г. Батайск", "Номер телефона", "Email", "2021-09-01", "Разработчик мобильных/десктопных приложений")""")
    cursor.execute("""INSERT INTO applicants VALUES (3, "Кмета", "Антон", "Геннадиевич", "М", "2005-07-22", "г. Красный Сулин", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
    cursor.execute("""INSERT INTO applicants VALUES (4, "Медведев", "Иван", "Юрьевич", "М", "2005-04-08", "г. Азов", "Номер телефона", "Email", "2021-09-01", "Неопределившийся")""")
    cursor.execute("""INSERT INTO applicants VALUES (5, "Зубков", "Роман", "????????", "М", "2005-04-09", "г. Батайск", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
    cursor.execute("""INSERT INTO applicants VALUES (6, "Пермяков", "Руслан", "????????", "М", "2005-03-23", "г. Гуково", "Номер телефона", "Email", "2021-09-01", "Разработчик Web-Мультимедийных приложений")""")
    con.commit()