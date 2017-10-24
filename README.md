# comp120-tinkering-graphics
Python Code for Re-purposing Graphics Algorithms

### Important: If downloading from github, assets.7z must be uncompressed before the program can run!
### Important: path_to_assets in main.py must point to the assets folder at runtime. By default, this points to the folder above the Scripts Folder.
			   When running on a new computer, please ensure the file structure is maintained or this variable is set corretly to avoid errors.

## Overview

This is a utility program designed to be used in a game that implements random unit generation. When provided with appropriate images, the program will generate
and save a sprite using randomly selected images from several catagories, incuding: head, body, legs and feet. The program can be easily expanded to accomodate additional
catagories such as weapons, with minimal changes to the code. The images used to create the random sprites could also be easily seperated into more precise catagories,
for example, long and short hair, to allow for more control over the sprites generated.

For this project, images have been provided in the assets folder. If different images are used, ensure the sprite_file_type has been set correctly in main.py.

Newly created sprites are saved in Assets/Sprites/CustomSprites with default names of sprite0, sprite1 etc. A text file will be created in the scripts folder to record the
names in use. To reset the autonaming to 0, delete the spriteNames.txt file.

To run the program, simply run main.py. The new image will appear in the save location and the program will exit.

### Please Note:

As a utility tool designed to be run during the generation of a game world, or used as a tool for developers to quickly make custom sprites, no gui is provided.
Instead, the new sprites are saved directly to file where they can be used in the game.

## Dependencies

The pygame, glob and random libraries must be available for the program to import.

## Files

### main.py

Starting point of program. Contains the file path and file type of the images to be used. Instantiates GetImages and Sprite classes.

### get_images.py

GetImages class which contains several functions to easily load a large number of images into seperate lists for later use.

### Sprite.py

Sprite class which contains methods for drawing, updating and saving the sprite image.

## TODO

* Finish docstring commenting
* Add explanation in readme.txt explaining how to use and the reason why a gui is not provided
* Combine readme.txt and readme.md!
* Merge with master
* Upload to learning space as zip file
