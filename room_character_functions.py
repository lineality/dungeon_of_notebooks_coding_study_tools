class Character_Object:

    # constructor
    def __init__(self, 
                 status = 1,
                 avatar = 'x',
                 name = "No_Name", 
                 element = 1, 
                 health_points = 10, 
                 hit_points = 2, 
                 micro_location_in_room_or_riding_on = (11,9),
                 macro_location_which_room_or_riding_on = None,
                 has_objects_list = [],
                 ):
      
        ############
        # attributes
        ############
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

        self.avatar = avatar  # single character str
        self.status = status  # 1 = healthy, 0 = ailing, -1 = unconcious
        self.name = name
        self.element = element_lookup[element]  # (1,2,3,4,5)
        self.health_points = health_points  # (int)
        self.hit_points = hit_points  # (int)

        # Contains and Contains-by (other objects)
        self.micro_location_in_room_or_riding_on = micro_location_in_room_or_riding_on  # object.location / (1,2)
        self.macro_location_which_room_or_riding_on = macro_location_which_room_or_riding_on  # object.location (1,2,0,0,0) (room x, room y, level-floor, which-building, etc.)
        self.micro_location = self.micro_location_in_room_or_riding_on
        self.macro_location = self.macro_location_which_room_or_riding_on
        self.has_objects_list = has_objects_list  # list
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
        # for rooms
        # self.effected = specific mode for method, e.g. reflect?

    #########
    # Methods
    #########


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

    def set_micro_location(self, micro_location_in_room_or_riding_on):
        self.micro_location_in_room_or_riding_on = micro_location_in_room_or_riding_on

    def set_macro_location(self, macro_location_which_room_or_riding_on):
        self.macro_location_which_room_or_riding_on = macro_location_which_room_or_riding_on

    def set_has_objects_list(self, has_objects_list):
        self.has_objects_list = has_objects_list

    def add_to_has_objects_list(self, new_object):
        self.has_objects_list.append(new_object)


    ##########
    # Effects
    ##########

    # The basic modality(?) is that if the other element is + effects_you
    # your health and hitpoints get boosted
    # 
    # if the other element is - effects_you
    # 
    # 1. water
    # 2. forest
    # 3. fire
    # 4. void
    # 5. ice
    # 

  

    def calculate_effect(self, other_element, give_or_get):
        if give_or_get == "get":
            return self.effect_dictionary[(self.elment, other_element)]
        elif give_or_get == "give":
            return self.effect_dictionary[(other_element, self.element)]
        else:
            print(f"input error: calculate_effect: {give_or_get}")


    def get_effect(self, object_id):
        # get plus_minus_neutral
        plus_minus_neutral = self.calculate_effect(object_id.element, "get")
        # get the magnitude
        magnitude = object_id.hit_points
        # effects
        self.set_hit_points(self.hit_points + (magnitude * plus_minus_neutral) )
        self.set_health_points(self.health_points + (magnitude * plus_minus_neutral) )

        if self.status == 0:
            print(f"{self.name} is ailing.")

        if self.status == -1:
            print(f"{self.name} is unconsiocus.")


    def give_effect(self, object_id):
        # if a list of (held/riding) objects is put in
        if type(object_id) is list:
            for this_object in object_id:
                # get plus_minus_neutral
                plus_minus_neutral = self.calculate_effect(this_object.element, "give")
                # get the magnitude
                magnitude = self.hit_points
                if self.status == -1:
                    print(f"{self.name} is unconscious, you cannot affect others.")
                else:
                    this_object.set_hit_points( this_object.hit_points + (magnitude * plus_minus_neutral) )
                    this_object.set_health_points( this_object.health_points + (magnitude * plus_minus_neutral) )
        # effects
        elif self.status == -1:
            print(f"{self.name} is unconscious, you cannot affect others.")

        else:  # just one object entered
            # get plus_minus_neutral
            plus_minus_neutral = self.calculate_effect(object_id.element, "give")
            # get the magnitude
            magnitude = self.hit_points
            # cause and effect: make changes resulting from effect
            object_id.set_hit_points( object_id.hit_points + (magnitude * plus_minus_neutral) )
            object_id.set_health_points( object_id.health_points + (magnitude * plus_minus_neutral) )


    def set_location(self, room_id):
        room_id.has_objects_list.append(self)
  

#########
# Room !!
#########

