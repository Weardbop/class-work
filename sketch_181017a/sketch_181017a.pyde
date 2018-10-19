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
    rect(x, height - 150, 3, 100)
