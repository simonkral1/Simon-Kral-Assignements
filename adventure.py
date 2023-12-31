# all text generated by chatGPT for more immersion

game_start_message = """In a land long forgotten, amidst a time blurred between legend and reality, you find yourself awakening in a tower that whispers of despair and solitude. A heavy fog of confusion weighs on your mind, yet fragments of memories nudge at the corners of your consciousness - an urgent message, a perilous journey, and a kingdom hanging in the balance.

As your senses become more alert, the dismal confines of the tower become painfully apparent. The damp, moss-covered walls encase you, and the slender slits of windows offer only a glimpse of the freedom that lies beyond. Iron shackles clank eerily in the silence, their cold and unforgiving embrace a harsh reminder of the tower's dark past.

Your heart races, a flurry of urgency and determination surging within you. You cannot stay here, not now. The realm needs you, and time is slipping away with each passing moment. With resolve steeling in your veins, you know you must escape this wretched place and uncover the truth that lurks in the shadows of the castle.

As you rise, your resolve hardens, echoing the steely glint in your eyes. The adventure that unfolds before you is fraught with challenges and unknown dangers, but within you burns a flame of hope, a beacon in the engulfing darkness.

It's time to forge your path, to navigate through the intertwining passages of the looming castle that holds secrets in its very stones.

With a deep breath, you step forward, the journey of a lifetime awaits...

Welcome to the Adventure!"""

print(game_start_message)


# dictionaries as rooms

tower = {
    'id': 'tower',
    'Description': 'The tower looms, a somber mixture of a prison and sanctuary, with weathered stone walls and narrow windows that hint at the outside world. Inside, the damp air clings to your skin, and the weight of solitude hangs heavily, a constant companion in this place where hope seems to have fled. Iron shackles, remnants of its grim past, adorn the dark corners, whispering tales of despair to anyone who dares to listen. You find yourself on top of the tower.',
    'down': "great_hall", 
    'north': 'none', 
    'south': 'none', 
    'east': 'none', 
    'west': 'none',
    'up': 'none'
}

great_hall = {
    'id': 'great_hall',
    'Description': 'The great hall unfolds before you, a vast space of grandeur and decay intertwined. Arched windows, now hosting tendrils of ivy, allow fractured light to dance on the faded tapestries that tell tales of a golden era long past. A once magnificent chandelier hangs precariously, its crystals sharing whispers with the battered, yet stoic, tables below. The air holds a mixture of must and old wood, an aroma of times that once held laughter and feasts. Now, it stands in silent dignity, awaiting the echo of footsteps to once again fill its hallowed space with life and fervor.',
    'up': 'tower', 
    'south': 'gate', 
    'north': 'passage', 
    'east': 'none', 
    'west': 'none',
    'down' : 'none'
}
passage = {
    'id': 'passage',
    'Description': 'The passage is a narrow and dimly lit corridor, where the walls are lined with ancient tapestries depicting the valorous deeds of yesteryears. The floor, a worn path through centuries-old stone, echoes softly with each step, as if whispering secrets to those who pass. The flickering torches cast long, dancing shadows, leading you north towards the regal, yet foreboding, king\'s quarters.',
    'north': 'kings_quarters',
    'south': 'great_hall',
    'east': 'none',
    'west': 'none',
    'down' : 'none',
    'up': 'none'
}

kings_quarters = {
    'id': 'kings_quarters',
    'Description': "You find yourself in the King's Quarters, a place where wisdom and authority once converged. Shadows of grandeur linger in the delicate frescoes that adorn the walls, narrating tales of a time when the kingdom thrived under a wise and just rule. In one corner of the room, a majestic globe structure catches your eye, intricately detailed and adorned with constellations and celestial bodies. Beside it, a shelf lined with ancient scrolls and tomes beckons, holding secrets of the universe within its depths. As your gaze wanders, you notice a peculiar arrangement of star charts and diagrams that seem to whisper the secrets of the cosmos. You find a series of sketches that seem to map the very fabric of reality, where artistry meets intellect, the perfect blend of wonder and 'science'. Could this union of celestial beauty and earthly knowledge be the key to unlocking the gate that guards the realms beyond?",
    'north': 'none',
    'south': 'passage',
    'east': 'none',
    'west': 'none',
    'down' : 'none',
    'up': 'none'
}



gate = {
        'id': 'gate',
        'Description': 'Before you stands the imposing edifice of the ancient gate, a marvel of forgotten craftsmanship, intertwining reality with enigmatic magic. The immense stone doorway is adorned with intricate carvings of celestial beings and cryptic runes that seem to pulsate with a life of their own, holding secrets from a time immemorial. A heavy silence hangs in the air, a quietude that seems to hum with the expectation of the spoken word, a password that would unlock the mysteries that lie beyond. The guardian stones flanking the gateway emanate a gentle, pulsating glow, hinting at the dormant magic that awaits to be awakened. Here, at the precipice of the known and the unknown, you feel the weight of history and the pull of adventure, urging you to find the key that would unlock the path forward into the realms of legend and myth.', 
       
       'north': 'great_hall', 
       'south': 'none',
       'east': 'none', 
       'west': 'none',
       'down' : 'none',
       'up': 'none'
       }

# dictionary of dictionaries for grouping rooms

rooms = {
    "tower": tower,
    "great_hall": great_hall,
    "passage": passage,
    "kings_quarters": kings_quarters,
    "gate": gate
}


current_room = tower



print(current_room['Description'])

# function for moving around the castle has extra feature launching the gate password function when player is at the gate

def move(current_room, rooms):
    direction = input("Which way do you want to go? (north, south, east, west,up, down) ").lower()

    if current_room['id'] == 'gate':
        if gate_password():
            return 'end'
    
    if direction in ['north', 'south', 'east', 'west', 'up', 'down']:
        if current_room[direction] != 'none':
            new_room_name = current_room[direction]
            current_room = rooms[new_room_name]
            print(current_room['Description'])
        else:
            print("You can't move further in this direction.")
    else:
        print("Invalid direction. Please try again.")
    
    return current_room

# player needs to enter the correct password to escape the castle and win the game. Password is located in the kings quarters

def gate_password():
    password = input("What password will you try?")
    if password == "science":
        print("The gate hums and vibrates with a resonance that echoes the wisdom embedded in your uttered password. Slowly, the ancient mechanism gives way, the giant stone doors parting with a sound like the murmuring of old rivers. A burst of fresh air, carrying the scent of freedom and wildflowers, meets you as you step through the gateway, leaving the shadows of the castle behind. You have emerged victorious, stepping into a new dawn, a world ripe with possibilities and adventures yet to be discovered. Farewell, brave voyager, until we meet again in tales yet untold.")
        return True  
    else:
        print("With bated breath, you whisper the password, hoping to witness the magical gateway yield to your command. The seconds stretch into an eternity, your heartbeat loud in the pressing silence. The runes on the gate remain dark, the expected hum of awakening magic absent. The anticipated symphony of mechanisms springing to life never comes. Nothing happens, the gate remains steadfast, unyielding, leaving you amidst the echoing silence, a crescendo of hope deflated. Your heart sinks as the reality dawns - it was not the right password. The journey, it seems, is far from over.")
        return False  

# ends the game loop and gives option to play again
while True:
    current_room = tower
    
    
    while current_room != 'end':
        current_room = move(current_room, rooms)

    play_again = input("Do you want to play again? (yes or no): ").lower()
    if play_again != 'yes':
        break





