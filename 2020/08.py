# "För att inte obehöriga ska läsa denna lista har listan krypterats. Varje bokstav har skjutits fram 13 snäpp i alfabetet”

# Detta innebär att A har blivit N, B har blivit O, och C har blivit P. Om man kommer till slutet av alfabetet räknar man om från början, t.ex. åäöabcde… osv. Ett Ö har således blivit ett M.

krypterad_önskelista = ["syitöynå", "oncxrdoäyycöezö", "eåqrbfnddråcxnzrbn"]
key =	{
  "a": "q",
  "b": "r",
  "c": "s",
  "d": "t",
  "e": "u",
  "f": "v",
  "g": "w",
  "h": "x",
  "i": "y",
  "j": "z",
  "k": "å",
  "l": "ä",
  "m": "ö",
  "n": "a",
  "o": "b",
  "p": "c",
  "q": "d",
  "r": "e",
  "s": "f",
  "t": "g",
  "u": "h",
  "v": "i",
  "w": "j",
  "x": "k",
  "y": "l",
  "z": "m",
  "å": "n",
  "ä": "o",
  "ö": "p"
}

for word in krypterad_önskelista:
  for c in word:
    print(key[c], end='')
  print()
