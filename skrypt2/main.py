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
