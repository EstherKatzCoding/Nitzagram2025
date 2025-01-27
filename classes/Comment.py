import pygame
from constants import *

class Comment:


    def __init__(self, text):
        """
        Initialize a comment with the given text.
        :param text: str, the content of the comment
        """
        if not all(char.isascii() for char in text):  # Ensure only English characters
            raise ValueError("Comments can only contain English characters.")
        self.text = text

    def display(self, index):
        """
        Display the comment on the screen.
        The position depends on the index in the post's comments list.
        :param index: int, the index of the comment in the list
        :return: None
        """
        # Calculate the Y position based on the index
        comment_y_pos = FIRST_COMMENT_Y_POS + index * COMMENT_LINE_HEIGHT
        font = pygame.font.SysFont("Ariel", COMMENT_TEXT_SIZE)
        text_surface = font.render(self.text, True, BLACK)

        # Display the comment
        screen.blit(text_surface, (FIRST_COMMENT_X_POS, comment_y_pos))
