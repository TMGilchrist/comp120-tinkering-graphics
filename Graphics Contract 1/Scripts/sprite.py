import pygame


class Sprite:

    # The image used for the sprite
    image = 0

    def __init__(self, size, base, legs, body, head, feet, weapon):

        """
        Constructor for sprite class.

        Args:
            size (tuple): The size of the sprite in pixels.
            base (image): The image to use for the sprite base.
            legs (image): The image to use for the sprite's legs.
            body (image): The image to use for the sprite's body.
            head (image): The image to use for the sprite's head.
            feet (image): The image to use for the sprite's feet.
            weapon (image): The image to use for the sprite's weapon.
        """

        self.size = size
        self.base = base
        self.legs = legs
        self.body = body
        self.head = head
        self.feet = feet
        self.weapon = weapon

    def draw(self):

        """Draws the sprite's component images onto a PyGame surface and assigns it to the image property."""

        sprite_base = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        sprite_base.set_alpha(255)

        sprite_base.blit(self.base, (0, 0))
        sprite_base.blit(self.legs, (0, 0))
        sprite_base.blit(self.body, (0, 0))
        sprite_base.blit(self.head, (0, 0))
        sprite_base.blit(self.feet, (0, 0))

        # Save sprite
        self.image = sprite_base

    def draw_with_position(self, base_pos, body_pos, legs_pos, head_pos):

        """
        Draws the sprite's component images onto a PyGame surface at
        specified positions and assigns the surface to the image property.

        Args:
            base_pos (tuple): Position of the base image.
            body_pos (tuple): Position of the body image.
            legs_pos (tuple): Position of the legs image.
            head_pos (tuple): Position of the head image.

        """

        sprite_base = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        sprite_base.set_alpha(255)

        sprite_base.blit(self.base, base_pos)
        sprite_base.blit(self.legs, legs_pos)
        sprite_base.blit(self.body, body_pos)
        sprite_base.blit(self.head, head_pos)
        sprite_base.blit(self.feet, (0, 0))

        # Save sprite
        self.image = sprite_base

    def update(self, to_update, new_values):

        """
        Updates the sprite image.

        Args:
            to_update (list of strings): The components to change, referencing the sprite properties.
            new_values (list of images): The new images for the components being changed .

        """

        for i in range (0, len(to_update)):
            setattr(self, to_update[i], new_values[i])

        self.draw()

    def save_with_id(self, save_path, file_type):

        """
        Saves the sprite image to file with a unique name and
        records the name used in a text document.

        Args:
              save_path (string): The file path in which to save the image.
              file_type (string): The file extension to use when saving the image.

        """

        sprite_id = 0

        with open("spriteNames.txt", "a+") as f:
            for line in f:
                sprite_id += 1

            f.write("sprite" + str(sprite_id) + "\n")
            f.close()

        pygame.image.save(self.image, save_path + "/sprite" + str(sprite_id) + "." + file_type)
