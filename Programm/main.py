import mysql.connector

# Подключение к базе данных
mydb = mysql.connector.connect(
    host="localhost",
    user="phpmyadmin",
    password="q123",
    database="phpmyadmin"
)

mycursor = mydb.cursor()

# Функция для добавления нового животного
def add_animal():
    animal_type = input("Введите тип животного (домашнее/вьючное): ")
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения (гггг-мм-дд): ")
    skill = input("Введите команду, которую умеет выполнять животное: ")

    sql = "INSERT INTO animals (animal_type, name, birth_date, skill) VALUES (%s, %s, %s, %s)"
    val = (animal_type, name, birth_date, skill)
    mycursor.execute(sql, val)

    mydb.commit()

    print("Животное успешно добавлено!")

# Функция для добавления команды животному
def add_command():
    name = input("Введите имя животного: ")
    new_skill = input("Введите новую команду для животного: ")

    sql = "UPDATE animals SET skill = %s WHERE name = %s"
    val = (new_skill, name)
    mycursor.execute(sql, val)

    mydb.commit()

    print("Команда добавлена!")

# Функция для вывода списка всех животных
def list_animals():
    mycursor.execute("SELECT * FROM animals")
    animals = mycursor.fetchall()

    for animal in animals:
        print(animal)


# Функция для изменения типа животного
def change_animal_type():
    name = input("Введите имя животного, которое нужно перенести: ")
    new_animal_type = input("Введите новый тип животного (домашнее/вьючное): ")

    sql = "UPDATE animals SET animal_type = %s WHERE name = %s"
    val = (new_animal_type, name)
    mycursor.execute(sql, val)

    mydb.commit()

    print("Тип животного успешно изменен!")

# Основной код
while True:
    print("Меню:")
    print("1. Добавить новое животное")
    print("2. Добавить команду животному")
    print("3. Изменить тип животного")
    print("4. Вывести список всех животных")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_animal()
    elif choice == "2":
        add_command()
    elif choice == "3":
        change_animal_type()
    elif choice == "4":
        list_animals()
    elif choice == "5":
        break
    else:
        print("Неверный выбор, попробуйте снова.")