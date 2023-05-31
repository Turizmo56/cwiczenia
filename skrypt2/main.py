def potegi(podstawa, wykladnik):
    if wykladnik == 1:
        return podstawa
    if wykladnik == 0:
        return 1
    polowa = potegi(podstawa, wykladnik // 2)
    if wykladnik % 2 == 0:
        return polowa * polowa
    else:
        return polowa * polowa * podstawa


if __name__ == "__potegi__":
    potegi(podstawa, wykladnik)


def palindron(napis):
    n = len(napis)
    for i in range(len(napis) // 2):
        if napis[i] != napis[n - 1 - 1]:
            return False
        return True
    if __name == "__palindron__":
        palindron(napis)


def anagram(napis1, napis2):
    n = len(napis1)
    if n != len(napis2):
        return False
    slownik1 = dict()
    slownik2 = dict()
    for i in range (n):
        if napis1[i] in slownik1:
            slownik1[napis1[i]] += 1
        else:
            slownik1[napis1[i]] = 1
        if napis2[i] in slownik2:
            slownik2[napis2[i]] += 1
        else:
            slownik2[napis2[i]] = 1
            return slownik1 == slownik2