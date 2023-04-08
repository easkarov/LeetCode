class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        d = {}

        for k, let in enumerate(s):
            if let not in d:
                d[let] = [k, k]
                continue
            d[let][1] = k

        vs = sorted(d.values())
        ans = []

        s, f = vs[0]
        for i in range(1, len(vs)):
            a, b, = vs[i]

            if s <= a <= f:
                f = max(f, b)
                continue

            ans.append(f - s + 1)
            s = a
            f = b

        ans.append(f - s + 1)
        return ans
