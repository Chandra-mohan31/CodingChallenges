def longestCommonPrefix(strs):
    l = len(strs)
    out_str = " "
    for i in range(l):

        # l_str = len(strs[i])
        if(i+1 < len(strs) and strs[i][i] == strs[i+1]):
            out_str += strs[i][i]

    return out_str


print(longestCommonPrefix(["flower", "flow"]))
