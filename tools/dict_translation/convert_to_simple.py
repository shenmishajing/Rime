import os
import shutil
import opencc

c = opencc.OpenCC('t2s')


def main():
    root_path = 'tools/dicts'
    source_path = os.path.join(root_path, 'original')
    target_path = os.path.join(root_path, 'simplified')

    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.makedirs(target_path)

    for file in os.listdir(source_path):
        if file.endswith('.dict.yaml'):
            open(os.path.join(target_path, file), 'w').write(
                c.convert(open(os.path.join(source_path, file)).read()))


if __name__ == "__main__":
    main()
