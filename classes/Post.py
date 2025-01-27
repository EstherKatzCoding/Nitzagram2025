import pygame
from constants import *
from helpers import *
from Comment import *

class Post:
    """
    A class used to represent a post on Nitzagram
    """
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.comments_display_index = 0

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        new_comment_text = read_comment_from_user()
        if new_comment_text.strip():  # Only add non-empty comments
            try:
                new_comment = Comment(new_comment_text)
                self.comments.append(new_comment)
            except ValueError as e:
                print(str(e))

    def display(self):
        # Initialize screen
        screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        screen = pygame.display.set_mode(screen_size)
        screen.fill(WHITE)  # Clear screen

        # Username
        username_font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        username_text = username_font.render(self.username, True, BLACK)
        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))

        # Location
        location_font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        location_text = location_font.render(self.location, True, BLACK)
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # Number of likes
        likes_font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        likes_text = likes_font.render(f"{self.likes_counter} likes", True, BLACK)
        screen.blit(likes_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        # Description
        description_font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        description_text = description_font.render(self.description, True, BLACK)
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        # Display comments
        self.display_comments(screen)

        # Update the display
        pygame.display.update()

    def display_comments(self, screen):
        """
        Display comments on the post. If there are more than 4 comments,
        show only 4 comments starting from `comments_display_index`.

        :param screen: Pygame screen to render the comments.
        """
        # Check if there are more comments than the display limit
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont("Arial", COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("View more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display up to NUM_OF_COMMENTS_TO_DISPLAY comments
        position_index = self.comments_display_index
        for i in range(NUM_OF_COMMENTS_TO_DISPLAY):
            if position_index >= len(self.comments):
                position_index = 0  # Wrap around to the start of the comments
            comment_text = self.comments[position_index]
            comment_font = pygame.font.SysFont("Arial", COMMENT_TEXT_SIZE)
            rendered_comment = comment_font.render(comment_text, True, BLACK)
            screen.blit(rendered_comment, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + i * COMMENT_LINE_HEIGHT))
            position_index += 1
