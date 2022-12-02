from utils import NerDataset
import re
from collections import Counter
import numpy as np
import pandas as pd

raw_text = open('data/神农本草经_无换行.txt', 'r', encoding='utf_8').read()

medicine = list(open('data/medicine_all.txt', 'r', encoding='utf_8').read().split('\n'))
use = list(open('data/use_all.txt', 'r', encoding='utf_8').read().split('\n'))

annotations = {'medicine': medicine, 'use':use}

raw_text = raw_text.replace('\n', '')
raw_text = raw_text.replace('\t', '')
labels = len(raw_text) * ['O']

for ann, entities in annotations.items():
    for entity in entities:
        # 先生成实体对应的 BME 标注类型
        B, M, E = [['{}-{}'.format(i, ann)] for i in ['B', 'I', 'I']]
        # 计算实体词中的数量
        M_len = len(entity) - 2
        # 生成 label，如果词中数为0，则直接为 BE，不然按数量添加 M
        label = B + M * M_len + E if M_len else B + E
        # 从原始文本中找到实体对应出现的所有位置
        idxs = [r.start() for r in re.finditer(entity, raw_text)]

        for idx in idxs:
            labels[idx:idx + len(entity)] = label


f = open('data/神农百草经_labeled.txt', 'w', encoding='utf_8')
for ann, label in zip(raw_text, labels):
    d = str(ann)+' '+str(label)+'\n'
    f.write(d)
