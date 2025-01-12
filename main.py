from fractions import Fraction
counter = 0
stringctrs = list("`1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./")
shifteds = list('~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?')
shifts = dict(zip(stringctrs, shifteds))
strind = 0
stringcounter = stringctrs[strind]
shifted = False
numbers = {0:0}
cntrind = 0
pastrns = 0
looping = False
loopnumming = True
loopnum = ''
loopcode = ''
rloop = False
frac = False
f = open('file.txt')
def readit(txt):
  global strind
  global stringcounter
  global shifted
  global cntrind
  global pastrns
  global loopnum
  global looping
  global loopcode
  global loopnumming
  global rloop
  global frac
  ltxt = list(txt)
  for i in range(len(ltxt)):
    j = ltxt[i]
    if pastrns:
      pastrns -= 1
      continue
    if looping:
      if loopnumming:
        if j == '@':
          rloop = True
          continue
        num = '0'
        k = i
        while num.isnumeric():
          num += ltxt[k]
          k += 1
        num = num[1:-1]
        loopnum = int(num)
        loopnumming = False
      elif not loopnumming:
        if j == ')':
          looping = False
          loopnumming = True
          if rloop:
            for k in range(loopnum, 0, -1):
              readit(loopcode[1:].replace("'", str(k)))
          else:
            for k in range(1, loopnum+1):
              readit(loopcode[1:].replace("'", str(k)))
          loopcode = ''
          loopnum = ''
          rloop = False
        else:
          loopcode += j
      continue
    if j == 'à':
      strind -= 1
    elif j == 'á':
      strind += 1
    elif j == 'o':
      if shifted:
        print(shifts[stringcounter], end='')
      else:
        print(stringcounter, end='')
    elif j == 'â':
      shifted = True if shifted == False else false
    elif j == 'ä':
      num = '0'
      k = i+1
      while num.isnumeric():
        num += ltxt[k]
        k += 1
      num = num[1:-1]
      strind = int(num)
      pastrns = len(num)
    elif j == '+':
      numbers[cntrind] += 1
    elif j == '-':
      numbers[cntrind] -= 1
    elif j == 't':
      numbers[numbers.keys()[-1]+1] = 0
    elif j == 'l':
      del numbers[numbers.keys()[-1]]
      if cntrind > numbers.keys()[-1]:
        cntrind = numbers.keys()[-1]
    elif j == '>':
      cntrind += 1
    elif j == '<':
      cntrind -= 1
    elif j == 'ö':
      if frac:
        print(f'{Fraction(numbers[cntrind]).limit_denominator()}', end='')
      else:
        print(numbers[cntrind], end='')
    elif j == 'š':
      num = '0'
      k = i+1
      while num.isnumeric():
        num += ltxt[k]
        k += 1
      num = num[1:-1]
      cntrind = int(num)
      pastrns = len(num)
    elif j == 'ʂ':
      num = '0'
      k = i+1
      while num.isnumeric():
        num += ltxt[k]
        k += 1
      num = num[1:-1]
      numbers[cntrind] = int(num)
      pastrns = len(num)
    elif j == 'ü':
      print(eval(f'\'\\u{txt[i+1:i+5]}\''), end='')
      pastrns = 4
    elif j == 'P':
      print()
    elif j == '(':
      looping = True
    elif j == 'S':
      print(end=' ')
    elif j == 'm':
      num = '0'
      k = i+1
      while num.isnumeric():
        num += ltxt[k]
        k += 1
      num = num[1:-1]
      numbers[cntrind] = numbers[cntrind] * int(num)
      pastrns = len(num)
    elif j == 'd':
      num = '0'
      k = i+1
      while num.isnumeric():
        num += ltxt[k]
        k += 1
      num = num[1:-1]
      numbers[cntrind] = numbers[cntrind] / int(num)
      pastrns = len(num)
    elif j == 'f':
      frac = True if shifted == False else False
    stringcounter = stringctrs[strind]
readit(f.read())
