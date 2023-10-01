class Solution:
    def longestCommonPrefix( strs:[str]) -> str:
        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]

        common_prefix=[]
        for i in range(min(len(first_str),len(last_str))):
            if first_str[i] == last_str[i]:
                common_prefix.append(first_str[i])
            else:
                break

        return ''.join(common_prefix)

    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))