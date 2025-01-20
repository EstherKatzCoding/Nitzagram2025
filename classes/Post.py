import pygame
from constants import *


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description, likes_counter, comments):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []


    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        self.comments.append(text)

    def display(self):
        screen_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        screen = pygame.display.set_mode(screen_size)

        # username
        username_font = pygame.font.SysFont("Ariel", UI_FONT_SIZE)
        username_text = username_font.render(self.username, True,BLACK)
        screen.blit(username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))

        # location
        location_font = pygame.font.SysFont("Ariel", UI_FONT_SIZE)
        location_text = location_font.render(self.location, True, BLACK)
        screen.blit(location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))

        # number of likes
        likes_font = pygame.font.SysFont("Ariel", UI_FONT_SIZE)
        likes_text = likes_font.render(self.likes_counter, True, BLACK)
        screen.blit(likes_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))

        # description
        description_font = pygame.font.SysFont("Ariel", UI_FONT_SIZE)
        description_text = description_font.render(self.description, True, BLACK)
        screen.blit(description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

        # comments
        for i, comment in enumerate(self.comments[:6]):  # displays up to 6 comments
            comment_font = pygame.font.SysFont("Ariel", UI_FONT_SIZE)
            comment_text = comment_font.render(comment, True, BLACK)
            comment_y = FIRST_COMMENT_Y_POS + i * COMMENT_LINE_HEIGHT
            screen.blit(comment_text, (FIRST_COMMENT_X_POS, comment_y))


def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



