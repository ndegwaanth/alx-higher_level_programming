#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        string_len = len(sentence)
        return (string_len, sentence[0])
