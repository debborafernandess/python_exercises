import sys

# Parse args
list = sys.argv[1].split(',')

def sentence(list):
  phrase = ''

  for i in list[:-2]:
    phrase += i + ', '

  phrase += list[-2] + ' and ' + list[-1]

  print(phrase)


sentence(list)
