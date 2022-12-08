# Algoritmen går ut på att addera och subtrahera vartannat tal i den långa talföljden, och man börjar med addition. T.ex. så skulle talföljden 12543 med algoritmen bli 1+2-5+4-3, vilket skulle ge lösenordet -1.

talföljd = 126654831548266514852461379524813824618465141519467252346164242416184973581416155963142

input = str(talföljd)
ans = int(input[0])

for i in range(1, len(input)-1, 2):
  ans += int(input[i])
  ans -= int(input[i+1])

print(ans)
