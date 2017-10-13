def streak_check(n, ExactK):
    k = 1
    while (n + k) % (k + 1) == 0:
        k += 1
        if k > ExactK:
            return 0
    return k

# print(streak_check(13, 4))
# print(streak_check(14, 1))
# print(streak_check(13, 1))
# print(streak_check(13, 5))

Answer = 2

Max = 31
print(4**31)
for i in range(1, 30):
    print(streak_check(360361 + (15 * 2)*i, 15))
for i in range(3, (4 ** Max) + 1, 2):
    # N = 4 ** i
    # for n in range(1, N+1):
    Current = streak_check(i, Max)
    # print(i, Current)
    if Current > 0:
        Limit = 4 ** Current
        # print(i, Current, Limit, i <= Limit)
        if i <= Limit:
            Answer += 1
    if Current == 15:
        print(i, Current, Limit, i <= Limit)
        break

print(Answer)