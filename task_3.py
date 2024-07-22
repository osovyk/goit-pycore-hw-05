import sys
from collections import Counter
from pathlib import Path


def load_logs(file_path: str) -> list:
    file = Path(file_path)
    result = []

    with open(file) as logs:
        for line in logs:
            result.append(parse_log_line(line))

    return result


def parse_log_line(line: str) -> dict:
    result = {
        "data": line.split()[0],
        "time": line.split()[1],
        "level": line.split()[2],
        "message": " ".join(line.split()[3:])
    }

    return result


def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = filter(lambda item: item["level"] == level, logs)
    result = []

    for log in filtered_list:
        parsed_log = " ".join([value for key, value in log.items()]).replace(level, "-")
        result.append(parsed_log)

    return result


def count_logs_by_level(logs: list) -> dict:
    level_counter = Counter(log['level'] for log in logs)
    result = {level: count for level, count in level_counter.items()}

    return result


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f"{key:<17}| {value}")


def main():
    if 2 != len(sys.argv) != 3:
        print("Помилка: використання 'python task_3.py <шлях до файлу з логами> <рівень логування (опціонально)>'")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.is_file():
        print(f"Помилка: {file_path} не є файлом або не існує.")
        sys.exit(1)

    try:
        loaded_logs = load_logs(sys.argv[1])
        counted_logs_by_level = count_logs_by_level(loaded_logs)
        display_log_counts(counted_logs_by_level)

        if len(sys.argv) == 3:
            log_level = sys.argv[2].upper()
            filtered_logs_by_level = filter_logs_by_level(loaded_logs, log_level)
            print(f"\nДеталі логів для рівня '{log_level}':")
            for log in filtered_logs_by_level:
                print("".join(log))
    except IndexError:
        print("Помилка: Ви намагаєтесь відкрити файл, який не містить логів")
        sys.exit(1)


if __name__ == "__main__":
    main()
