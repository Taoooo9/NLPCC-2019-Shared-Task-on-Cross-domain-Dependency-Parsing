import random

random.seed(666)
file = 'PC-Unlabeled.conll_avg3.out'
file1 = 'PC-Unlabeled.conll_avg_good4.out'
file2 = 'PC-Unlabeled.conll_avg_bad4.out'
writer = open(file1, encoding='utf-8', mode='w')
writer1 = open(file2, encoding='utf-8', mode='w')
data = []
sentence = ''
with open(file, encoding='utf-8') as f:
    for word in f.readlines():
        if word != '\n':
            word = word.split('\t')
            word = '\t'.join(word)
            word = word + '+-*/'
            sentence += word
        else:
            data.append(sentence)
            sentence = ''
data_len = len(data)
# print(data_len)
# small_data = random.sample(data, int(data_len / 2))
# middle_data = list(set(data).difference(set(small_data)))
# print(len(small_data))
# print(len(middle_data))

for line in data:
    line = line.split('+-*/')
    for word in line:
        if word == '':
            pass
        else:
            writer.write(word)
    writer.write('\n')
writer.close()

# for line in middle_data:
#     line = line.split('+-*/')
#     for word in line:
#         if word == '':
#             pass
#         else:
#             word = word.split('\t')
#             if len(word) != 10:
#                 print(word)
#             word[6] = '_'
#             word[7] = '_'
#             word[9] = '_'
#             word = '\t'.join(word)
#             writer1.write(word + '\n')
#     writer1.write('\n')
# writer1.close()


