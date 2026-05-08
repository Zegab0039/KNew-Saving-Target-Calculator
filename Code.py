
def zrfun(message):
  try:
    value = float(input(message))
    return value
  except ValueError:
    return 0.0
def onefun(c_blnc, c_mnths, c_mrate, c_mnthly, c_trgt):
  while c_blnc < c_trgt:
    c_blnc = c_blnc + (c_blnc * c_mrate)
    c_blnc = c_blnc + c_mnthly
    c_mnths = c_mnths + 1
  extra = c_blnc - c_trgt
  print(f"You will have {c_trgt:,.2f} in {c_mnths} months with an extra {extra:,.2f}!")
  return c_blnc, c_mnths
continueonsystem = True
while continueonsystem:
  print("Hello, welcome to Key NEWledge STC!")
  trgt = zrfun("First thing first, how much is your saving target?")
  loopmntly = True
  while loopmntly:
    mntly = zrfun("Ok, and how much can you save per month?")
    if mntly <= 0:
      print("Ops... You have to save at least a bit of money!")
    elif mntly > 0:
      loopmntly = False
      break
  i = zrfun("And how much is the interest rate in percentual? (if not, please submit 0)")
  blnc = 0
  mnths = 0
  if i > 0:
    arate = 1/100
    mrate = (1 + arate)**(1/12)-1
  else:
    mrate = 0
  blnc, mnths = onefun(0, 0, mrate, mntly, trgt)

  while True:
    left = input("Want to calculate again? Y/N")
    if left.lower() == "n":
      continueonsystem = False
      break
    elif left.lower() == "y":
      print("Restarting...")
      break
    else:
      print("I didn't understand, could you try again?")
