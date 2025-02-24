from .base import Tokenizer, pair_count,merge_and_mint

class BasicTokenizer(Tokenizer):
    def __init__(self):
        super().__init__()

    def train(self,text,vocab_size,verbose=False):
        assert vocab_size >=256
        num_merges= vocab_size - 256 

        text_bytes = text.encode("utf-8")
        ids= list(text_bytes)

        merges={}
        vocab={idx:bytes([idx]) for idx in range(256)}
        for i in range(num_merges):
            pairs=pair_count(ids)
            pair=max(pairs,key=pairs.get)
            idx=256+i
            ids=merge_and_mint(ids,pair,idx)
            merges[pair]=idx
            vocab[idx]=vocab[pair[0]] + vocab[pair[1]]
            if verbose:
                print(f"merge {i+1}/{num_merges}: {pair} -> {idx} ({vocab[idx]}) had {pairs[pair]} occurrences")

        self.merges=merges
        self.vocab=vocab

    
    def decode(self,ids):
        text_bytes= b"".join(self.vocab[idx] for idx in ids)
        text=text_bytes.decode('utf-8',errors='replace')
        return text
    
    def encode(self,text):
        text_bytes=text.encode("utf-8")
        ids= list(text_bytes)
        while len(ids)>=2:
            pairs=pair_count(ids)
            pair=min(pairs, key=lambda p:self.merges.get(p,float("inf")))
            if pair not in self.merges:
                break
            idx=self.merges[pair]
            ids=merge_and_mint(ids,pair,idx)

        return ids