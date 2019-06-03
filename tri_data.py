from tqdm import tqdm


def select_data(file1, file2, same_file, diff_file1, diff_file2):
    file1_data = []
    file2_data = []
    same_data = []
    file1_data_dict = {}
    unit = []
    score = []
    sentence = ''
    sentence1 = ''
    file1_reader = open(file1, encoding='utf-8')
    file2_reader = open(file2, encoding='utf-8')
    same_writer = open(same_file, encoding='utf-8', mode='w')
    diff_writer1 = open(diff_file1, encoding='utf-8', mode='w')
    diff_writer2 = open(diff_file2, encoding='utf-8', mode='w')
    pbar = tqdm(file1_reader.readlines())
    pbar1 = tqdm(file2_reader.readlines())
    for word in pbar:
        if word != '\n':
            word = word.split('\t')
            score.append(word[9])
            word[9] = '_'
            word = '\t'.join(word)
            word = word + '+-*/'
            sentence += word
        else:
            unit.append(sentence)
            unit.append(score)
            file1_data.append(unit)
            file1_data_dict[sentence] = unit
            unit = []
            score = []
            sentence = ''
    for word in pbar1:
        if word != '\n':
            word = word.split('\t')
            word[9] = '_'
            word = '\t'.join(word)
            word = word + '+-*/'
            sentence1 += word
        else:
            file2_data.append(sentence1)
            sentence1 = ''
    len_file1 = len(file1_data)
    len_file2 = len(file2_data)
    same_data_str = list(set(file1_data[i][0] for i in range(len(file1_data))).intersection(set(file2_data)))
    for line in same_data_str:
        same_data.append(file1_data_dict.get(line))

    len_same = len(same_data)
    diff1_data = set(file1_data[i][0] for i in range(len(file1_data))).difference(same_data_str)
    len_diff1 = len(diff1_data)
    diff2_data = set(file2_data).difference(same_data_str)
    len_diff2 = len(diff2_data)

    writer_same_data(same_writer, same_data)
    writer_diff_data(diff_writer1, diff1_data)
    writer_diff_data(diff_writer2, diff2_data)

    print('文件1总数', len_file1, '\t', '相同句子数：', len_same, '\t', '不同句子数：', len_diff1)
    print('文件2总数', len_file2, '\t', '相同句子数：', len_same, '\t', '不同句子数：', len_diff2)
    print('相同的数据占比：', 100 * float(len_same / len_file1), '%')
    print('相同的数据占比：', 100 * float(len_same / len_file2), '%')


def writer_same_data(writer, data):
    for unit in data:
        line = unit[0].split('+-*/')
        score = unit[1]
        for word, value in zip(line, score):
            if word == '':
                pass
            else:
                word = word.split('\t')
                word[9] = value
                word = '\t'.join(word)
                writer.write(word)
        writer.write('\n')
    writer.close()


def writer_diff_data(writer, data):
    for line in data:
        line = line.split('+-*/')
        for word in line:
            if word == '':
                pass
            else:
                word = word.split('\t')
                if len(word) != 10:
                    print(word)
                word[6] = '_'
                word[7] = '_'
                word = '\t'.join(word)
                writer.write(word + '\n')
        writer.write('\n')
    writer.close()


if __name__ == "__main__":
    file1 = 'PB-Unlabeled.conll15.out'
    file2 = 'PB-Unlabeled.conll25.out'
    file3 = 'PB-Unlabeled.conll35.out'

    same_file12 = 'PB-Unlabeled.same12.out6'
    same_file13 = 'PB-Unlabeled.same13.out6'
    same_file23 = 'PB-Unlabeled.same23.out6'

    diff_file1 = 'PB-Unlabeled.diff1.out6'
    diff_file2 = 'PB-Unlabeled.diff2.out6'
    diff_file3 = 'PB-Unlabeled.diff3.out6'

    select_data(file1, file2, same_file12, diff_file1, diff_file2)
    select_data(file1, file3, same_file13, diff_file1, diff_file3)
    select_data(file2, file3, same_file23, diff_file2, diff_file3)

