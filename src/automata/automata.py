from PIL import Image, ImageDraw, ImageFont
import math

#name to save the automata
name_automata = 'test'
extension = '.png'

#automata's nodes and edges
nodes = list(['0','1','2']) #states
edges = list([['0','1','a'],['0','2','b'],['1','1','b']]) #[origin, destiny, symbol]

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
    global nodes

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
        nodes[c - 1] = [nodes_temp,x,y,angle] #convert ['1','2',...] to [['1',x,y,angle],['2',x,y,angle],...]

        c = c + 1
    return

def DrawNodes():
    print("\tDrawing nodes...")
    global name_automata, extension
    global image, draw, node_radius
    global nodes

    #for each node in nodes
    for node in nodes:
        x = node[1]
        y = node[2]
        #draw a circle in the box
        box = (x - node_radius, y - node_radius, x + node_radius, y + node_radius)
        draw.ellipse(box, fill='white', outline ='black',width=2)
        #draw state
        draw.text((x - 2,y - 5), node[0], fill='black')
        image.save(name_automata + extension)
    return

def DrawArrows():
    print("\tDrawing arrows...")
    global nodes, edges, name_automata, extension
    global image, draw, node_radius

    #draw line origin to destiny
    for edge in edges:
        origin = edge[0]
        destiny = edge[1]
        origin_center = [0,0] #x,y
        destiny_center = [0,0] #x,y
        angle = 0

        #find origin and destiny centers
        for node in nodes:
            if origin in node:
                origin_center = [node[1],node[2]]
                angle = node[3]
            if destiny in node:
                destiny_center = [node[1],node[2]]
                angle = node[3]

        #if the origin is different to destiny
        if origin != destiny:
            #draw line
            box = (origin_center[0], origin_center[1], destiny_center[0], destiny_center[1])
            draw.line(box, fill='black', width=2)
            image.save(name_automata + extension)
        elif origin == destiny:
            #draw circle
            h_node = origin_center[0]
            k_node = origin_center[1]
            arrow_radius = 10
            x = int(math.cos(math.radians(angle)) * node_radius + h_node)
            y = int(math.sin(math.radians(angle)) * node_radius + k_node)

            #draw a circle in the box
            box = (x - arrow_radius, y - arrow_radius, x + arrow_radius, y + arrow_radius)
            draw.ellipse(box, outline = 'black', width=2)
            image.save(name_automata + extension)

    return
    
def DrawAutomata():
    global name_automata
    print("Building automata ... {0}".format(name_automata))
    #Build main circle
    BuildMainCircle()
    #Draw arrows
    DrawArrows()
    #Draw nodes
    DrawNodes()
    return

#Draw Automata
DrawAutomata()