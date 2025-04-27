def count_words(txt):
    arr = txt.split()
    return len(arr)

def count_char(txt):
    txt = txt.lower()


    counts = {}
    for ch in txt:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_on(d):
    return d["num"]

def report(count_dict):
    count_list = []
    for k in count_dict:
        if k.isalpha():
            count_list.append({"char": k, "num": count_dict[k]})



    count_list.sort(reverse=True, key=sort_on)
    for i in range(len(count_list)):
        d = count_list[i]
        print(f"{d['char']}: {d['num']}")

    