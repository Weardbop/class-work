x = 450
x2 = 450
x3 = 150
y2 = 0
y_diff = 3
def setup():
    size(640, 480)

def draw():
    global x
    global x2
    global x3
    global y2
    global y_diff
    print(x)
    if x >= 640:
        x = 0
    if x2 >= 640:
        x2 = 0
    if y2 > 430 or y2 < 0:
        y_diff *= -1
    y2 += y_diff
    x += 3
    x2 += 6
    background(135,206,235)
    fill(255)
    noStroke()
    y = height/6
    
    #cloud
    ellipse(x, y, 50, 50)
    ellipse(x + 50, y, 50, 50)
    ellipse(x + 25, y - 25, 50, 50)
    ellipse(x + 25, y + 25, 50, 50)
    ellipse(x + 60, y - 25, 50, 50)
    ellipse(x + 60, y + 25, 50, 50)
    ellipse(x + 80, y, 50, 50)
    
    #house
    fill(0,128,0)
    rect(0, height - 50, width, 50)
    rect(width/2 - 125, height - 175, 250, 125)
    fill(255,0,0)
    triangle(width/2 - 150, height - 175, width/2 + 150, height - 175, width/2, height - 275)
    rect(width/2 - 25, height - 125, 50,75)
    
    #car
    fill(0,0,255)
    rect(x2 - 50, height - 120, 200, 50)
    rect(x2, height - 150, 100,30)
    fill(255,0,0)
    ellipse(x2, height - 70, 40, 40)
    ellipse(x2 + 100, height - 70, 40, 40)
    
    #flying saucer
    fill(0,255,0)
    ellipse(x3, y2 - 20, 80, 80)
    fill(128,128,128)
    ellipse(x3, y2, 150, 60)
