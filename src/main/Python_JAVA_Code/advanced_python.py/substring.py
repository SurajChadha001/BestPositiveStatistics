def longest_common_substring(text1,text2):
  m = len(text1)
  n = len(text2)
  dp = [[0 for _ in range(n+1)]for _ in range(m + 1)]
  longest=0
  for i in range(1, m + 1):
    for j in range(1,n+1):
      if text1[i-1] == text2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
        longest = max(longest, dp[i][j])
      else:
        dp[i][j] = 0
substring=""
i=m
j=n
while i>0 and j>0:
  if dp[i][j]>0:
    substring=text1[i-1] + substring
    i-=1
    j-=1
  else:
    break
  return substring
  text1 = "geeksforgeeks"