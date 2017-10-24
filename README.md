# comp120-tinkering-graphics
Python Code for Re-purposing Graphics Algorithms

### Important: assets.7z must be uncompressed before the program can run!
### Important: path_to_assets in main.py must point to the assets folder at runtime. By default, this points to the folder above the Scripts Folder. When running on a new computer, please ensure the file structure is maintained or this variable is set corretly to avoid errors.

## Overview

When provided with appropriate images, this python program will generate and save a sprite using randomly selected images from several catagories, incuding: head, body, legs and feet. 

For this project, images have been provided in the assets folder. If different images are used, ensure the sprite_file_type has been set correctly in main.py.

## Dependencies

The pygame, glob and random libraries must be available for the program to import.

## Files

### main.py

Starting point of program. Collects lists of images to use when generating a sprite and instantiates an instance of the Sprite class.

### Sprite.py

Sprite class which contains methods for drawing, updating and saving the sprite image.

## TODO

* Finish docstring commenting
* Add explanation in readme.txt explaining how to use and the reason why a gui is not provided
* Merge with master
* Upload to learning space as zip file
