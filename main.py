# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#spos -> start position value
#epos  -> end position value
#volume ->  the volume of the bars.
#calculated -> the volume of the variable bars.

def volumecalculation(sp,tub):
    i=sp
    stack=[]
    spos=tub[i]
    slope=tub[i+1] - tub[i]
    while slope < 0:
      slope=tub[i+1] - tub[i]
      stack.append(tub[i])
      i+=1
    while slope >= 0 and i < len(tub) -1:
      slope=tub[i+1] - tub[i]
      stack.append(tub[i])
      i+=1
    epos = tub[i]
    ep = i-1
    print(stack)
    print("the value of epos and spos is",epos,spos)

    height=min(spos,epos)
    calculatedvolume=0
    print("the value of height is",height)
    volume = 0
    while len(stack) > 0:
      a=stack.pop()
      if a > height:
        continue
      else:
        calculatedvolume = a+calculatedvolume
        volume = volume+height
        print(volume)
    b=volume-calculatedvolume
    print("the value of b is", b)
    return (volume - calculatedvolume),ep



# ns - > negative slope count
# ps - > positive slope count
# sp -> starting position
# ep - > ending position
def rainwaterharvesting(tub):
    L1=len(tub)
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
        elif ns > 0 and slope > 0:
         ps +=1
        else:
          pass

        print("the value of i is",i)
        if ns > 0 and ps > 0:
          print("the volume calculation function is called and the value is",sp)
          a,pos = volumecalculation(sp,tub)
          print("the values are",a,pos)
          tubvolume = a+tubvolume
          ns = 0
          ps = 0
          i=pos
          continue

        i+=1
    return tubvolume


L1=[1,2,1,2,0,0,0,0]
L2=[15,14,13,12,11,12,13,12,11,10,9,8,7,8,9,10,11,12,13,14]
L3=[20,19,20,1,2,3,4,5,6,7,8]


#a=volumecalculation(0,L3)
#print("the volume calculated is",a)


b=rainwaterharvesting(L2)
print("the volume calculated is",b)
