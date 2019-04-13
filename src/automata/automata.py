from PIL import Image, ImageDraw
import math

#name to save the automata
name_automata = 'test'
extension = '.png'

#automata's nodes and edges
nodes = list(['1','2','3']) #states
edges = list([['1','2','a'],['1','3','b'],['2','2','b']]) #[origin, destiny, symbol]

#image size
width = 400
heigth = 400

#circle radius
main_circle_radius = 150
node_radius = 15

#create new image
image = Image.new('RGBA', (width, heigth))
#create new draw object
draw = ImageDraw.Draw(image)

def BuildMainCircle():
    print("\tBuilding main circle...")
    
    global width, heigth, main_circle_radius
    global nodes, nodes_center

    h = int(width / 2)
    k = int(heigth / 2)

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
        x = int(math.cos(math.radians(angle)) * main_circle_radius + h)
        y = int(math.sin(math.radians(angle)) * main_circle_radius + k)

        #add new point
        nodes_temp = nodes[c - 1]
        nodes[c - 1] = [nodes_temp,x,y,angle] #convert ['1','2',...] to [['1',x,y],['2',x,y],...]

        c = c + 1
    return

def DrawNodes():
    print("\tDrawing nodes...")
    global name_automata
    global image, draw, node_radius

    #for each node in nodes
    for node in nodes:
        x = node[1]
        y = node[2]
        #draw a circle in the box
        box = (x - node_radius, y - node_radius, x + node_radius, y + node_radius)
        draw.ellipse(box, fill='black', outline ='blue')
        image.save(name_automata + extension)
    return

def DrawArrows():
    print("\tDrawing arrows...")
    global nodes, edges, name_automata
    global image, draw

    #draw line origin to destiny
    for edge in edges:
        origin = edge[0]
        destiny = edge[1]
        origin_center = [0,0] #x,y
        destiny_center = [0,0] #x,y

        #find origin and destiny centers
        for node in nodes:
            if origin in node:
                origin_center = [node[1],node[2]]
            if destiny in node:
                destiny_center = [node[1],node[2]]

        #if the orgin is different to destiny
        if origin != destiny:
            #draw line
            box = (origin_center[0], origin_center[1], destiny_center[0], destiny_center[1])
            draw.line(box, fill='black', width=2)
            image.save(name_automata + extension)
        elif origin == destiny:
            #draw circle
            
            pass

    return
    
def DrawAutomata():
    global name_automata
    print("Building automata ... {0}".format(name_automata))
    #Build main circle
    BuildMainCircle()
    #Draw nodes
    DrawNodes()

    DrawArrows()
    return

#Draw Automata
DrawAutomata()