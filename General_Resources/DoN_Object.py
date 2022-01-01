# version 2022.01.01

#####################################################################
# General DoN Obj: Character, Dungeon Level, Room, Item, Swarm, Etc. 
#####################################################################

class DoN_Object:

    ##############
    # Constructor
    ##############
    def __init__(self,
                 blurb = '', 
                 health_status = 1,
                 avatar = 'x',
                 name = "No_Name", 
                 element = 1, 
                 health_points = 10,
                 root_hit_points = 2, 
                 hit_points = 2, 
                 micro_location = (11,9),  # micro_location_in_room_or_riding_on
                 macro_location = None,  # macro_location_which_dungeon_room_or_riding_on
                 inventory = [],  # carying objects for moving around
                 enchantment_list = [],
                 swarm_list = [],
                 active_items = [],  # items used in actions
                 flags = {},

                 # For Inside_of_Room Features:
                 door_location = (-2, 2),
                 size_of_room = (12, 12),
                 floor_tile = " ",
                 padding = "  ", 
                 dungeon_room = [],

                 # For Duneon Level Rooms
                 room_id = None, 
                 room_name = None, 
                 room_description = None, 
                 room_X = None, 
                 room_y = None,

                 # For Characters
                 character_and_item_dictionary = {},
                 party_location = 0
                 ):


        ######################
        # Instance Attributes
        ######################

        self.blurb = blurb
        self.avatar = avatar  # single character str
        self.health_status = health_status  # 1 = healthy, 0 = ailing, -1 = unconcious
        self.name = name  # plain language name
        self.element = self.element_lookup[element]  # (1,2,3,4,5)
        # self.element = element
        self.health_points = health_points  # (int) stating health
        self.hit_points = hit_points  # (int) starting Hitpoints
        self.root_hit_points = hit_points  # (int)

        # Contains and Contains-by (other objects)
        """
        Explaining micro_location and macro_location:
        micro_location_in_room_or_riding_on = micro_location_in_room_or_riding_on  # object.location / (1,2)
        macro_location_which_room_or_riding_on = macro_location_which_room_or_riding_on  # object.location (1,2,0,0,0) (room x, room y, level-floor, which-building, etc.)
        """
        self.micro_location = micro_location
        self.macro_location = macro_location
        self.inventory = inventory  # list
        self.enchantment_list = enchantment_list
        self.swarm_list = swarm_list

        self.active_items = active_items
        self.flags = {
            "auto_react": False,
            "reflect": False,
            "swarm": False,
            # "has_swarm" : False,
            # "swarm_id": False,
                 }
        self.enchantment_list = enchantment_list
        # your_element: How_other_element_effects_you
        self.effect_dictionary = {
            # 1
            (1,1): 0,
            (1,2): 0,
            (1,3): 0,
            (1,4): -1,
            (1,5): 1,
            # 2
            (2,1): 1,
            (2,2): 0,
            (2,3): 0,
            (2,4): 0,
            (2,5): -1,
            # 3
            (3,1): -1,
            (3,2): 1,
            (3,3): 0,
            (3,4): 0,
            (3,5): 0,
            # 4
            (4,1): 0,
            (4,2): -1,
            (4,3): 1,
            (4,4): 0,
            (4,5): 0,
            # 5
            (5,1): 0,
            (5,2): 0,
            (5,3): -1,
            (5,4): 1,
            (5,5): 0,
        }
        # for inside_of_rooms
        self.door_location = door_location
        self.size_of_room = size_of_room
        self.floor_tile = floor_tile
        self.padding = padding  # for printing
        self.dungeon_room = dungeon_room

        # Duneon Level Rooms Attributes
        self.room_id = room_id
        self.room_name = room_name
        self.room_description = room_description
        self.n_to_room = None
        self.s_to_room = None
        self.e_to_room = None
        self.w_to_room = None
        self.room_X = room_X
        self.room_y = room_y
        self.room_dictionary = {}
        
        # Dungeon_Level Attributes
        self.dungeon_level_grid = None
        self.dungeon_level_width = 0
        self.dungeon_level_height = 0

        # Characters
        self.character_and_item_dictionary = character_and_item_dictionary
        self.party_location = party_location

    ###############
    # Dictionaries
    ###############

    element_lookup = {
        1:1,
        2:2,
        3:3,
        4:4,
        5:5,
        'water':1,
        'forest':2,
        'fire':3,
        'void':4,
        'ice':5,
        'Water':1,
        'Forest':2,
        'Fire':3,
        'Void':4,
        'Ice':5
    }

    element_dict = {
        1:'water',
        2:'forest',
        3:'fire',
        4:'void',
        5:'ice',
    }


    ######################
    # Methods (Functions)
    ######################

    """
    diversify how the object is printed
    """

    # Nicer Print
    def __repr__(self):
    #     return f"{self.blurb}"
    # Fix this later - still just room-print
    # def room_print(self):
        if self.e_to_room is not None:
            return f"({self.room_X}, {self.room_y}) -> ({self.e_to_room.room_X}, {self.e_to_room.room_y})"
        return f"({self.room_X}, {self.room_y})"

    def print_room_links(self, object_1=None):
        # default to describing yourself
        if object_1 is None:
            object_1 = self

        if object_1.e_to_room is not None:
            return f"({object_1.room_X}, {object_1.room_y}) -> ({object_1.e_to_room.room_X}, {object_1.e_to_room.room_y})"
        return f"({object_1.room_X}, {object_1.room_y})"

    def print_dungeon_level_grid(self):
        for i in range(0, len(self.room_dictionary)):
        #     print(self.room_dictionary[i])
            # call room link function(medthod)
            self.print_room_links(object_1=self.room_dictionary[i])

        # for i in self.dungeon_level_grid:
            # if self.e_to_room is not None:
            #     return f"({self.room_X}, {self.room_y}) -> ({self.e_to_room.room_X}, {self.e_to_room.room_y})"
            # return f"({self.room_X}, {self.room_y})"


    ##########################
    # For Dungeon Level Rooms
    ##########################

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to_room", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to_room", self)

    def get_room_in_direction(self, direction):
        '''
        Find out what room
        '''
        return getattr(self, f"{direction}_to_room")


    #################
    # Dungeon Levels
    #################

    # TODO: modify or diversify this to make more types of patterns
    def dungeon_level_procedural_generation_algorithm(self, d_level_size_x, d_level_size_y, dungeon_level_number_of_rooms):
        '''
        Super Simple dungeon_level_procedural_generation_algorithm:
        A basic snake pattern within a preset-sized dungeon_level_grid.
        '''

        # Initialize the dungeon_level_grid
        self.dungeon_level_grid = [None] * d_level_size_y
        self.dungeon_level_width = d_level_size_x
        self.dungeon_level_height = d_level_size_y
        for i in range( len(self.dungeon_level_grid) ):
            self.dungeon_level_grid[i] = [None] * d_level_size_x

        # Start from lower-left corner (0,0)
        X_for_room = -1 # (this will become 0 on the first step)
        y_for_room = 0
        room_number_counter = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None
        while room_number_counter < dungeon_level_number_of_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and X_for_room < d_level_size_x - 1:
                room_direction = "e"
                X_for_room += 1
            elif direction < 0 and X_for_room > 0:
                room_direction = "w"
                X_for_room -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y_for_room += 1
                direction *= -1

            # Create a room in the given direction
            room = DoN_Object(inventory=[], room_id=room_number_counter, room_name="A Generic Room", room_description="This is a generic room.", room_X=X_for_room, room_y=y_for_room)
            # Note that in Django, you'll need to save the room after you create it

            # add room features to room-objects
            room.make_a_dungeon_room()

            # TODO fix this
            # # add to inventory list
            # self.inventory.append[room]

            # add room to room dictionary
            self.room_dictionary[room_number_counter] = room

            # add room to level inventory
            self.inventory.append(room)

            # Save the room in the World dungeon_level_grid
            self.dungeon_level_grid[y_for_room][X_for_room] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connect_rooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_number_counter += 1

        ###############
        # Housekeeping
        ###############

        # Make Room-Zero the Staircase
        self.dungeon_level_grid[0][0].room_id = "_-S"


    def dungeon_level_print_rooms(self):
        '''
        Print the rooms in room_dungeon_level_grid, 
        in ascii characters,
        to a termianl (or notebook)

        The console prints top to bottom 
        but array is arranged bottom to top.
        
        So reverse the array so the print is drawn in the right direction.
        '''

        # Add top border
        str = "# " * ((3 + self.dungeon_level_width * 5) // 2) + "\n"

        # make a copy of the list
        reverse_dungeon_level_grid = list(self.dungeon_level_grid) 
        # reverse the copy
        reverse_dungeon_level_grid.reverse()


        #####################
        # Print The Dungeon!
        #####################

        # Iterate through table of rooms and print
        for row in reverse_dungeon_level_grid:

            # Print NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to_room is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

            # Print ROOM ROW
            str += "#"
            for room in row:
                # check for a room to the West
                if room is not None and room.w_to_room is not None:
                    str += "-"
                else:
                    str += " "

                if room is not None:
                    #zfill is vanilla python to pad length for standarization
                    str += f"{room.room_id}".zfill(3)
                else:
                    str += "   "
                
                # check for a room to the East
                if room is not None and room.e_to_room is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"

            # Print SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to_room is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.dungeon_level_width * 5) // 2) + "\n"

        # Print string
        print(str)

    ######
    # Set
    ######
    def set_avatar(self, avatar):
        self.avatar = avatar

    def set_name(self, name):
        self.name = name

    def set_health_points(self, health_points):
        self.health_points = health_points

    def set_hit_points(self, hit_points):
        self.hit_points = hit_points

    # set place in room (or ride)
    def set_micro_location(self, set_micro_location):
        self.micro_location = set_micro_location

    # set room (or ride)
    def set_macro_location(self, set_macro_location):
        self.macro_location = set_macro_location

    # def set_inventory(self, inventory):
    #    self.inventory = inventory


    # TODO
    # ...system for removing from last place and adding to next?
    def set_as_your_location(self, room_id):
        room_id.inventory.append(self)

    def remove_as_your_location(self, room_id):
        room_id.inventory.remove(self)
    # 
    # def set_as_object_location(self, room_id, object_id):
    #     room_id.inventory.append(object_id)

    def remove_as_object_location(self, object_id, room_id):
        room_id.inventory.remove(object_id)


    ###############
    # Add / Remove
    ###############

    def add_to_inventory(self, new_object):
        self.inventory.append(new_object)

    def remove_from_inventory(self, old_object):
        self.inventory.remove(old_object)

    def add_to_enchantment_list(self, new_object):
        self.enchantment_list.append(new_object)

    def add_to_enchantments(self, new_object):
        self.enchantment_list.append(new_object)

    def add_to_swarm_list(self, new_object):
        self.swarm_list.append(new_object)

    def add_to_swarms(self, new_object):
        self.swarm_list.append(new_object)


    #######
    # Misc
    #######

    def report(self):
        print( "inventory   = ", self.inventory )
        print( "len of      = ", len(self.inventory ) )
        print( "elements of = ", self.print_inventory_element() )

    def print_inventory_blurbs(self):
        for item in self.inventory:
            print(item.blurb)

    def print_inventory_names(self):
        for item in self.inventory:
            print(item.name)

    def print_inventory_elements(self):

        list_of_elements = []

        # iterate list of riders and append their elements to a list
        for item in self.inventory:
            get_element = self.element_dict[item.element]
            get_element = item.element
            list_of_elements.append(get_element)

        return list_of_elements

    def activate_item(self, item):
        self.active_items_list.append(item)

    def deactivate_item(self, item):
        self.active_items_list.remove(item)

    def get_element(self):
        return self.element_dict[self.element]

    ##############################
    # Effects & (magic)"Elements"
    ##############################

    """
    The basic modality(?) is that if the other element is + effects_you
    your health and hitpoints get boosted
    
    if the other element is - effects_you
    
    1. water
    2. forest
    3. fire
    4. void
    5. ice
    """

    def calculate_effect(self, other_element, give_or_get):
        if give_or_get == "get":
            return self.effect_dictionary[(self.element, other_element)]
        elif give_or_get == "give":
            return self.effect_dictionary[(other_element, self.element)]
        else:
            print(f"input error: calculate_effect: {give_or_get}")


    def check_health(self, for_this_object):
        if for_this_object.health_status == 0:
            print(f"{for_this_object.name} is ailing.")

        if for_this_object.health_status == -1:
            print(f"{for_this_object.name} is unconsiocus.")

 
    def tally_item_hp(self):
        # counter
        tally_hp = 0
        # iterate through list of active items
        for this_item in self.active_items:
            # check for "None"
            if this_item.hit_points:
                tally_hp += this_item.hit_points
        return tally_hp

        # get the magnitude
        magnitude = self.hit_points + self.tally_item_hp()


    def get_one_effect(self, target_object_id, effecting_object_id):
        # get plus_minus_neutral: compare the effect-element to your element
        plus_minus_neutral = target_object_id.calculate_effect(effecting_object_id.element, "get")
      
        # get the magnitude of the effect (same as hit_points)
        magnitude = effecting_object_id.hit_points + effecting_object_id.tally_item_hp()

        # effects on target_object_id: health & hitpoints
        target_object_id.set_hit_points( target_object_id.hit_points + (magnitude * plus_minus_neutral) )
        target_object_id.set_health_points( target_object_id.health_points + (magnitude * plus_minus_neutral) )

        # check target_object_id health
        target_object_id.check_health(target_object_id)


    def get_effect(self, effecting_object_id):

        # if swarm:
        # the thing effecting you is a swarm
        # you are affected by everything in swarm 
        # (but not the swarm enchantment / vessel itself)
        if effecting_object_id.flags["swarm"] is True:
            for this_object_id in effecting_object_id.inventory:
                self.get_one_effect(self, this_object_id)

            # auto react  
            if (self.health_status >= 0) and (self.flags["auto_react"] is True):
                # react and GIVE effect
                self.give_effect( effecting_object_id )
                # To DO Add swarm effect option here?

        else:  # not a swarm
            # get an effect for yourself
            self.get_one_effect(self, effecting_object_id)

            # your inventory
            # AND then get effects for all objects riding on you
            for this_item in self.inventory:

                # if it's a list
                if type(this_item) == list:
                    for this_this_item in this_item:
                        self.get_one_effect(self, this_this_item)

                else:  # if just one thing
                  self.get_one_effect(self, this_item)

            # auto react  
            if (self.health_status >= 0) and (self.flags["auto_react"] is True):
                self.give_effect( effecting_object_id )


    # calls the "get-effect" method
    def give_effect(self, target_object_id):
        # first check if actor is unfit:
        # if unfit, don't act
        if self.health_status == -1:
            print(f"{self.name} is unconscious, you cannot affect others.")

        elif type(target_object_id) is list:
            # if a list of (held/riding) objects is put in
            # iterate through list
            for this_object in target_object_id:
                # call on recipient of effect to 'get' effect
                this_object.get_effect(self)

        else:  # just one object entered
            # call on recipient of effect to 'get' effect
            target_object_id.get_effect(self)


    ####################
    # Methods For Rooms
    ####################  
    """
    Using method above
    to create a 2D array 
    """

    def make_a_dungeon_room(self):  # (door_location = (-2, 2), size_of_room = (12, 12), floor_tile = " "):

        # tuple unpacking
        rows, cols = self.size_of_room

        # Make the Room Itself
        the_room = [[self.floor_tile for i in range(cols)] for j in range(rows)] 

        # Add walls & halls

        # Add left hall (column)
        for i in range(2, len(the_room) -1):
            the_room[i][1] = "|"

        # Add right hall (column)
        for i in range(2, len(the_room) -1):
            the_room[i][-2] = "|"

        # Add top hall (row)
        for i in range(1, len(the_room)-1):
            the_room[1][i] = "_"

        # Add bottom hall (row)
        for i in range(2, len(the_room)-2):
            the_room[-2][i] = "_"
        
        # Add a door!
        the_room[self.door_location[0]][self.door_location[1]] = " "

        self.dungeon_room = the_room


    def set_padding(self, padding = "  "):
        self.padding = padding


    def set_size_of_room(self, size_of_room = (12, 12)):
        self.size_of_room = size_of_room


    def set_floor_tile(self, floor_tile = " "):
        self.floor_tile = floor_tile


    def set_door_location(self, door_location = (-2, 2)):
        self.door_location = door_location


    #   ( ) [ ] .  .
    def print_dungeon_room(self):  # (dungeon_room, padding = "  "):

        # make sure objects in room are added:
        for this_character in self.inventory:
            self.add_character_to_map(this_character)

        # iterate through rows and columns
        for row in range(len(self.dungeon_room)):
            # print("\n")
            print_line = ""
            for col in range(len(self.dungeon_room)):
                # print one row at at time
                print_line += str(self.dungeon_room[row][col])
                if col != (len(self.dungeon_room)-1):
                  # add in spacing
                  print_line += self.padding
            print(print_line)
        

    # dungeon_room[row][col] = noun
    def add_something_to_map(self, to_here, add_this):  # (dungeon_room, to_here, add_this):
        self.dungeon_room[to_here[0]][to_here[1]] = add_this


    def add_character_to_map(self, character_id):
        self.add_something_to_map( character_id.micro_location, character_id.avatar  )


    # dungeon_room[row][col] = noun
    def add_some_things(self, list__to_here_add_this):  # (dungeon_room, to_here, add_this):
        for pair in list__to_here_add_this:
            self.dungeon_room[pair[0][0]][pair[0][1]] = pair[1]


    # dungeon_room[row][col] = noun
    def main_characters(self):  # (dungeon_room, to_here, add_this):
        self.add_something_to_map((11,3),"A")
        self.add_something_to_map((11,4),"B")
        self.add_something_to_map((11,5),"C")
        self.add_something_to_map((11,6),"D")
        self.add_something_to_map((11,7),"E")
        self.add_something_to_map((11,8),"F")


    # Modify Room Contents
    def move_something(self, from_here, to_here):  # dungeon_room, from_here, to_here, padding = " "):
        
        # From: 
        # original floor-tile becomes blank
        # first save a copy of the item that is moving
        move_this = self.dungeon_room[from_here[0]][from_here[1]]
        # then clear the tile...
        self.dungeon_room[from_here[0]][from_here[1]] = self.padding

        # To: 
        # item is moved here
        self.dungeon_room[to_here[0]][to_here[1]] = move_this


    #############
    # For Swarms 
    #############

    def add_raw_swarm_enchantment_here(self):
        # create swarm
        Raw_Swarm = DoN_Object( inventory=[],
                                avatar = 'S',
                                name = "Swarmy", 
                                element = 1, 
                                health_points = 10000,
                                root_hit_points = 2, 
                                hit_points = 2, 
                                micro_location = (5,6),  # micro_location_in_room_or_riding_on
                                macro_location = self,  # macro_location_which_dungeon_room_or_riding_on
                               )
        # add to inventory of room
        self.add_to_enchantment_list(Raw_Swarm)
        # ??? add to enchantments of room
        self.add_to_swarm_list(Raw_Swarm)
        # ??? add to enchantments of room
        self.add_to_inventory(Raw_Swarm)


    def add_raw_swarm_enchantment(self, add_to_this_room):
        # create swarm
        Raw_Swarm = DoN_Object( inventory = [],
                                avatar = 'S',
                                name = "Swarmy", 
                                element = 1, 
                                health_points = 10000,
                                root_hit_points = 2, 
                                hit_points = 2, 
                                micro_location = (5,6),  # micro_location_in_room_or_riding_on
                                macro_location = add_to_this_room,  # macro_location_which_dungeon_room_or_riding_on
                               )
        # add to inventory of room
        self.add_to_inventory.enchantment_list(Raw_Swarm)
        # ??? add to enchantments of room
        add_to_this_room.enchantment_list(Raw_Swarm)
    

    def set_auto_react(self, True_or_False):
        self.flags["auto_react"] == True_or_False


    # def add_swarm_to_room(self, this_room):
    #     pass


    # add one population to swarm
    def populate_swarm(self, swarm_located_here, population_size, health, hp, which_element):
        # # inspection
        # print("populating...\npopulation size = ", population_size, "element = ", which_element)

        for i in range(0, population_size):
            this_object = DoN_Object(inventory=[], health_points=health, hit_points=hp, element=which_element)
            
            # self.inventory.append(i)
            
            # set the location of the swarm item
            # self.set_as_object_location(swarm_located_here, this_object)
            swarm_located_here.inventory.append(this_object)

    # make a randomly populated swarm
    # large chance of just one elemnet?
    def make_a_random_swarm(self, swarm_located_here = None, max_number_of_elements = 6):
        import random

        if not swarm_located_here:
            swarm_located_here = self

        # lists of options for activity creation
        population_size_list = [3,10,42,50,100,300,1000]
        which_element_list = [1,2,3,4,5]
        number_of_elements_list = [1,1,1,1,1,1,1,1,1,2,2,2,3,3,4,4,5]
        health_list = [1,1,1,2,2]
        hp_list = [1,1,1,2,2]

        random.choice(number_of_elements_list)

        # number_of_elements
        # number_of_elements = random.randrange(1,max_number_of_elements)
        number_of_elements_in_swarm = random.choice(number_of_elements_list)

        # pick number between 1 and 5
        #which_element = random.randrange(1,6)
        which_element = random.choice(which_element_list)

        # pick a number between 1 and 1000, multiples (stepsize) of 100
        # population_size = random.randrange(1,1000,100)
        population_size = random.choice(population_size_list)

        # pick number 1 or 2
        # healh = random.randrange(1,3)
        health = random.choice(number_of_elements_list)

        # pick number 1 or 2
        hp = random.choice(hp_list)

        # take the settings generated above and put them int0
        # the 'populate' function (method)
        for i in range(number_of_elements_in_swarm):
            #    populate_swarm(self, swarm_located_here, population_size, health, hp, which_element)
            # self.populate_swarm( swarm_located_here, population_size, health, hp, which_element )
            self.populate_swarm( swarm_located_here, 
                                random.choice(population_size_list),
                                health,
                                random.choice(hp_list), 
                                random.choice(which_element_list) 
                                )


            # # inspection
            # print("\nnumber_of_elements_in_swarm", number_of_elements_in_swarm)
            # print("which_element", which_element)
            # print("population_size", population_size)            
            # print("health", health)            
            # print("hp", hp)            


    def make_a_swarm_in_each_dungeon_level_room(self):
        for i in range(0, len(self.room_dictionary)):
            # call room link function(medthod)
            self.room_dictionary[i].make_a_random_swarm()


    #############
    # Characters
    #############

    def make_main_characters(self, choice_of_element=1):

        character_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':choice_of_element}
        
        # iterate through characters list and make characters
        for key, value in character_dict.items():

            # inspection
            print(key, value)

            # creaate object
            this_character = DoN_Object( avatar=key, element=value, inventory=[], blurb="Character" )
            
            # put object in character_and_item_dictionary
            self.character_and_item_dictionary[key] = this_character


    ##################
    # Treasure Chests
    ##################


    def make_chests(self):
        # note: self.print_dungeon_map() will print this
        
        # for key, value in self.room_dictionary.items():
        for this_room_number, this_room_object in self.room_dictionary.items():

            # reset
            this_chest = None
            
            # create object
            this_chest = DoN_Object( avatar="@", inventory=[], blurb="chest", micro_location=(2,9))

            # add to inventory
            this_room_object.inventory.append(this_chest)

            # to do: add randomize location? (pick and check spot empty?)
            # # add location in room
            # this_room_object.micro_location = (2,9)

            # put chest object in character_and_item_dictionary
            this_room_object.character_and_item_dictionary["treasure_chest"] = this_chest




    ################
    # Action & REPL
    ################




    ##########################
    # End of Class DoN_Object
    ##########################

    '''
    ToDo:

    for swarm: inventory vs. active inventory?

    Fractional health stats?
    set to float?

    term: "inventory" for 'has_items"?

    make a swarm effect method?

    '''
