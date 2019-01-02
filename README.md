MP2: Viterbi decoding
=====================

In this MP, you will help create a Viterbi part of speech tagger.

You have a choice to make: you can either attempt the "basic"
assignment, or you can attempt the "stretch" assignment. It is up to
you.

Data
----

The file `emissions.tsv` is a tab-separated values file where the first
column is a [Penn Treebank POS
tag](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html),
the second column is a token, and the third is the conditional probability
of the token given the tag, expressed as a negative log probability.

The file `transitions.tsv` is a tab-separated values file where the
first and second column are a tag bigram and the third is the conditional
probability of that bigram, expressed as a negative log probability.
Note that this file contains transitions from the start tag (represented
by `<S>` but not transitions to any final tag).

These have been computed using sections 00-18 of the [Penn
Treebank](https://catalog.ldc.upenn.edu/ldc99t42).

The file `ptb.tok` contains the tokens of sections 00-18 of the Penn
Treebank.

These files are all distributed as gzipped data: decompress them before
using.

Basic tier
----------

`hmm_tagger-basic.py` contains a carefully-documented template for a HMM
tagger that takes `emissions.tsv` , `transitions.tsv`, and `ptb.tok` as
arguments. It currently computes the Viterbi probabilities, but it
neither stores nor follows backtraces. Your assignment is to modify the
`hmm_tag` function so that it:

-   stores backtraces,
-   follows the backtraces to produce the most likely tag sequence, and
-   returns that tag sequence in the original order.

You do not need to make use of `hmm_tagger-stretch.py`.

Stretch tier
------------

`hmm_tagger-basic.py` contains a carefully-documented template for a HMM
tagger that takes `emissions.tsv` , `transitions.tsv`, and `ptb.tok` as
arguments. Your assignment is to implement the `hmm_tag` function so
that it:

-   computes the Viterbi probabilities,
-   stores backtraces,
-   follows the backtraces to produce the most likely tag sequence, and
-   returns that tag sequence in the original order.

Do not make use of `hmm_tagger-basic.py`.

What to turn in
---------------

Regardless of which tier you attempt, you should turn in:

-   your completed `hmm_tagger.py`, and
*   a write-up describing your approach and challenges you encountered.

Hints
-----

-    The simplest way to store backtraces is as a list of dictionaries.
-    Note the outer and inner keys for `emissions` and `transitions`.


Test support
------------

My implementation returns the following tagging for the first sentence:

    Pierre/NNP Vinken/NNP ,/, 61/CD years/NNS old/JJ ,/, will/MD join/VB the/DT board/NN as/IN a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD ./.
