from turtle import*

color('red', 'yellow')

begin_fill()
while True: 
  forward(500)
  left(170)
  if abs(pos()) < 1: 
    break
end_fill()
done()

# def line(size): 
#   forward(size)
#   right(90)
#   forward(size)
#   right(90)
#   forward(size)
#   right(90)
#   forward(size)
  
# line (150)
# right(30)
# square(250)
# input()