from PIL import Image, ImageDraw
import math

#name to save the automata
name_automata = 'test'

#automata's nodes and edges
nodes = list(['1','2','3']) #states
edges = list([['1','2','a'],['1','3','b'],['2','2','b']]) #[origin, destiny, symbol]
nodes_center = list()

#image size
width = 400
heigth = 400

#create new image
image = Image.new('RGBA', (width, heigth))
#create new draw object
draw = ImageDraw.Draw(image)

def BuildMainCircle():
    print("\tBuilding main circle...")
    
    global width, heigth
    global nodes, nodes_center

    h = int(width / 2)
    k = int(heigth / 2)
    radius = 80

    #initial angle
    angle = 0
    #angle seperation
    angle_separation = int(360 / len(nodes))

    x = 0
    y = 0

    c = 1
    while c <= len(nodes):
        #next point
        angle = angle + angle_separation
        x = int(math.cos(math.radians(angle)) * radius + h)
        y = int(math.sin(math.radians(angle)) * radius + k)

        #add new point
        nodes_center.append([x,y])

        c = c + 1
    return

def DrawNodes():
    print("\tDrawing nodes...")
    global nodes_center, name_automata
    global image, draw
    radius = 15

    for point in nodes_center:

        box = (point[0] - radius, point[1] - radius, point[0] + radius, point[1] + radius)
        draw.ellipse(box, fill='blue', outline ='blue')
        image.save(name_automata + '.png')
    return

    
def DrawAutomata():
    global name_automata
    print("Building automata ... {0}".format(name_automata))
    #Build main circle
    BuildMainCircle()
    #Draw nodes
    DrawNodes()
    return

def DrawArrows():
    print("\tDrawing arrows...")
    global edges, nodes_center, name_automata
    global image, draw
    radius = 15

    

    return

#Draw Automata
DrawAutomata()