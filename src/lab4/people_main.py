from people2 import SurveyProcessor, Respondent
import  sys

def main():
    try:
        boundaries = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Все границы возрастных групп должны быть целыми числами.")
        sys.exit(1)

    try:
        processor = SurveyProcessor(boundaries)
    except ValueError as ve:
        print(f"Ошибка: {ve}")
        sys.exit(1)

    print("Введите список респондентов в формате <ФИО>,<возраст>. Для завершения введите 'END':")
    respondents = []
    while True:
        try:
            line = sys.stdin.readline()
            line = line.strip()
            if line.upper() == "END":
                break
            parts = line.split(',', 1)
            if len(parts) != 2:
                print(f"Некорректная строка: '{line}'. Ожидается формат <ФИО>,<возраст>.")
                continue
            full_name = parts[0].strip()
            age_str = parts[1].strip()
            age = int(age_str)
            if not (0 <= age <= 123):
                print(f"Некорректный возраст для респондента '{full_name}': {age}. Должен быть от 0 до 123.")
                continue
            respondent = Respondent(full_name, age)
            respondents.append(respondent)
        except ValueError:
            print(f"Некорректный возраст в строке: '{line}'. Должен быть целым числом.")
            continue
        except Exception as e:
            print(f"Ошибка при обработке строки '{line}': {e}")
            continue

    processor.process_respondents(respondents)

    processor.display_groups()

if __name__ == "__main__":
    main()

# python /Users/carlia/PycharmProjects/prog/src/lab4/people_main.py  18 25 35 45 60 80 100