<<<<<<< HEAD
import pygame
#pygame, sys, matplotlib
import sys
import matplotlib.pyplot as plt
#initialize pygame
pygame.init()
sprite_image = pygame.image.load('file.png')

    


=======
import csv
>>>>>>> b71680bfc49b0aadd49e6a0802e0b5ca627f5cf7

sensor_Manifest = 'sensor.csv'

<<<<<<< HEAD
# Set up the colors
GREEN = (34, 139, 34)
GREY = (169, 169, 169)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLACK1 = '#0d0d0d'
slow = 2
medium = 4
fast = 6

# Set up the car object
car_width = 50
car_height = 80
car_rect = sprite_image.get_rect(center=(screen_width//2, screen_height//2))


# Set up the movement controls
car_speed = slow
def change_speed(speed):
    global car_speed
    car_speed = speed
 
slow_button = pygame.Rect(50, 50, 100, 50)
medium_button = pygame.Rect(50, 125, 100, 50)
fast_button = pygame.Rect(50, 50, 50, 50)

  
# pygame.Rect(50,50,100,100)
# pygame.Rect(30,30,30,30)
# pygame.Rect(66,66,66,66)
font = pygame.font.Font(None, 30)
slow_text = font.render("Slow", True, WHITE)
medium_text = font.render("Medium", True, WHITE)
fast_text = font.render("Fast", True, WHITE)
screen.blit(slow_text, (60, 55))
screen.blit(medium_text, (60, 130))
screen.blit(fast_text, (60, 205)) 
move_left = False
move_right = False
move_up = False
move_down = False
# Set up the road path
road_path = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_s:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_s:
                move_down = False
            

    mouse_pos = pygame.mouse.get_pos()
    if slow_button.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            change_speed(slow)
    elif medium_button.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            change_speed(medium)
    elif fast_button.collidepoint(mouse_pos):
        if event.type == pygame.MOUSEBUTTONUP:
            change_speed(fast)
    
    # Move the car
    if move_left:
        car_rect.x -= car_speed
    elif move_right:
        car_rect.x += car_speed
    if move_up:
        car_rect.y -= car_speed
    elif move_down:
        car_rect.y += car_speed
    # Update the road path
    prev_position = (car_rect.x + car_width/2, car_rect.y + car_height/2)
    road_path.append(prev_position)
    current_position = (car_rect.x + car_width/2, car_rect.y + car_height/2)

    # Draw the screen
    screen.fill(GREEN)

    # Draw the road
    road_rect = pygame.Rect(screen_width/4, 0, screen_width/2, screen_height)
    pygame.draw.rect(screen, GREY, road_rect)
    line_rect = pygame.Rect(screen_width/2 - 2.5, 0, 5, 25)
    for i in range(0, screen_height, 50):
        line_rect.top = i
        pygame.draw.rect(screen, WHITE, line_rect)
        


    # Draw the car
    screen.blit(sprite_image, car_rect)
    
    
    #draw the buttons 
    button_width = 100
    button_height = 50
    slow_button = pygame.Rect(75, 75, button_width, button_height)
    medium_button = pygame.Rect(75, 155, button_width, button_height)
    fast_button = pygame.Rect(75, 230, button_width, button_height)

    light_grey = (200, 200, 200)

    font = pygame.font.Font(None, 30)
    slow_text = font.render("Slow", True, WHITE)
    medium_text = font.render("Medium", True, WHITE)
    fast_text = font.render("Fast", True, WHITE)

    screen.blit(slow_text, (slow_button.left + (button_width - slow_text.get_width()) // 2, slow_button.top + (button_height - slow_text.get_height()) // 2))
    screen.blit(medium_text, (medium_button.left + (button_width - medium_text.get_width()) // 2, medium_button.top + (button_height - medium_text.get_height()) // 2))
    screen.blit(fast_text, (fast_button.left + (button_width - fast_text.get_width()) // 2, fast_button.top + (button_height - fast_text.get_height()) // 2))

    if car_rect.left < road_rect.left + (car_width / 2):
        car_rect.left = road_rect.left + (car_width / 2)
    elif car_rect.right > road_rect.right - (car_width / 2):
        car_rect.right = road_rect.right - (car_width / 2)
    if car_rect.top < road_rect.top + (car_height / 2):
        car_rect.top = road_rect.bottom - (car_height / 2)
    elif car_rect.bottom > road_rect.bottom - (car_height / 2):
        car_rect.bottom = road_rect.top + (car_height / 2
        
    checkbox_size = 20
    h2_sensor_value = 42
    temperature_value = 72
    valves_value = "Open"
    oxygen_sensor_value = 12.5
    pressure_value = 100

    # Set up the labels
    h2_sensor_value = 42
    temperature_value = 72
    valves_value = "Open"
    oxygen_sensor_value = 12.5
    pressure_value = 100

    # Set up the labels
    h2_sensor_label = font.render("h2_sensor: " + str(h2_sensor_value), True, BLACK)
    temperature_label = font.render("Temperature: " + str(temperature_value), True, BLACK)
    valves_label = font.render("Valves: " + valves_value, True, BLACK)
    oxygen_sensor_label = font.render("O^2 Sensor: " + str(oxygen_sensor_value), True, BLACK)
    pressure_label = font.render("Pressure: " + str(pressure_value), True, BLACK)

    # Draw the labels
    screen.blit(h2_sensor_label, (700, 50))
    screen.blit(temperature_label, (700, 100))
    screen.blit(valves_label, (700, 150))
    screen.blit(oxygen_sensor_label, (700, 200))
    screen.blit(pressure_label, (700, 250))
    
    pygame.display.update()

    # Limit the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)


    debouncer = Debouncer(.25)
leakyBucket = LeakyBucket(5, 1)
def my_loop():
    outOfRange = False

=======
TEMP_MIN = 0
TEMP_MAX = 100
PRESURE_MIN = 0
PRESURE_MAX = 100

sensor_Veh = {'Temp': 0.0, 'Presh': 0, 'Status': True, 'Faulty': False}
key_position = {
  'ACC': True,
  'RUN': False,
  'CRANK': False,
  'LOCKED': False  #if a sensor is faulty we will lock the position
}
ignition = True


def Read_data():
  try:
    with open(sensor_Manifest, 'r') as sensor_log:
      # Create CSV read object
      sensor_in = csv.DictReader(sensor_log)
      # print(type(sensor_in))
      for line in sensor_in:
        print(line)
      # Hold information in dictionary

      for key, value in sensor_Veh.items():
        if key in sensor_in:
          sensor_Veh[key] = sensor_in[key]

  except FileNotFoundError:
    print(f"No sensor manifest found!\n")
    return
>>>>>>> b71680bfc49b0aadd49e6a0802e0b5ca627f5cf7


def Write_data():
  sensor_dict = {}
  sensor_dict.update(sensor_Veh)

  try:
    with open(sensor_Manifest, 'w', newline='') as csv_file:
      fieldnames = ['key', 'value']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()
      for key, value in sensor_dict.items():
        try:
          writer.writerow({'key': key, 'value': value})
        except Exception as e:
          print(f"Error: Unable to update {key}: {value}!")
  except Exception as e:
    print(f"Error connected to sensor manifest!: {e}")


def Detect_Fault():
  for key, value in sensor_Veh.items():  #can take it out
    #call the leaking bucket algorethem instead
    #if leaking bucket changes faulty to false
    if key == 'Faulty':
      if (value == True):
        for key, valu in key_position.items():
          key_position.update({key: False})
    while True:
        if debouncer.debounce():
            if sensorCheck():
                outOfRange = True
            if add_packet(outOfRange):
                return True


#if the leaking bucket retrunes true after false , then the keyposition will be unstuck

      if (value == False):
        for key, value in key_position.items():
          key_position.update({key: True})

    if (key == 'Temp'):
      if value < TEMP_MIN:
        print("fault due to low temp")
      if value > TEMP_MAX:
        print("fault due to high temp")
    if (key == 'Presh'):
      if value < PRESURE_MIN:
        print("fault due to low pressure")
      if value > PRESURE_MAX:
        print("fault due to High pressure")


def main():
  Read_data()
  #call fun
  Detect_Fault()
  # for key, value in sensor_Veh.items():
  #   print(key,"-",value)
  for key, value in key_position.items():
    print(key, "-", value)
  #Write_data()


main()
