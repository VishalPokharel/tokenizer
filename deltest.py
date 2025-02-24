from byte_pair_encoding import BasicTokenizer
tokenizer=BasicTokenizer()

# A sample text to test encoding and decoding
sample_text = "h"

# Encode the sample text to a list of token IDs
encoded_tokens = tokenizer.encode(sample_text)
print("Encoded tokens:", encoded_tokens)

# Decode the list of token IDs back into text
decoded_text = tokenizer.decode(encoded_tokens)
print("Decoded text:", decoded_text)
