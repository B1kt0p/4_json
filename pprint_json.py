import json
import os
import sys


def read_json_filenames_from_args():
    file_path = []
    try:
        for path in sys.argv[1:]:
            if os.path.exists(path):
                file_path.append(path)
            else:
                print("Файл {} не найден".format(path))
        if file_path:
            return file_path
        else:
            print("Не найден не один файл")
            return None
    except IndentationError:
        pass


def load_json_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            json_data = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            json_data = None
    return json_data


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    path_files = read_json_filenames_from_args()
    if path_files:
        for path in path_files:
            json_data = load_json_from_file(path)
        if json_data:
            pretty_print_json(json_data)
        else:
            print("Файл {} некоретный".format(path))
    print("Программа завершена.")
