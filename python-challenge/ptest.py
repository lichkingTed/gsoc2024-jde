import imageio as imageio
import pygame
import random
import numpy as np
import os

pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Brownian Motion Simulation")
clock = pygame.time.Clock()
running = True

# Robot settings
x, y = width // 2, height // 2
direction = random.uniform(0, 2 * np.pi)
speed = 5
color = (255, 255, 255)  # White

frame_directory = "frames"
os.makedirs(frame_directory, exist_ok=True)
frame_count = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += speed * np.cos(direction)
    y += speed * np.sin(direction)

    # Boundary detection and change direction
    if x <= 0 or x >= width or y <= 0 or y >= height:
        direction = random.uniform(0, 2 * np.pi)

    x = max(0, min(x, width))
    y = max(0, min(y, height))


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (int(x), int(y)), 10)

    pygame.display.flip()

    pygame.image.save(screen, f"{frame_directory}/frame_{frame_count}.png")
    frame_count += 1

    clock.tick(120)

pygame.quit()


print("Generating GIF...")
frames = []
for i in range(frame_count):
    frame_path = f"{frame_directory}/frame_{i}.png"
    frames.append(imageio.imread(frame_path))
imageio.mimsave('simulation.gif', frames, duration=1000 / 120)
