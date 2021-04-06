# What is happening under the hood in Dungeon of Notebooks?

- simplicity (few extra packages and libraries)
- open transparency
- easy to modify


# Basic Design: Objects and Resonance

Every 'object' in the Dungeon of Notebooks (DoN) world is a similar kind of object. This, oddly, applies to both the story-level colloquial term 'object' (or whatever synonym) referring to inventory items such as hammers, bags, shields, shirts, and socks. And living creatures in rooms are also objects in rooms. And player-characters are also objects in rooms. And rooms are also objects in the larger dungeon. All of these 'objects' (in non-technical language) are also "objects" in the technical language of object oriented programming: all objects are instances of the class "DoN_Object." 



# Stories & Abstractions: On the Level of the Story

The basic aim is that the use of the tools and the designs of the python functions (mostly class methods) should operate on the level story. If a character is moving from one place to another, or if a character is casting a  spell or enchantment, the use of the function (or method) should operate on that level.

For example you might say, "well, it's not really a character, and they aren't really moving, so there's no point in having a function to pretend to move a pretend character." My view, just one vote, is that this statement in quotes reflects an extremism perspective which undermines not only a given project but best-practice in coding itself. For example, 'refactoring' while often used to mean 'optimizing' or 'debugging' originally meant and still often means: making the code easier to understand, read, and use. 




# Curious Worlds: Instrumentalist Implications of Resonance

