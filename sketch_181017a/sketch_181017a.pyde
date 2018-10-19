x = 450
a = 450
def setup():
    size(640, 480)

def draw():
    global x
    global a
    print(x)
    if x >= 640:
        x = 0
    if a >= 640:
        a = 0
    x += 3
    a += 6
    background(135,206,235)
    fill(255)
    noStroke()
    y = height/6
    ellipse(x, y, 50, 50)
    ellipse(x + 50, y, 50, 50)
    ellipse(x + 25, y - 25, 50, 50)
    ellipse(x + 25, y + 25, 50, 50)
    ellipse(x + 60, y - 25, 50, 50)
    ellipse(x + 60, y + 25, 50, 50)
    ellipse(x + 80, y, 50, 50)
    fill(0,128,0)
    rect(0, height - 50, width, 50)
    rect(width/2 - 125, height - 175, 250, 125)
    fill(255,0,0)
    triangle(width/2 - 150, height - 175, width/2 + 150, height - 175, width/2, height - 275)
    rect(width/2 - 25, height - 125, 50,75)
    fill(0,0,255)
    rect(a - 50, height - 120, 200, 50)
    rect(a, height - 150, 100,30)
    fill(255,0,0)
    ellipse(a, height - 70, 40, 40)
    ellipse(a + 100, height - 70, 40, 40)
    
