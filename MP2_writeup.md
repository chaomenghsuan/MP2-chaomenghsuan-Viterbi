## Viterbi Decoding:

I completed the `hmm_tagger-stretch.py` by creating the function `hmm_tag` from the scratch.

## Challenges

`KeyError`: this happened when I tried to index the emissions dictionary or the transitions dictionary. I realized that the dictionaries does not include some certain combinations, and that means the probabilities of such combinations are nearly 0 (with negative log value, infinite). I used `try`-`except KeyError` to prevent the program from breaking down. 