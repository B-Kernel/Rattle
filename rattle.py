import os
import time
import subprocess
os.system('color 1f')
Rattle = True
def titlebar():
  print("(N)ew","(C)ompile","(O)pen","(E)xit")
titlebar()
time.sleep(1)
while Rattle == True:
  Rattle_Command = input()
  if Rattle_Command == "E" or Rattle_Command == "Exit":
    Rattle = False
  elif Rattle_Command == "C" or Rattle_Command == "Compile":
    os.system('cls')
    titlebar()
    Rattle_Subcommand = input("PATH: ")
    try:
      with open(Rattle_Subcommand, "r") as filer:
        os.system('cls')
        titlebar()
        exec(filer.read())
    except:
      os.system('color 4f')
      print("An Error has occured.")
      time.sleep(3)
      os.system('color 1f')
      os.system('cls')
      titlebar()
  elif Rattle_Command == "N" or Rattle_Command == "New":
    Rattle_Temp = True
    os.system('cls')
    titlebar()
    Rattle_Subcommand = input("PATH: ")
    with open(Rattle_Subcommand, "w") as filer:
      os.system('cls')
      print("Write Code Here...")
      while Rattle_Temp == True:
        me = input()
        if me != "$EXIT":
          filer.write(me)
          filer.write("\n")
        else:
          break
