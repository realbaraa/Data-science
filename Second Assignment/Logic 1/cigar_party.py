def cigar_party(cigars, is_weekend):
  r=range(40,61)
  return cigars in r or (is_weekend and cigars >=40)