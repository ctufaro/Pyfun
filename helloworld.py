def super_reduced_string(s):
    retstr = ''
    ltrDic = {}
    visited = {}
    if s == '':
        return 'Empty String'
    for l in s:
        if l not in ltrDic:
            ltrDic[l] = 1
        else:
            ltrDic[l] = ltrDic[l] + 1
    for l in s:
        if l not in visited:
            if ltrDic[l]%2!=0:
                retstr = retstr + l
                visited[l] = True
    if retstr == '':
        return 'Empty String'
    return retstr

print(super_reduced_string('aaabccddd'))
    

    