class Room_Object:

    # constructor
    def __init__(self, 
                 avatar = 'x',
                 name = 'NoName_Room', 
                 element = 2, 
                 health_points = 100, 
                 hit_points = 100, 
                 micro_location_in_room_or_riding_on = None, 
                 macro_location_which_room_or_riding_on = None, 
                 has_objects_list = [],
                 door_location = (-2, 2),
                 size_of_room = (12, 12),
                 floor_tile = " ",
                 padding = "  ", 
                 dungeon_room = [],
                 ):
      
        ############
        # attributes
        ############
        self.avatar = avatar  # single character str
        self.name = name  # 
        self.element = element  # (1,2,3,4,5)
        self.health_points = health_points  # (int)
        self.hit_points = hit_points  # (int)

        # Contains and Contains-by (other objects)
        self.micro_location_in_room_or_riding_on = micro_location_in_room_or_riding_on  # object.location / (1,2)
        self.macro_location_which_room_or_riding_on = macro_location_which_room_or_riding_on  # object.location (1,2,0,0,0) (room x, room y, level-floor, which-building, etc.)
        self.has_objects_list = has_objects_list  # list

        # for rooms
        self.door_location = door_location
        self.size_of_room = size_of_room
        self.floor_tile = floor_tile
        self.padding = padding  # for printing
        self.dungeon_room = dungeon_room
        # self.effected = specific mode for method, e.g. reflect?

    #########
    # Methods
    #########

    ##############
    # Set & Add To
    ##############

    def set_avatar(self, avatar):
        self.avatar = avatar

    def set_name(self, name):
        self.name = name

    def set_health_points(self, health_points):
        self.health_points = health_points

    def set_hit_points(self, hit_points):
        self.hit_points = hit_points

    def set_micro_location(self, micro_location_in_room_or_riding_on):
        self.micro_location_in_room_or_riding_on = micro_location_in_room_or_riding_on

    def set_macro_location(self, macro_location_which_room_or_riding_on):
        self.macro_location_which_room_or_riding_on = macro_location_which_room_or_riding_on

    def set_has_objects_list(self, has_objects_list):
        self.has_objects_list = has_objects_list

    def add_to_has_objects_list(self, new_object):
        self.has_objects_list.append(new_object)



    # Using above second method to create a  
    # 2D array 
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
        for this_character in self.has_objects_list:
            self.add_character(this_character)

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
    def add_something(self, to_here, add_this):  # (dungeon_room, to_here, add_this):
        self.dungeon_room[to_here[0]][to_here[1]] = add_this

    def add_character(self, character_id):
        self.add_something( character_id.micro_location_in_room_or_riding_on, character_id.avatar  )

    # dungeon_room[row][col] = noun
    def add_some_things(self, list__to_here_add_this):  # (dungeon_room, to_here, add_this):
        for pair in list__to_here_add_this:
            self.dungeon_room[pair[0][0]][pair[0][1]] = pair[1]

    # dungeon_room[row][col] = noun
    def main_characters(self):  # (dungeon_room, to_here, add_this):
        self.add_something((11,3),"A")
        self.add_something((11,4),"B")
        self.add_something((11,5),"C")
        self.add_something((11,6),"D")
        self.add_something((11,7),"E")
        self.add_something((11,8),"F")

    # Modify Room Contents
    def move_something(self):  # dungeon_room, from_here, to_here, padding = " "):
        
        # From: 
        # original floor-tile becomes blank
        # first save a copy of the item that is moving
        move_this = self.dungeon_room[from_here[0]][from_here[1]]
        # then clear the tile...
        self.dungeon_room[from_here[0]][from_here[1]] = self.padding

        # To: 
        # item is moved here
        self.dungeon_room[to_here[0]][to_here[1]] = move_this



    ##########
    # Effects
    ##########

    # The basic modality(?) is that if the other element is + effects_you
    # your health and hitpoints get boosted
    # 
    # if the other element is - effects_you
    # 
    # 1. water
    # 2. forest
    # 3. fire
    # 4. void
    # 5. ice
    # 

  

    def calculate_effect(self, other_element, give_or_get):
        if give_or_get == "get":
            return self.effect_dictionary[(self.elment, other_element)]
        elif give_or_get == "give":
            return self.effect_dictionary[(other_element, self.element)]
        else:
            print(f"input error: calculate_effect: {give_or_get}")


    def get_effect(self, object_id):
        # get plus_minus_neutral
        plus_minus_neutral = self.calculate_effect(object_id.element, "get")
        # get the magnitude
        magnitude = object_id.hit_points
        # effects
        self.set_hit_points(self.hit_points + (magnitude * plus_minus_neutral) )
        self.set_health_points(self.health_points + (magnitude * plus_minus_neutral) )

        if self.status == 0:
            print(f"{self.name} is ailing.")

        if self.status == -1:
            print(f"{self.name} is unconsiocus.")


    def give_effect(self, object_id):
        # if a list of (held/riding) objects is put in
        if type(object_id) is list:
            for this_object in object_id:
                # get plus_minus_neutral
                plus_minus_neutral = self.calculate_effect(this_object.element, "give")
                # get the magnitude
                magnitude = self.hit_points
                if self.status == -1:
                    print(f"{self.name} is unconscious, you cannot affect others.")
                else:
                    this_object.set_hit_points( this_object.hit_points + (magnitude * plus_minus_neutral) )
                    this_object.set_health_points( this_object.health_points + (magnitude * plus_minus_neutral) )
        # effects
        elif self.status == -1:
            print(f"{self.name} is unconscious, you cannot affect others.")

        else:  # just one object entered
            # get plus_minus_neutral
            plus_minus_neutral = self.calculate_effect(object_id.element, "give")
            # get the magnitude
            magnitude = self.hit_points
            # cause and effect: make changes resulting from effect
            object_id.set_hit_points( object_id.hit_points + (magnitude * plus_minus_neutral) )
            object_id.set_health_points( object_id.health_points + (magnitude * plus_minus_neutral) )


