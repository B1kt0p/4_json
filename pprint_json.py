import json
import sys


def load_json_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return None


def pretty_print_json(json_content):
    print(json.dumps(
        json_content,
        indent=4, sort_keys=True,
        ensure_ascii=False
    ))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        json_content = load_json_from_file(file_path)
        if json_content:
            pretty_print_json(json_content)
        else:
            print("Файл {} некоретный или не существует".format(file_path))
    else:
        print("Неправильный формат команды. Обратитесь к README.md")
    print("Программа завершена.")
