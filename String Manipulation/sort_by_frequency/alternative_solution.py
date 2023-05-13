def sort_by_freq(msg):
    msg_sort = sorted(msg)
    msg_sort_frq = sorted(msg_sort, key = lambda c: msg_sort.count(c))
    return "".join(msg_sort_frq)

out = sort_by_freq("aabbccdddddeeee")
print(f"String sorted by char frequency: {out}")