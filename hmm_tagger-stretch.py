#!/usr/bin/env python
"""Simple HMM tagger with Viterbi decoding.

This acts as a template for the "stretch" version of the assignment. Viterbi
computation is not implemented, nor is backtracing.

Sample invocation:

    ./hmm_tagger-stretch.py \
        --emissions=emissions.tsv \
        --transitions=transitions.tsv \
        ptb.tok
"""


import argparse
import collections
import csv
import operator


START = "<s>"
INF = float("inf")


def hmm_tag(tokens, emissions, transitions):
    # FIXME: Compute and return the Viterbi tag sequence.
    # forward
    track_P = []
    track_T = []
    for i in range(len(tokens)):
        cur_P = {}
        cur_T = {}
        cur_tags = emissions[tokens[i]].keys()
        for t in cur_tags:
            cur_P[t] = emissions[tokens[i]][t]
            if not track_P:
                try:
                    cur_P[t] += transitions[t][START]
                except KeyError:
                    cur_P[t] += INF
            else:
                temp={}
                for t0 in track_P[-1].keys():
                    try:
                        T = transitions[t][t0]
                    except KeyError:
                        T = INF
                    P = track_P[-1][t0]
                    temp[cur_P[t] + T + P] = t0
                cur_P[t] = min(temp.keys())
                cur_T[t] = temp[cur_P[t]]
        track_P.append(cur_P)
        track_T.append(cur_T)
    
    # backward
    track_T = track_T[::-1]
    last_p = track_P[-1]
    last_t = min(last_p, key=last_p.get)
    tags = []
    tags.append(last_t)
    for i in range(len(track_T)-1):
        cur = track_T[i][tags[-1]]
        tags.append(cur)
    return tags[::-1]


def main(args):
    # Reads emission and transition matrices.
    emissions = collections.defaultdict(dict)
    with open(args.emissions, "r") as source:
        for (tag, token, prob) in csv.reader(source, delimiter="\t"):
            # Token -> tag instead of tag to token.
            emissions[token][tag] = float(prob)
    transitions = collections.defaultdict(dict)
    with open(args.transitions, "r") as source:
        for (prev_tag, tag, prob) in csv.reader(source, delimiter="\t"):
            transitions[tag][prev_tag] = float(prob)
    # Tags data.
    with open(args.tokens, "r") as source:
        for line in source:
            tokens = line.rstrip().split()
            tags = hmm_tag(tokens, emissions, transitions)
            gen = zip(tokens, tags)
            print(" ".join(f"{token}/{tag}" for (token, tag) in gen))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HMM tagger")
    parser.add_argument("--emissions", required=True, help="Emission table")
    parser.add_argument(
        "--transitions", required=True, help="Transition table"
    )
    parser.add_argument("tokens", help="Token file")
    main(parser.parse_args())
