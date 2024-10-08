import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Reaction Time Test")

# Load sound
sound = pygame.mixer.Sound('peep.wav')  # Replace 'beep.wav' with your sound file

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 55)

def display_message(message):
    screen.fill(white)
    text = font.render(message, True, black)
    screen.blit(text, (width // 4, height // 2))
    pygame.display.update()

def reaction_time_test():
    running = True
    display_message("Press space to start")
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    display_message("Wait for the sound...")
                    pygame.display.update()
                    time.sleep(random.uniform(2, 5))  # Random delay between 2 and 5 seconds

                    sound.play()  # Play the sound
                    start_time = time.time()

                    waiting_for_reaction = True
                    while waiting_for_reaction:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    reaction_time = (time.time() - start_time) * 1000  # Reaction time in ms
                                    display_message(f"Reaction Time: {int(reaction_time)} ms")
                                    pygame.display.update()
                                    time.sleep(2)
                                    waiting_for_reaction = False
                                    display_message("Press space to start again")

    pygame.quit()

if __name__ == "__main__":
    reaction_time_test()
