def make_out_word(out, word):
    split = len(out) / 2
    strin=out[0:int(split)]
    strout = out[int(split):]
    return (strin) + word + (strout)