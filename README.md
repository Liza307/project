# gazprom_project
Над проектом работала команда 3:
Project manager Александр Сиротин
Product manager Данис Маматулин
Designer Маргарита Бикмуллина
Designer Маргарита Борович
Designer Дарья Корешкова
Designer Ирина Рыженкова
Designer Анастасия Власова
BA Евгений Исаев
BA Анастасия Земцова
SA Алёна Пичкалова
SA Вадим Гнездилов
QA Галина Васюта
Frontend Денис Недосейкин
Backend Лозинская Елизавета
Бэкенд проекта доступен по доменному имени http://gzpr3.zapto.org/

Ссылка на swagger - https://app.swaggerhub.com/apis/pichkalovaalena/My_project1/1.0#/info

Для запуска проекта необходимо выполнить следующие действия:
1. git clone git@github.com:Liza307/project.git
2. python -m venv venv (Создать виртуальное окружение)
4. source venv/Scripts/activate (Активировать виртуальное окружение)
5. Из директории где файл requirements написать pip install -r requirements.txt
6. Из директории где файл manage.py выполнить команду python manage.py migrate
7. Из директории с файлом manage.py выполнить python manage.py runserver

project - приложение, написанное на Django Rest Framework. Список используемых библиотек можно найти в файле requirements.txt
Ввод тестовых данных
`python manage.py insert_test_data`