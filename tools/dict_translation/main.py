class cfg:
    start_line = 34
    # start_line = 0

    original_area = ['g', 'f', 'd', 's', 'a', 'h', 'j', 'k', 'l', 'm', 't', 'r', 'e', 'w', 'q', 'y', 'u', 'i', 'o', 'p',
                     'n', 'b', 'v', 'c', 'x', 'z']

    new_area = ['i', 'u', 'e', 'o', 'a', 'd', 'h', 't', 'n', 's', 'x', 'k', 'j', 'q', 'p', 'f', 'g', 'c', 'r', 'l', 'b',
                'm', 'w', 'v', 'z', 'y']

    map_dict = {}
    for i in range(len(original_area)):
        map_dict[original_area[i]] = new_area[i]


def main():
    print(cfg.map_dict)
    dict_file = open('dvorak_wubi.old.dict.yaml', 'r')
    res_file = open('dvorak_wubi.dict.yaml', 'w')
    # dict_file = open('dvorak_wubi.old.sogou.dict.yaml', 'r')
    # res_file = open('dvorak_wubi.sogou.dict.yaml', 'w')
    for i in range(cfg.start_line - 1):
        res_file.write(dict_file.readline())

    for line in dict_file.readlines():
        for char in line:
            if 'a' <= char <= 'z':
                res_file.write(cfg.map_dict[char])
            else:
                res_file.write(char)


if __name__ == "__main__":
    main()
