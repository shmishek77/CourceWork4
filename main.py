from src.classes import HeadHunter
from src.json_saver import JSONSaver

hh = HeadHunter()
json_saver = JSONSaver("data/vacancies.json")


def user_interaction():

    # начало работы программы, получение ключегого слова для поиска по вакансиям
    vacancies = hh.filter_vacancies(input("Введите ключевое слово для поиска по вакансиям и нажмите Enter: "))
    json_saver.write_vacancies(vacancies)

    # выбор сортировки вакансий
    sort = input(
"""
Выберите сортировку:
1 - вывести вакансии без сортировки
2 - отсортировать по зарплате по убыванию
3 - отсортировать по зарплате по возрастанию
""")

    list_vacancies_from = json_saver.read_vacancies()

    if sort == "1":
        for vacancy in list_vacancies_from:
            print(vacancy)
            print("-" * 50)

    elif sort == "2":
        for vacancy in sorted(list_vacancies_from, reverse=True):
            print(vacancy)
            print("-" * 50)

    elif sort == "3":
        for vacancy in sorted(list_vacancies_from):
            print(vacancy)
            print("-" * 50)

    else:
        print("Такого варианта не существует! Завершение программы.")


if __name__ == "__main__":
    user_interaction()