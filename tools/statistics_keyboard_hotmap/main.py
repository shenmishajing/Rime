class cfg:
    start_line = 81


def main():
    dict_trans = {}
    dict_statistics = {}

    for i in range(26):
        dict_statistics[chr(ord('a') + i)] = 0

    dict_file = open('wubixinshiji.dict.yaml', 'r')
    for i in range(cfg.start_line - 1):
        dict_file.readline()

    for line in dict_file.readlines():
        word, code = line.split()[:2]
        if len(word) == 1 and '\u4e00' <= word <= '\u9fa5':
            dict_trans[word] = code

    src_file = open('src.txt', 'r')
    for line in src_file.readlines():
        for char in line:
            if '\u4e00' <= char <= '\u9fa5' and char in dict_trans:
                code = dict_trans[char]
                for letter in code:
                    dict_statistics[letter] += 1
    sum = 0
    for count in dict_statistics.values():
        sum += count

    for letter in dict_statistics:
        dict_statistics[letter] /= sum

    res_file = open('res.txt', 'w')
    for letter in sorted(dict_statistics.keys()):
        res_file.write(letter * int(10000 * dict_statistics[letter]))

    area = ['g',
            'f',
            'd',
            's',
            'a',
            'h',
            'j',
            'k',
            'l',
            'm',
            't',
            'r',
            'e',
            'w',
            'q',
            'y',
            'u',
            'i',
            'o',
            'p',
            'n',
            'b',
            'v',
            'c',
            'x']

    left_frequency = 0
    for i in range(5):
        frequency = 0
        for j in range(5):
            frequency += dict_statistics[area[i * 5 + j]]
        if i == 0 or i == 2:
            left_frequency += frequency
        print('area: ' + str(i + 1) + ' ' + str(frequency))

    print(left_frequency)


if __name__ == "__main__":
    main()
