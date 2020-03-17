""" Sort String """
def main():
    """ Sort String """
    data = input()
    data = data.split(",")
    dict_a = {}
    dict_b = {}
    for word in data:
        dict_a[word] = 0
        if word in dict_b.keys():
            dict_b[word] += 1
        else:
            dict_b[word] = 1
        for chara in word:
            if chara.isupper():
                dict_a[word] += ord(chara) * -1
            else:
                dict_a[word] += ord(chara)
    ans = sorted(dict_a.items(), key=lambda x: x[1])
    for i in ans:
        print((i[0] + "\n") * (dict_b.get(i[0])), end="")
main()