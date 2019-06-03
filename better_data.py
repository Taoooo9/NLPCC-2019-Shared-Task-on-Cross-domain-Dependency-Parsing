# @Author : bamtercelboo
# @Datetime : 2019/5/17 11:15
# @File : better_data.py
# @Last Modify Time : 2019/5/17 11:15
# @Contact : bamtercelboo@{gmail.com, 163.com}

"""
    FILE :  better_data.py
    FUNCTION : None
"""
import sys
import os
import time


class Instance:
    """
        Instance
    """
    def __init__(self):
        self.words_line = []
        self.count = 0
        self.better = True


class Better_data(object):
    """
        Better_data
    """
    def __init__(self, path, count, value):
        self.path = path
        self.out_path = self.path + ".better1"
        self.count = count
        self.value = value
        insts = self.read()
        self.tofile(insts)

    def read(self):
        """
        :return:
        """
        assert self.path is not None, "The Data Path Is Not Allow Empty."
        insts = []
        with open(self.path, encoding="UTF-8") as f:
            inst = Instance()
            for line in f.readlines():
                line = line.strip()
                if line == "" and len(inst.words_line) != 0:
                    inst.words_size = len(inst.words_line)
                    insts.append(inst)
                    inst = Instance()
                else:
                    line = line.strip().split()
                    v = line[-1]
                    if float(v) <= self.value:
                        inst.count += 1
                    if inst.count >= self.count:
                        inst.better = False
                    # print(line)
                    inst.words_line.append(line)

            if len(inst.words_line) != 0:
                inst.words_size = len(inst.words_line)
                insts.append(inst)
            # print("\n")
        return insts

    def tofile(self, insts):
        """
        :return:
        """
        file = open(self.out_path, encoding="utf-8", mode="w")
        for inst in insts:
            if inst.better is False:
                continue
            for word in inst.words_line:
                file.writelines("\t".join(word) + "\n")
            file.write("\n")
        file.close()


if __name__ == "__main__":
    path = "PB-Unlabeled.conll.out"
    count = 2
    value = 0.90
    Better_data(path, count, value)



