import os
import time
from byte_pair_encoding import BasicTokenizer

text = open("tests/taylorswift.txt", "r", encoding="utf-8").read()

os.makedirs("models", exist_ok=True)

t0 = time.time()

tokenizer= BasicTokenizer()
tokenizer.train(text,512,verbose=True)

prefix = os.path.join("models", "basic")

t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")