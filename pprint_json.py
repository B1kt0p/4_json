import json
import os
import sys


def read_json_filenames_from_args():
    path_files = []
    try:
        for path_to_json in sys.argv[1:]:
            if os.path.exists(path_to_json):
                path_files.append(path_to_json)
            else:
                print("Файл {} не найден".format(path_to_json ))
        if path_files:
            return path_files
        else:
            print("Не найден не один файл")
            return None
    except IndentationError:
        pass


def load_json_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            json_content = json.loads(f.read())
        except json.decoder.JSONDecodeError:
            json_content = None
    return json_content


def pretty_print_json(json_content):
    print(json.dumps(json_content, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    file_paths = read_json_filenames_from_args()
    if file_paths:
        for file_path in file_paths:
            json_content = load_json_from_file(file_path)
            if json_content:
                pretty_print_json(json_content)
            else:
                print("Файл {} некоретный".format(file_path))
    print("Программа завершена.")
