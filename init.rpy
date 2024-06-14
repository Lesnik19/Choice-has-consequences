# Определение персонажей игры.
define l = Character('Лакей', color="#550000", image='footman')
define k = Character('Король', color="#00cc00", image='king')
define s = Character('[secret]', color="#000000")
define ka = Character("Капитан", color="#000000")
define m = Character("Мотрос", color="#000000")
define st = Character("Старик", color="#000000")

define n = Character(None, kind=nvl)

define speed_text = 15 # Скорость печати текста
define pause_text = 0.5 # Время между частями текста

# музыка и звуки

define audio.secret_music = "music/music_scene.mp3"

init:
    $ coords = Position(xalign=2, yalign=0.9)

init python:
    g = Gallery()
    
    g.locked_button = "images/posters/poster lock.png"
    
    g.button("poster dungeon")
    g.condition("persistent.dungeon")
    g.image("poster dungeon")
    
    g.button("poster boards")
    g.condition("persistent.kraken")
    g.image("poster boards")
    
    g.button("poster looking")
    g.condition("persistent.looking")
    g.image("poster looking")
    
    g.button("poster thrall")
    g.condition("persistent.thrall")
    g.image("poster thrall")
    
    g.button("poster ninja")
    g.condition("persistent.ninja")
    g.image("poster ninja")
    
    g.button("poster shark")
    g.condition("persistent.shark")
    g.image("poster shark")
    
    g.button("poster shark2")
    g.condition("persistent.trove")
    g.image("poster shark2")
    
    g.button("poster shark3")
    g.condition("persistent.no_know")
    g.image("poster shark3")
    
    g.button("poster money")
    g.condition("persistent.help")
    g.image("poster money")
    
    g.button("poster rich")
    g.condition("persistent.leave")
    g.image("poster rich")
    
    g.button("poster repay")
    g.condition("persistent.repay")
    g.image("poster repay")
    
    # g.button("poster chest")
    # g.condition("persistent.chest")
    # g.image("poster chest")
    
    # g.button("poster bypass")
    # g.condition("persistent.bypass")
    # g.image("poster bypass")

label splashscreen:
    
    scene black
    
    pause(0.5)
    
    scene developer with fade
    
    pause(3)
    
    scene black with fade
