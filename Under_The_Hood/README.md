# What is happening under the hood in Dungeon of Notebooks?

- simplicity (few extra packages and libraries)
- open transparency
- easy to modify


# Basic Design: Objects and Resonance

Every 'object' in the world of Dungeon of Notebooks (DoN) a similar kind of object. This elusively simple statement, oddly, applies to both the story-level colloquial term 'object' (or whatever synonym) referring to inventory items such as hammers, bags, shields, shirts, and socks, and to living creatures in rooms which are also objects in rooms, and to player-characters who are also objects in rooms, and this applies to rooms which are objects in the larger dungeon. All of these 'objects' (so-called in non-technical language) are also "objects" in the technical language of object oriented programming: all objects are instances of the class "DoN_Object." 

Another way of looking at this from a story angle is that everything in this magical world is an enchantment with the same basic properties (or "attributes" in technical computer-speak):
- it has a basic element of its own (fire, water, ice, etc.)
- it follows the same rules for interacting with other elemental-enchantments.
- it is somewhere, and can move somewhere else (in a room, in a backpack, etc.)
- it can have another item located in it (in a room, in a backpack, etc.)
etc.



# Stories & Abstractions: On the Level of the Story

The basic aim is that the use of the tools and the designs of the python functions (mostly "class methods") should operate on the level story. That was probably a dense sentence so I will take some time to unpack it because it may be important for understanding how the code works. What I mean by "on the level of the story," is that if a character is moving from one place to another, or if a character is casting a  spell or enchantment, the use of the function (or method) should operate on that "level" of terms an objects and actions. 

For example someone might say, "well, a so-called-character is not really a character, it is just a computer object, and the character is not really moving it is just changing numbers in the program, so, therefore, there's no point in having a function to just pretend to move a merely pretend so-called-character." The view taken here is that that statement in quotes reflects an extreme perspective which would make both this project and coding best practice more difficult. 


Two examples: 
1. In theory, for some people it may be more 'pure' to just change the numbers that reflect a character moving rather than create a method (a function) which is easy to understand in plain language. The priority here is communication and understanding.

2. The concept of 'refactoring your code' is often (mis)used to mean 'optimizing' or 'debugging,' but originally 'refactoring' meant (and still often means) making the code easier to understand, read, and use. 




# Curious Worlds: Instrumentalist Implications of Resonance-Objects

An interesting side effect of this elemental-enchantment-object structure is that the world is kind of fractal-world. 

For example, let's start out with a basic common-sense character-perspective of 'levels' or 'scales' of a given world. 

The largest scale we currently have here is a village, a town.
The village contains a dungeon. 
The dungeon contains levels.
The dungeon-levels contain rooms.
The rooms contain chests.
The chests have items in them.
The items have enchantments. 

This gets interesting when we see that every object in the game-world is an elemental-enchantment-object with all the same basic properties of every other object, meaning that scale is relative not absolute. Every enchantment-object can play a role on any of these scales. For example, if you go into a room and find a cucumber on a table, you can go into that cucumber. That cucumber can contain: a village, a dungeon, levels, rooms, tables, and more cucumbers. 
