import MeCab
import argparse

def segment(line, mecab):
    return mecab.parse(line.strip().replace(" ", "")).strip().split()

mecab = MeCab.Tagger("-Owakati")
parser = argparse.ArgumentParser(description='')
parser.add_argument('--corpus', type=str, required=True, default="", help="")
parser.add_argument('--out', type=str, required=True, default="", help="")
args = parser.parse_args()

out_f = open(args.out, "w")

for line in open(args.corpus):
    out_f.write(" ".join(segment(line, mecab)) + "\n")
