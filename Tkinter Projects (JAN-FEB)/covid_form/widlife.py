from tkinter import *
root = Tk()
root.title("Wildlife Information")

animal_info = {
    "Tiger": "The Bengal Tiger is the national animal of both India and Bangladesh. The tiger’s coat is yellow to light orange, with stripes ranging from dark brown to black. The number of tigers has reduced dramatically in the past few years, due to poaching and human-tiger conflict.",
    "Lion": "Asiatic Lion aka the Indian Lion or Persian Lion is a lion subspecies that is endangered. It differs from the African lion by less inflated auditory bullae, a larger tail tuft and a less developed mane.",
    "Blackbuck": "The Blackbuck is an ungulate species of antelope and it is near threatened. The main threat to this species is poaching, predation, habitat destruction, overgrazing, inbreeding and sanctuary visitors.",
    "Leopard": "The snow leopard is a large cat native to the mountain ranges in Central and South Asia. Snow leopards have long, thick fur, and they are really strong."
}

jungle_image = PhotoImage(file="images/jungle2.png").subsample(2,2)
tiger_image = PhotoImage(file="images/tiger.png").subsample(6,6)
lion_image = PhotoImage(file="images/lion.png").subsample(6,6)
blackbuck_image = PhotoImage(file="images/blackbuck.png").subsample(7,7)
leopard_image = PhotoImage(file="images/leopard.png").subsample(4,4)

# Define frame dimensions
frame_width = 800
frame_height = 600

# Create a frame for the entire window
frame = Frame(root, width=frame_width, height=frame_height)
frame.pack()

# Create a canvas to display the jungle background image
canvas = Canvas(frame, width=frame_width, height=frame_height)
canvas.pack()

# Set jungle image as the background
canvas.create_image(frame_width // 2, frame_height // 2 , anchor=CENTER, image=jungle_image)

# Position animal images and information in the corners of the frame
corner_coordinates = [(50, 50), (frame_width - 400, 50), (frame_width - 400, frame_height - 300), (50, frame_height - 300)]

for coord, animal in zip(corner_coordinates, ["Tiger", "Lion", "Blackbuck", "Leopard"]):
    image = None
    if animal == "Tiger":
        image = tiger_image
    elif animal == "Lion":
        image = lion_image
    elif animal == "Blackbuck":
        image = blackbuck_image
    elif animal == "Leopard":
        image = leopard_image

    # Position animal image
    canvas.create_image(coord[0], coord[1], anchor=NW, image=image)
    
    # Position animal information text
    canvas.create_text(coord[0] + 100, coord[1], text=animal_info[animal], anchor=NW, width=250)

root.mainloop()