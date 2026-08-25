class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for i in range(len(output)):
            for string in strs:
                if i == len(string) or string[i] != output[i]:
                    return string[:i]
        return output
        
        # output = strs[0]
        # for string in strs:
        #     if not string:
        #         return ""
        #     compare = min(len(output), len(string))
        #     for i in range(1, compare-1):
        #         if string[i] != output[i]:
        #             break
        #         output = output[:i]         

        # return output    