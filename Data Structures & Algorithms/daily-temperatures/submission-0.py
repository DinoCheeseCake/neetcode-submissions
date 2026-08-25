class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        st = [] # pair: [temp, idx]
        for idx, tmp in enumerate(temperatures):
            
            while st and tmp > st[-1][0]:
                st_tmp, st_idx = st.pop()
                res[st_idx] = idx-st_idx
            
            st.append([tmp, idx])

        return res