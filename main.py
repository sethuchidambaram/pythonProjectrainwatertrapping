# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')


#spos -> start position value
#epos  -> end position value
#volume ->  the volume of the bars.
#calculated -> the volume of the variable bars.
#m1 -> map of starting point and end point
#global variable

m1={}

def volumecalculate(sp, ep, tub):
  print(m1)
  height = min(tub[sp],tub[ep])
  calculatedvolume = 0
  print("the value of height is", height)
  volume = 0
  i=sp
  while i <= ep:
    if tub[i] > height:
      i+=1
      continue
    else:
      calculatedvolume = tub[i] + calculatedvolume
      volume = volume + height
      print(calculatedvolume)
    i+=1
  b = volume - calculatedvolume
  print("the value of b sp and ep is", b,sp,ep)
  return b

#maxep ->

def totalvolumecalculation(tub):
  L1=[]
  volume = 0
  maxep = 0
  for key in m1.keys():
    L1.append(key)
  print("the value of L1 is",L1)
  i = 0
  while i < len(L1):
    print("the value of i inside total volume calculate", i)
    if tub[L1[i]] <= tub[m1[L1[i]]]:
      a=volumecalculate(L1[i],m1[L1[i]],tub)
      volume=a+volume
      print("the volume less is called,sp,ep", volume,L1[i],m1[L1[i]])
    else:
        maxepval = tub[m1[L1[i]]]
        sp = L1[i]
        ep = m1[L1[i]]
        maxep=i
        print("the value of maepval is", maxepval)
        print("the value of startingpos is", sp)
        print("the value of endingpos is", ep)

        while i < len(L1):
            print("the value of i inside total volume  else calculate", i)

            if tub[m1[L1[i]]] > maxepval:
              maxepval=tub[m1[L1[i]]]
              maxep=i
            i+=1
        print("the value of max value and max position is",maxepval,maxep)
        a=volumecalculate(sp,m1[L1[maxep]],tub)
        volume=a+volume
        print("the volume is",volume)
        i=maxep+1
        print("the value of i after return is",i)
        continue

    i+=1
  return volume

def positioncreation(sp,tub):
    i = sp
    ep = 0
    spos = tub[i]
    slope = tub[i + 1] - tub[i]

    while slope < 0 and i < (len(tub) - 1):
      slope = tub[i + 1] - tub[i]
      i += 1

    if i == len(tub) -1:
      ep=i
      m1[sp] = ep
      return ep

    i-=1
    while slope >= 0 and i < (len(tub) - 1):
      slope = tub[i + 1] - tub[i]
      i += 1

    if i == (len(tub) - 1)  and slope >=0:
      epos = tub[i]
      ep = i
      print("the value of ep is", ep)


    else:
      epos = tub[i - 1]
      ep = i - 1


    m1[sp] = ep
    print(m1)
    return ep




# ns - > negative slope count
# ps - > positive slope count
# sp -> starting position
# ep - > ending position
def rainwaterharvesting(tub):
    L1=len(tub)
    position=[]
    i=0
    ns=0
    ps=0
    sp=0
    ep=0
    tubvolume=0
    while i < L1-1:
        slope=tub[i+1] - tub[i]
        if slope < 0 and ns == 0:
          sp=i
        if slope < 0:
          ns+=1
#        elif ns > 0 and slope > 0:
#          ps +=1
        else:
          pass



        if ns > 0:
          position.append(sp)
          pos = positioncreation(sp,tub)
          ns = 0
          ps = 0
          i=pos
          continue


        i+=1

    return totalvolumecalculation(tub)


L1=[1,2,1,2,0,0,0,0]
L2=[15,14,13,12,11,12,13,12,11,10,9,8,7,8,9,10,11,12,13,14,13,12,11,12,13,14]
L3=[20,19,20,1,2,3,4,5,6,7,8]
L4=[15,14,13,6,11,12,13,12,11,10,9,8,7,8,9,10,11,12,13,14]
L5=[0,3,0,1,0,2,0,4,0,1,0,3,0,2,0,1,0]
L6= [5,4,1,2,1,4,5]
L7=[0,2,0,4,0,1,0,3,0,2,0,1,0]
L8=[0,1,2,1,0,1,2,1,0,1,2,1,0,1,2,1,0]
#a=volumecalculation(0,L4)
#print("the volume calculated is",a)
L9=[5,4,3,2,1,0]
L10=[0,1,2,3,4,5]
L11=[5,4,3,2,1,0,1,2,3,4,5]
L12=[1,2,3,4,5,5,4,3,2,1,0]
L13=[1,0]
L14=[0,1,0,2,1,0,1,3,2,1,2,1]
L15=[4,2,0,3,2,5]

b=rainwaterharvesting(L5)
print("the volume calculated is",b)


'''
c=volumecalculate(0,1,L13)
print("the value of c is",c)

'''


# See PyCharm help at https://www.jetbrains.com/help/pycharm/





















