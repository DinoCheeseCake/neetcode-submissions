class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        time_st = []
        for p, s in sorted(pair)[::-1]:
            time_st.append((target-p)/s)
            if len(time_st) >= 2 and time_st[-1] <= time_st[-2]:
                time_st.pop()
        return len(time_st)