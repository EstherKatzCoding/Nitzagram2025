import pygame
from helpers import screen, mouse_in_button, read_comment_from_user
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from buttons import *

def main():
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Create a post
    post = Post(username="john_doe", location="New York, USA", description="Lovely day!", likes_counter=42, comments=[])

    # Define buttons
    like_button = Button(50, 500, 100, 50)  # מיקום וגודל לדוגמה
    comment_button = Button(200, 500, 100, 50)  # מיקום וגודל לדוגמה
    next_post_button = Button(350, 500, 100, 50)  # מיקום וגודל לדוגמה

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Like button clicked
                if mouse_in_button(like_button, mouse_pos):
                    post.add_like()
                    print(f"Post liked! Total likes: {post.likes_counter}")

                # Comment button clicked
                if mouse_in_button(comment_button, mouse_pos):
                    new_comment = read_comment_from_user()
                    if new_comment.strip():
                        post.add_comment(new_comment)
                        print(f"New comment added: {new_comment}")

                # Next post button clicked
                if mouse_in_button(next_post_button, mouse_pos):
                    print("Switching to the next post...")
                    # Add logic to switch posts here if needed

        # Draw the screen
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Draw the post and buttons
        post.display()

        # Draw buttons
        pygame.draw.rect(screen, (200, 0, 0),
                         (like_button.x_pos, like_button.y_pos, like_button.width, like_button.height))  # Like button
        pygame.draw.rect(screen, (0, 200, 0), (
        comment_button.x_pos, comment_button.y_pos, comment_button.width, comment_button.height))  # Comment button
        pygame.draw.rect(screen, (0, 0, 200), (next_post_button.x_pos, next_post_button.y_pos, next_post_button.width,
                                               next_post_button.height))  # Next post button

        # Update the display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


main()
