import os
import shutil

original_area = [
    'g', 'f', 'd', 's', 'a',
    'h', 'j', 'k', 'l', 'm',
    't', 'r', 'e', 'w', 'q',
    'y', 'u', 'i', 'o', 'p',
    'n', 'b', 'v', 'c', 'x', 'z']

new_area = [
    'i', 'u', 'e', 'o', 'a',
    'd', 'h', 't', 'n', 's',
    'x', 'k', 'j', 'q', 'p',
    'f', 'g', 'c', 'r', 'l',
    'b', 'm', 'w', 'v', 'z', 'y']

map_dict = {org_char: new_char for org_char,
            new_char in zip(original_area, new_area)}


def convert_key_map(source_file, target_file, start_line=0):
    source_file = open(source_file)
    target_file = open(target_file, 'w')

    for i in range(start_line - 1):
        target_file.write(source_file.readline())

    for line in source_file.readlines():
        for char in line:
            if char in map_dict:
                target_file.write(map_dict[char])
            else:
                target_file.write(char)


def main():
    root_path = 'tools/dicts'
    source_path = os.path.join(root_path, 'simplified')
    target_path = os.path.join(root_path, 'final')

    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.makedirs(target_path)

    for file in os.listdir(source_path):
        if file.endswith('.dict.yaml'):
            shutil.copy2(os.path.join(source_path, file),
                         os.path.join(target_path, file))

    for file_name, start_line in zip(['', '.sogou'], [34, 0]):
        file_name = f'dvorak_wubi{file_name}.dict.yaml'
        convert_key_map(os.path.join(source_path, file_name),
                        os.path.join(target_path, file_name), start_line)


if __name__ == "__main__":
    main()
