def fib_print(n):
  """Print a Fibonacci series up to n"""
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a + b
  print()

def fib(n):
  """Returns a list of Fibonacci numbers up to n"""
  a, b = 0, 1
  results = []
  while a < n:
    results.append(a)
    a, b = b, a + b
  return results

def ask_ok(prompt, retries=4, reminder='Please try again'):
  """Prompt user for confirmation and optimally allow retries"""
  while True:
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise ValueError('Invalid user response')
    print(reminder)

ask_ok('Do you really want to quit?', 6)