
import pygame
import math
import serial

arduino = serial.Serial("COM7", 9600)
clock = pygame.time.Clock()
pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arduino Radar")

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

SCALE = 6
angle = 45
points = {}

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # read from arduino

    if arduino.in_waiting:
        line = arduino.readline().decode().strip()

        try:
            angle, distance = map(int, line.split(","))
        except ValueError:
            continue

        angle_rad = math.radians(angle)

        x = math.cos(angle_rad) * distance * SCALE
        y = math.sin(angle_rad) * distance * SCALE

        points[angle] = (x, y)

        points[angle] = (x, y)

    # screen
    screen.fill(BLACK)

    angle_rad = math.radians(angle)

    end_x = CENTER_X + 300 * math.cos(angle_rad)
    end_y = CENTER_Y - 300 * math.sin(angle_rad)


    pygame.draw.circle(screen, GREEN, (CENTER_X, CENTER_Y), 5)

    #  rings
    pygame.draw.circle(screen, GREEN, (CENTER_X, CENTER_Y), 100, 1)
    pygame.draw.circle(screen, GREEN, (CENTER_X, CENTER_Y), 200, 1)
    pygame.draw.circle(screen, GREEN, (CENTER_X, CENTER_Y), 300, 1)

    # crosshair
    pygame.draw.line(screen, GREEN, (0, CENTER_Y), (WIDTH, CENTER_Y), 1)
    pygame.draw.line(screen, GREEN, (CENTER_X, 0), (CENTER_X, HEIGHT), 1)
    pygame.draw.line(screen, GREEN, (CENTER_X,CENTER_Y), (end_x,end_y), 5)

    # points
    for x, y in points.values():pygame.draw.circle(screen,GREEN,(CENTER_X + x, CENTER_Y - y),4)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
