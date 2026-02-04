class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        started = False
        ended = False

        result = []   # new array to build answer

        for d in num:
            digit = int(d)

            if change[digit] > digit and not ended:
                started = True
                result.append(str(change[digit]))

            elif change[digit] == digit:
                result.append(d)

            elif change[digit] < digit and not started:
                result.append(d)

            elif change[digit] < digit and started:
                ended = True
                result.append(d)
            elif change[digit] > digit and ended:
                result.append(d)

        return "".join(result)