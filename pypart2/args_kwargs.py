def best_func(*args):
    print(args)
    return sum(args)

print(best_func(1,2,3,4,5))


def best_func(*args):
    print(*args)
    # return sum(args)

print(best_func('1','2','3','4','5'))