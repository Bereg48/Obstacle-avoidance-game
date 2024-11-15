import pygame
<<<<<<< HEAD

back = pygame.image.load('code_game_back_floor.jpg')
hero = pygame.image.load('detective.png')
pot = pygame.image.load('teapot.png')
candle = pygame.image.load('candlestick.png')
box = pygame.image.load('wooden_box.png')
=======
from sys import exit

pygame.init()

# объявляем ширину и высоту экрана
width = 800
height = 400

# создаём экран игры
screen = pygame.display.set_mode((width, height))

# устанавливаем количество кадров в секунду
fps = 60
# создаём объект таймера
clock = pygame.time.Clock()

# создаём объекты шрифта: в скобках указываем шрифт и размер через запятую
text_font = pygame.font.Font('prstartk.ttf', 15)
text_font_collide = pygame.font.Font('prstartk.ttf', 50)

# создаём новую поверхность земли отдельным объектом surface
# в финальном коде не используется
# 1 - задаём размеры:
width_ts = 800
height_ts = 200
# 2 - создаём  поверхность по  размерам
test_surface = pygame.Surface((width_ts, height_ts))
# 3 - добавляем цвет
test_surface.fill('Brown')

# загружаем в переменные картинки из папки с нашим файлом
back = pygame.image.load('code_game_back_floor.jpg').convert()
hero = pygame.image.load('detective.png').convert_alpha()
pot = pygame.image.load('teapot.png').convert_alpha()
candle = pygame.image.load('candlestick.png').convert_alpha()
box = pygame.image.load('wooden_box.png').convert_alpha()

# объявляем переменные с начальными координатами для всех анимаций
hero_x_pos = 75
hero_y_pos = 180
candle_x_pos = 900
candle_y_pos = 70
box_x_pos = 900
box_y_pos = 200
pot_x_pos = 900
pot_y_pos = 345

# помещаем изображения в рамки прямоугольника
# в скобках задаём точку привязки и координаты для неё
hero_rect = hero.get_rect(center=(hero_x_pos, hero_y_pos))
pot_rect = pot.get_rect(center=(pot_x_pos, pot_y_pos))
candle_rect = candle.get_rect(center=(candle_x_pos, candle_y_pos))
box_rect = box.get_rect(center=(box_x_pos, box_y_pos))

# создаём сигнальные переменные
pot_flag = False
box_flag = False

# создаём объект текста: в скобках указываем текст, сглаживание и цвет
text_surface = text_font.render('Detective CODE Game', False, 'White')
text_collide = text_font_collide.render('CoLLiDE!!', False, 'Red')

# даём название окну игры
pygame.display.set_caption('Detective CODE Game')

# объявляем переменную-флаг для цикла игры
game = True

# запускаем бесконечный цикл
while game:
   # получаем список возможных действий игрока
   for event in pygame.event.get():
       # если пользователь нажал на крестик закрытия окна
       if event.type == pygame.QUIT:
           # выключаем цикл
           pygame.quit()
           # добавляем корректное завершение работы
           exit()

       # получаем список всех нажатых клавиш
       keys = pygame.key.get_pressed()

       # если нажата клавиша вверх, двигаем картинку вверх
       if keys[pygame.K_UP]:
           hero_rect.top -= 20
       # если нажата клавиша вниз, двигаем картинку вниз
       if keys[pygame.K_DOWN]:
           hero_rect.top += 20

   # размещаем все поверхности на нашем экране
   screen.blit(back, (0, 0))
   screen.blit(hero, hero_rect)
   screen.blit(candle, candle_rect)
   screen.blit(box, box_rect)
   screen.blit(pot, pot_rect)
   back.blit(text_surface, (250, 15))

   # запускаем движение всех предметов
   candle_rect.left -= 4
   # когда подсвечник пересёк половину экрана,
   # меняем сигнальную переменную для чайника и начинаем его движение
   if candle_rect.left <= 400:
       pot_flag = True
   if pot_flag:
       pot_rect.left -= 4

   # когда чайник пересёк половину экрана,
   # меняем сигнальную переменную для ящика и начинаем его движение
   if pot_rect.left <= 400:
       box_flag = True
   if box_flag:
       box_rect.left -= 4

   # обнуляем начальные координаты, когда правая грань
   # скрылась за границей экрана
   if candle_rect.right <= 0:
       candle_rect.left = 800
   if pot_rect.right <= 0:
       pot_rect.left = 800
   if box_rect.right <= 0:
       box_rect.left = 1000

# выводим сообщения о столкновении
if hero_rect.colliderect(candle_rect) or hero_rect.colliderect(pot_rect) or hero_rect.colliderect(box_rect):
   screen.blit(text_collide, (200, 165))

   # обновляем экран игры
   pygame.display.update()
   # добавляем к таймеру количество fps для частоты обновления основного цикла
   clock.tick(fps)
>>>>>>> 248f034 (loading all images into variables)
