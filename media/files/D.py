# dif = откр - закр
def gen(n: int, res: str, dif: int):
    if len(res) == 2*n and dif == 0:
        print(res)
    if len(res) < 2*n - dif - 1:
        # res += '('
        # dif += 1
        gen(n, res + '(', dif + 1)
    if dif > 0:
        # res += ')'
        # dif -= 1
        gen(n, res + ')', dif - 1)



n = int(input())
gen(n, '', 0)
