class Solution:
    def subArraySum(self,arr, n, s): 
       for i in range(n):
           sum=0
           for j in range(i,n):
               sum=sum+arr[j]
               if s==sum:
                   return i+1,j+1
               elif s<sum:
                   break
           