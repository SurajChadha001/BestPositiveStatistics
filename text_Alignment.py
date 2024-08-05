width = int(input())
letter = "H"
for i in range(0,width):
  print((letter+(2*i*letter)).center(width*2-1," "))
for _ in range (0, width+1):
    print (" "*(width//2)+letter*width+" "*(width*3)+letter*width) 
for _ in range(0,width//2+1):
   print(" "*(width//2) + letter * 5 * width)
for _ in range (0,width+1):
   print (" "*(width//2)+ letter * width + " "*(width*3) +  letter * width )
for i in range(0,width):
   print ((((letter*(width-1-i))+ letter + (letter*(width-1-i))).center(width*2-1, " ")).rjust(width*6-1," "))
