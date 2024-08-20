'''4. Function Returning Multiple Values
</summary>
Problem: Create a function that returns both the area and 
circumference of a circle given its radius.
</details>'''

askInput = float(input("Enter the redius..."))
def circle(r):
    area = round(3.14*r*r,2)
    circ = round(2*3.14*r,2)
    return area,circ

# result = circle(askInput)
# print(result)

area,circ = circle(askInput)
print(f"Area of the circle is {area}")
print(f"Circumference of the cicle is {circ}")