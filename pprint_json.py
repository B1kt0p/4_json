import json
import os, sys

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
            exit(0)
    except IndentationError:
        pass


def load_json_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data=json.loads(f.read())
        except:
            data=None
    return data

def pretty_print_json(json_loads):
    print(json.dumps(json_loads, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':
    path_files = read_json_filenames_from_args()
    for path in path_files:
        data=load_json_from_file(path)
    if data:
        pretty_print_json(data)
    else:
        print("Файл {} некоретный".format(path))

    print("Программа завершена.")

