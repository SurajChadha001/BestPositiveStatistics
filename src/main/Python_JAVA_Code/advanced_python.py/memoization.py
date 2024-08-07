def memoize(func):
  cache={}
def memoized_func(*args):
  if args in cache:
    return cache[args]
  else:
    result=func(*args)
    cache[args]=result
    return result
  return memoized_func
  def fibonacci(n):
    if n==0 or n==1:
      return n
    else:
      return fibonacci(n-1)+fibonacci(n-2)
      result = fibonacci(35)
      calculations
      print("Fibonacci of 35:{result}")