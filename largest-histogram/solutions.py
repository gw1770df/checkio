def largest_histogram(histogram):
    max_num = max(histogram)
    ll = [0 for i in range(max_num)]
    histogram += [0]
    for current_num in range(1, max_num + 1):
        num = 0
        for v in histogram:
            if v >= current_num:
                num += current_num
            elif num > ll[current_num - 1]:
                ll[current_num - 1] = num
                num = 0
    return max(ll)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
