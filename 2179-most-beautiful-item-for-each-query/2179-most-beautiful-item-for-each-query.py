import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        st = []
        items.sort(key=lambda x: x[0])

        for [price,beauty] in items:
            if not st:
                st.append((price,beauty))
                continue
            # print(st)
            if st[-1][0] == price and st[-1][1]<beauty:
                st.pop()
            # print("After pop", st)
            if not st or beauty > st[-1][1] :
                st.append((price,beauty))

        # processing queries
        ans = []
        for q in queries:
            pos = bisect.bisect_right(st,q,key=lambda x:x[0])
            # print(pos)
            # print(st)
            if pos == 0:
                ans.append(0)
                continue
            ans.append(st[pos-1][1])

        return ans

        

        
        