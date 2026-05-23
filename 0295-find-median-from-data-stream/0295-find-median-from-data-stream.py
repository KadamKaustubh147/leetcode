import heapq

class MedianFinder:

    def __init__(self):
        # h1 is maxheap, h2 is min heap
        self.h1, self.h2 = [], []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.h1, -1 * num)

        # right side should be greater than left side
        # 1 | 3 4 is correct
        # 1 4 | 3 is not
        if self.h2 and -self.h1[0] > self.h2[0]:
            nu = heapq.heappop(self.h1)
            heapq.heappush(self.h2,-nu)

        # length imbalance and pushing elements in h2 too
        if len(self.h1)-len(self.h2) > 1:
            nu = heapq.heappop(self.h1)
            heapq.heappush(self.h2,-nu)
        
        # print(self.h1, self.h2)
        
        if len(self.h2) - len(self.h1) > 1:
            # print("this ran")
            nu = heapq.heappop(self.h2)
            # print(nu)
            heapq.heappush(self.h1,-nu)
        
        
        # print(self.h1, self.h2)

    def findMedian(self) -> float:
        # three cases
        # case 1 --> both are of equal length --> then average of both the top elements

        if len(self.h1) == len(self.h2):
            return (-self.h1[0]+self.h2[0])/2
        elif len(self.h1) > len(self.h2):
            return -self.h1[0]
        else:
            return self.h2[0]
        
        
        
