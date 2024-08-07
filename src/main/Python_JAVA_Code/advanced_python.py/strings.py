def minimum_edit_distance_dp(str1,str2):
  m=len(str1)+1
  n=len(str2)+1
  dp=[[0 for _ in range(n)]for _ in range(m)]
  for i in range(m):
    dp[i][0]=i
    string to str1[0:i]
    for j in range(n):
      dp[0][j]=j
      string to str2[0:j]
      for i in range(1,m):
        for j in range(1,n):
          if str1[i-1]==str2[j-1]:
            dp[i][j]=dp[i-1][j-1]
          else:
            insertion = dp[i][j-1]+1
            deletion = dp[i-1][j]+1
            substitution = dp[i-1][j-1]+1
            dp[i][j]=min(insertion,deletion,substitution)
            return dp[m-1][n-1]
            right corner 
str1='Kitten'
str2="sitting"
distance=minimum_edit_distance_dp(str1,str2)
print(f"Minimum edit distance between '{str1}' and '{str2}':{distance}"")