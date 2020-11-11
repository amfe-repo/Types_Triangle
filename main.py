import math
import turtle  

def config_draw(color, scale, distance, angle):
  turtle.color(color)
  turtle.forward(distance * scale)
  turtle.left(180 - angle)


def draw(triangle):
  scale = 30
  
  config_draw("red", scale, triangle["b"]["side"],
   triangle["a"]["angle"])

  config_draw("blue", scale, triangle["c"]["side"],
    triangle["b"]["angle"])

  config_draw("green", scale, triangle["a"]["side"],
   triangle["c"]["angle"])



def formule_angle(a, b, c, angle_char):
  result = 0

  if angle_char == "A":
    result = ((b**2)+(c**2)-(a**2))
    result = result/float((2*b*c))
    
  if angle_char == "B":
    result = ((b**2)-(a**2)-(c**2))
    result = result/float((2*a*c)*(-1))
  
  if angle_char == "C":
    result = ((c**2)-(a**2)-(b**2))
    result = result/float((2*a*b)*(-1))
  
  result = math.acos(result)
  result = math.degrees(result)
  return result


def calculate_angle(a, b, c):
  A = B = C = 0
  
  A = formule_angle(a, b, c, "A")
  B = formule_angle(a, b, c, "B")
  C = formule_angle(a, b, c, "C")

  return A,B,C


def determinate_type(triangle):
  type_triangle = ""

  if triangle["a"]["side"] == triangle["b"]["side"]:
    if triangle["b"]["side"] == triangle["c"]["side"]:
      type_triangle = "Equilateral"
    else:
      type_triangle = "Isosceles"

  else:
    if triangle["a"]["side"] == triangle["c"]["side"]:
      type_triangle = "Isosceles"

    else:
      if triangle["b"]["side"] == triangle["c"]["side"]:
        type_triangle = "Isosceles"
      else:
        type_triangle = "Scalene"
  
  return type_triangle


a = b = c = 0

a = float(input("Take me first side: "))
b = float(input("Take me second side: "))
c = float(input("Take me third side: "))

angles = calculate_angle(a, b, c)

triangle = {
  "a":{
    "side":a, "angle":angles[0]
  },
  "b":{
    "side":b, "angle":angles[1]
  },
  "c":{
    "side":c, "angle":angles[2]
  }
}

print("\nThis triangle is: {}".format(determinate_type(triangle)))

print("\nThe angle A is: {}\nThe angle B is: {}\nThe angle C is {}\n".format(triangle["a"]["angle"], triangle["b"]["angle"], triangle["c"]["angle"]))

draw(triangle)