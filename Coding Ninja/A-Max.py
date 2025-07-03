def max_per_diff(n):
    digits = list(str(n))
    min_pr = int(''.join(sorted(digits)))
    max_pr = int(''.join(sorted(digits,reverse=True)))
    max_diff = max_pr - min_pr
    return max_diff
if __name__ =='__main__':
    n = int(input())
    print(max_per_diff(n))



