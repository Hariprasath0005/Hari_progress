import math
def paint_calc(height,width,cover):
  num = math.ceil(height*width/cover)
  print(f"You'll need {num} cans of paint.")

test_h = int(input("Enter the height:")) # Height of wall (m)
test_w = int(input("Enter the weight:")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)