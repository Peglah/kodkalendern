# Beräkna summan av de 123 första tal som är delbara med 7 och hjälp nissarna att få fram koden till väckarklockan för att kunna aktivera alarmet och väcka tomten!

kod = []
i = 1

while len(kod) < 123:
  if i % 7 == 0:
    kod.append(i)
  i += 1

print(sum(kod))
