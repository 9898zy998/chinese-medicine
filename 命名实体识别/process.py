import numpy as np
import pandas as pd
import jieba

with open('data/othername.txt', 'r', encoding="utf-8") as f:
  other = f.readlines()

with open('data/medicine_all.txt', 'r', encoding="utf-8") as f:
  data = f.readlines()

for i in other:
  i = i.replace('\n','')
  if i != '' and i not in data:
    data.append(i+'\n')

with open('data/medicine_all_1.txt', 'w', encoding='utf_8') as file:
  for i in data:
    file.write(i)
