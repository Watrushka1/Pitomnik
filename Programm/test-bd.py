import mysql.connector

# Подключение к базе данных
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="phpmyadmin",
        password="q123",
        database="phpmyadmin"
    )

    if connection.is_connected():
        print("Успешное подключение к базе данных MySQL")

except mysql.connector.Error as error:
    print("Ошибка при подключении к базе данных MySQL:", error)

finally:
    if 'connection' in locals():
        connection.close()
        print("Соединение с базой данных закрыто")