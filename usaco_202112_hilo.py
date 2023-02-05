"""
5
5 2 1 4 3

B
E guess

0,1,2, ... N   N+1

5 2 1 4 3

4.5
5 -- HI
2 -- LO
4 -- LO

"HILOLO"  1

0.5 1.5 2.5 3.5 4.5 5.5

"""


def get_hilo_times(permutation, x):
    cnt = 0
    x += 0.5
    last_hi = False
    lo, hi = 0, len(permutation)+1
    for guess in permutation:
        if guess < lo or guess > hi:
            continue

        if guess < x:
            lo = guess
            if last_hi:
                cnt += 1
                last_hi = False
        else:
            hi = guess
            last_hi = True
    return cnt


def print_hilo_times(permutation):
    n = len(permutation)
    # Calculate HILO times for each x from 1 to N
    for x in range(n+1):
        print(get_hilo_times(permutation, x))


# def calc_times(permutation):
#     n = len(permutation)
#     ans = []
#     # Calculate HILO times for each x from 1 to N
#     for x in range(n+1):
#         ans.append(get_hilo_times(permutation, x))
#     return ans


# test = [5, 1, 2, 4, 3]
# for x in range(len(test)+1):
#     print(get_hilo_times(test, x))


lines = []
while True:
    l = input()
    if l == "":
        break
    lines.append(l)

for perm in lines[1::2]:
    perm = list(map(int, perm.split()))
    print_hilo_times(perm)
