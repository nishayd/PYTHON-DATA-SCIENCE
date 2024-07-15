from turtle import *
speed("fastest")
s=5 
d=100
for i in range(s):
    fd(d)
    lt(360/s)
    write(i, font=("arial", 12, "normal"))
    circle(360/s)

mainloop()
