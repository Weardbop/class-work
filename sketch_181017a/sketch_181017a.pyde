x = 450

def setup():
    size(640, 480)

def draw():
    global x
    print(x)
    if x >= 640:
        x = 0
    x += 3
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
    
