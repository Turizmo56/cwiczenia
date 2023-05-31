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


def palindron(napis):
    return napis == napis[::-1]


def anagram(napis1,napis2):
        n = len(napis1)
        if n != len(napis2):
            return False
        slownik1 = dict()
        slownik2 = dict()
        for i in range(n):
            if napis1[i] in slownik1:
                slownik1[napis1[i]] += 1
            else:
                slownik1[napis1[i]] = 1
            if napis2[i] in slownik2:
                slownik2[napis2[i]] += 1
            else:
                slownik2[napis2[i]] = 1
        return slownik1 == slownik2


def main():
    print("2^5 = " + str(potegi(2, 5)))
    print("CzyPalindrom(kajak) = " + str(palindron("kajak")))
    print("CzyPalindrom(kobyla) = " + str(palindron("kobyla")))
    print("Czy anagram(kwiat, tkwia) = " + str(anagram("kwiat","tkwia")))
    print("czy anagram(kobyla,boczek) = " + str(anagram("kobyla", "boczek")))


if __name__ == "__main__":
    main()
