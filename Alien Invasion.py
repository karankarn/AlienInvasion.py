import sys
import pygame
from pygame.sprite import Group
from alien import Alien
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
    #Initialize game and create screen object
    pygame.init()
    # Using variable 'ai settings' for class 'Settings()'
    ai_settings = Settings()
    #Drawing screen
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #Naming Screen
    pygame.display.set_caption("Alien Invasion")
    #Make a play button
    play_button = Button(ai_settings,screen,"Play")

    #Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #Make an alien
    gf.create_fleet(ai_settings,screen,ship,aliens)
    alien =Alien(ai_settings,screen)

    #Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)


    #Starting main loop of game
    while True:
        #checking events from game_functions
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        #updating screen from game_functions
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()