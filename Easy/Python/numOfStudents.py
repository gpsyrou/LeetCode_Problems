'''
1450. Number of Students Doing Homework at a Given Time


Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
'''

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
                
        return sum([1 for t in range(len(startTime)) if  (startTime[t] <= queryTime) & (queryTime <= endTime[t])])

