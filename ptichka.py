from pygame import *
from random import randint


width = 800
height = 600
fps = 60
game = True

window = display.set_mode((width, height))
clock = time.Clock()

player_y = height // 2
speed = 0 #скорость
s2 = 0 #множитель скорости
player = Rect(width // 3, player_y, 50, 50)
sost = "start"
timer = 10
pipe_speed = 3
pipe_size = 200
pipe_pos = height // 2

pipes = []



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    key_pressed = key.get_pressed()
    press = mouse.get_pressed()
    click = key_pressed[K_SPACE] or press[0]
    if timer > 0:
        timer -= 1
    
    for i in range(len(pipes)-1, -1, -1):
        pipe = pipes[i]
        pipe.x  -= 3

        if pipe.right < 0:
            pipes.remove(pipe)

    if sost == "start":
        if click and timer == 0 and len(pipes) == 0:
            sost = "play"
        player_y += (height // 2 - player_y) * 0.1
        player.y = player_y
    elif sost == "play":
        if click:
            s2 = -2
        else: 
            s2 = 0
        player_y += speed
        speed = (speed + s2 + 1) * 0.98
        player.y = player_y

        if len(pipes) == 0 or pipes[len(pipes)- 1].x < width - 200:
            pipes.append(Rect(width, 0, 50, pipe_pos - pipe_size // 2)) 
            pipes.append(Rect(width, pipe_pos + pipe_size // 2 , 50, height - pipe_pos - pipe_size // 2)) 
            pipe_pos += randint(-100, 100)
            if pipe_pos < pipe_size:
                pipe_pos = pipe_size
            elif pipe_pos > height -  pipe_size:
                pipe_pos = height -  pipe_size

        if player.top < 0 or player.bottom > height:
            sost = "fall"

        for pipe in pipes:
            if player.colliderect(pipe):
                sost = "fall"
    
    elif sost == "fall":
        speed = 0
        s2 = 0
        sost = "start"
        timer = 60
    else:
        pass
    


    


    window.fill("Grey")
    for pipe in pipes:
        draw.rect(window, ("Green"), pipe)
    draw.rect(window, ("Yellow"), player)

    display.update()
    clock.tick(fps)


