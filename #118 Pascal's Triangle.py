'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        r = [[1]]
        for i in range(2,numRows+1):
            lastRow = r[-1]
            row = [1,1]
            for j in range(i-2):
                row.insert(-1, lastRow[j]+lastRow[j+1])
            r.append(row)
        return r