#returns the binary format of a number
def countBits(n):
    binary = "{0:b}".format(n)
    n = [i for i,f in enumerate(binary) if f == "1"]
    return len(n)

    #n = "{0:b}".format(n).count("1")

#returns the str members in a list
def filter_list(l):
    r = list()
    #return [x for x in l if isinstance(x,int)]
    pos = [j for j,h in enumerate(l) if type(h) == int]
    for i in pos:
       r.append(l[i])
    return r

#hides all characters except for the last 4
def maskify(cc):
    aa = list(cc)
    for i in range(len(aa) - 4):
        aa[i] = "#"
    return "".join(aa)
#return "#"*(len(cc)-4) + cc[-4:]
