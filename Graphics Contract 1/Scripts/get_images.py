import pygame
import glob


class GetImages:

    base = []
    legs = []
    body = []
    hair = []
    feet = []

    def __init__(self, path_to_assets, sprite_file_type):

        """
        Constructor for GetImages class.

        Args:
            path_to_assets (string): The file path pointing to the assets folder.
            sprite_file_type (string): The file extension to find
        """

        self.path_to_assets = path_to_assets
        self.sprite_file_type = sprite_file_type

        self.load_all()

    def load_all(self):
        self.load_components("base")
        self.load_components("legs")
        self.load_components("body")
        self.load_components("hair")
        self.load_components("feet")

    def load_components(self, component):
        path = glob.glob(self.path_to_assets + "/Sprites/" + component + "/*" + self.sprite_file_type)

        # Component names NEED to be standardised. i.e. sprite folders should be named the same as lists

        for filename in path:
            print("Getting components for " + component)
            getattr(self, component).append(pygame.image.load(filename))