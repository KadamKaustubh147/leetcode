class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        # q.append(for ticket in tickets[::-1])
        for ticket in tickets:
            q.append(ticket)
        # n = len(tickets)
        time = 0 # or the number of iterations

        while q:
            front = q.popleft()
            front -= 1
            time += 1
            if front==0 and k==0:
                return time
            if front != 0:
                q.append(front)
            if k==0:
                k=len(q)-1
            else:
                k-=1

        return time
            
