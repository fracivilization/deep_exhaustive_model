with open('data/genia.train.iob2', 'r', encoding='utf-8') as f:
    txt = f.read()
snts = [[line.split('\t')  for line in snt.split('\n')] for snt in txt.split('\n\n')]
from seqeval.metrics.sequence_labeling import get_entities
for snt in snts:
    pass
