import json
import sys


def read_json_filenames_from_args():
    try:
        path_to_json = sys.argv[1]
        return path_to_json
    except IndexError:
        return None


def load_json_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except json.decoder.JSONDecodeError:
        return None
    except FileNotFoundError:
        return None


def pretty_print_json(json_content):
    print(json.dumps(json_content, indent=4,
                     sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    file_path = read_json_filenames_from_args()
    if file_path:
        json_content = load_json_from_file(file_path)
        if json_content:
            pretty_print_json(json_content)
        else:
            print("Файл {} некоретный или не существует".format(file_path))
    else:
        print("Не введено имя файла")
    print("Программа завершена.")
