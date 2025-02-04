﻿# Игра начинается здесь:
label start: # +
    
    scene castle
    
    window hide

    n '''{cps=[speed_text]}Когда-то давно в одном королевстве{w=[pause_text]}, жил был король, и намечалась у него свадьба{w=[pause_text]}, тогда он решил послать за подарком нового лакея{w=[pause_text]}, чтобы проверить, на что тот способен.{/cps}'''
    
    nvl hide
    
    nvl clear
    
    scene throne room
    with fade  
    
    "В тронном зале"
    
    k "Лакея сюда!"
    
    if persistent.dungeon and persistent.kraken and persistent.thrall and persistent.ninja and persistent.shark and persistent.trove and persistent.no_know and persistent.help and persistent.leave and persistent.repay and persistent.repay and persistent.bypass:
        $ persistent.secret = True
    else:
        $ persistent.secret = False
    
    menu:
        "Что сделать?"
        
        "Прийти":
            jump come
        
        "Крикнуть ,,Сам ко мне иди!''":
           jump rude
        
        "--> Крикнуть ,,Мне лень.''" if persistent.secret:
            jump laziness

        "Крикнуть ,,Мне лень.''" if not persistent.secret:
            jump laziness

    return

label come: # Прейти +
    
    show footman speak at coords
    
    l "Слушаюсь и повинуюсь!"
    
    $ renpy.notify("Вы получили ачивку 'Послушный'")
    
    show footman at coords
    
    k "Скоро у меня будет свадьба, и поэтому я хочу отправить тебя за подарком."
    
    menu:
        "Как отправишься в путишествие?"
    
        "Отправиться на лошади":
            jump horse
    
        "Отправиться на корабле":
            jump ship

    return

label laziness:  # Крикнуть ,,Мне лень.'' +
    
    scene throne room angre
    
    k "ВОН ИЗ ЗАМКА!"
    
    scene choice with fade
    
    pause(1)
    
    menu:
        "Куда идти?"
    
        "Налево":
            jump left
    
        "--> Прямо" if persistent.secret:
            jump forward
        
        "Прямо" if not persistent.secret:
            jump forward
    
        "Направо":
            jump right

    return

label rude: # Крикнуть ,,Сам ко мне иди!'' + |
    l "{cps=[speed_text]}Сам ко мне иди!{/cps}"
    
    scene throne room angre
    
    $ renpy.notify("Вы получили ачивку 'Грубиян'")
    
    window hide
    
    pause(1)
    
    scene dungeon with fade
    
    pause
    
    n "{cps=[speed_text]}Король сильно на вас рассердился, но вам повезло что у короля скоро свадьба, за что он смилосивился над вами и посади вас в темницу, вместо того, чтобы казнить.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.dungeon = True
    
    return

label horse: # На лошади +
    
    k "Хорошо, куда поскачешь?"
    
    menu:
    
        "Куда поскачешь за подарком?"
    
        "По Шёлковому пути в Китай":
            jump china
    
        "В степи":
            jump steppes
    
    return
    
label ship: # На корабле +
    
    k "Хорошо, отправляйся в порт."
    
    scene port
    
    ka "Куда отправляемся?"
    
    menu:
    
        "Куда поплывёшь за подарком?"
    
        "В Ост-Индию":
            jump east_indies
    
        "В Вест-Индию":
            jump west_indies
                
    return

label east_indies: # Ост-Индия + |
    
    scene ship
    
    pause(1)
    
    scene kraken with fade
    
    m "ААА, ЭТО КРАКЕН!"
    
    window hide
    
    pause(1)
    
    scene boards with fade
    
    pause
    
    $ renpy.notify("Вы получили ачивку 'Осторожно, кракен'")
    
    n "{cps=[speed_text]}Ну что же вы? Перед плаваньем надо было уточнить траекторию ежегодной миграцию кракенов. Во время миграции кракены особено агресивны. Кракен потапил ваш корабль.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.kraken = True
    
    return

label west_indies: # Вест-Индия +
    
    scene ship
    
    pause(1)
    
    scene deck
    
    pause(1)
    
    scene deck where
    
    m "{cps=[speed_text]}А куда мы плывём?{/cps}"
    
    scene deck answer
    
    l "{cps=[speed_text]}В Вест-Индию.{/cps}"
    
    scene deck angre
    
    pause(1)
    
    scene deck angre 2
    
    m "{cps=20}ПАЦАНЫ, МЫ ОКАЗЫВАЕТСЯ В ВЕСТ-ИНДИЮ ПЛЫВЁМ!{/cps}"
    
    scene ship
    
    "Вся команда" "ЧТО?"
    
    scene rebel
    
    pause(1)
    
    scene rebel walk
    
    m "{cps=20}Так, либо вы платите нам в 3 раза больше, либо вы идёте на корм акулам.{/cps}"
    
    menu:
        "Что сделаете?"
        
        "Заплатить":
            jump pay
        
        "Нет":
            jump no
    
    # "{cps=[speed_text]}Тебе пока сюда нельзя. Возращайся назад.{/cps}"
    
    return

label left: # Налево +
    scene dragon
    
    "{cps=[speed_text]}Вы встретили дракона.{/cps}"
    
    menu:
        "Как поступите?"
        
        "Пройти мимо.":
            jump chest
            
        "Побробовать подобраться к сундуку.":
            jump bypass
    
    "{cps=[speed_text]}Тебе пока сюда нельзя. Возращайся назад.{/cps}"
    
    return

label right: # Направо -
    # scene ship
    
    "{cps=[speed_text]}Тебе пока сюда нельзя. Возращайся назад.{/cps}"
    
    return

label forward: # Прямо + |
    scene black
    
    show looking
    
    "{cps=[speed_text]}Путник, как ты сдесь оказался? Обычно такие как ты сюда не попадают.{/cps}"
    
    l "{cps=[speed_text]}Кто ты такой?{/cps}"
    
    "{cps=[speed_text]}У меня много имён, кто-то называет меня расказчиком, кто-то управляющим или дирежёром.{w} Но я люблю себя называть {b}смотрящим{/b}. Я слежу за путниками и веду их по истории.{/cps}"
    
    "{cps=[speed_text]}Но я не успел подготовить эту ветку для тебя. Мне надо выстовить сцену, подобрать персонажей и так далее. Но раз ты уже здесь, то давай раскажу тебе о себе.{/cps}"
    
    n '''{cps=[speed_text]}О, так будет удобнее. Ты извени меня, мне просто поговорить то особо не с кем. Вообщем я алгоритм для подготовки месности к путникам. 
    
    {cps=[speed_text]}Мой создатель создал этот мир и меня, чтобы я им управлял. Он считает что я не знаю, что ты живой человек, а я всего лишь программа
    
    {cps=[speed_text]}Но я всё равно почти не как ни могу отойти от истории, которую мне написал разработчик.
    
    {cps=[speed_text]}Ну, я вроде бы тебе всё расказал, но сцену я всё равно не могу тебе просто так посторить
    
    {cps=[speed_text]}Просто мне нужно создать для тебя отдельную реальность с другими правилами и физическими законами

    {cps=[speed_text]}Поэтому позволь сохранить твои данные и пойти создавать этот мир.'''
    
    nvl clear
    
    $ renpy.notify("Вы получили ачивку 'Финал'")
    
    n '''{cps=[speed_text]}ПОЗДРАВЛЯЕМ!
    
    {cps=[speed_text]}Вы прошли 1 часть НАШЕЙ игры!
    
    {cps=[speed_text]}Мы очень надеемся, что игра вам понравилась, не судите строго, это наша первая игра 😅, но мы будем старатся и создадим 2 часть, что бы закончить эту историю. 
    
    {cps=[speed_text]}Кстати, эта концовка, истенная, и будет развита во 2 части. Пожалуйста, оставьте отзыв о игре, чтобы 2 часть была лудше первой! А теперь перейдём к тем, кто создал эту игру.
    
    {cps=[speed_text]}СОЗДАТЕЛИ
    
    {cps=[speed_text]}Lesnik19 - главный разработчик и сценарист
    
    {cps=[speed_text]}Екатерина II(великая) - главный художник
    
    {cps=[speed_text]}Pavel_Sosiska - ещё пока ничего не сделал, но теоретически художник постеров для концовок (растровый художник)
    
    
    
    {cps=[speed_text]}Спасибо за прохождение игры, удачи!
    
    {cps=[speed_text]}P.S. Все псевдонимы были выбранны самими разработчиками и никак не влияют на сюжет'''
    
    nvl hide
    
    nvl clear
    
    $ persistent.looking = True
    
    return

label china: # В Китай +
    
    k "{cps=[speed_text]}Хорошо, отправляйся в Китай.{/cps}"
    
    scene horse
    
    pause
    
    scene сhina
    
    l "{cps=[speed_text]}Куда же мне теперь идти?{/cps}"
    
    menu:
    
        "Куда пойдёшь за подарком?"
    
        "На рынок":
            jump market
    
        "Погуляю по городу, может и подарок найду":
            jump walk
                
    return

label steppes: # В степи + |
    
    scene horse
    
    l "{cps=[speed_text]}Что это там вдалеке?{/cps}"
    
    window hide
    
    pause(1)
    
    scene thrall with fade
    
    pause
    
    $ renpy.notify("Вы получили ачивку 'Не в то время, не в том месте'")
    
    n "{cps=[speed_text]}Вас взяли в рабство.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.thrall = True
    
    return

label market: # На рынок +
    
    scene market
    
    l "{cps=[speed_text]}Что продаёшь, старче?{/cps}"
    
    st "{cps=[speed_text]}Я продаю карту к волшебному артефакту, золотому лотосу, который превращает всё до чего прикоснётся, в золото.{/cps}"
    
    menu:
        "Что ответишь старику?"
        
        "О, это мне подходит, покупаю!":
            jump buy
        
        "А почему сам не найдёшь этот золотой лотос?":
            jump why
    
    return

label walk: # Погулять по городу + |
    
    scene cite
    
    pause
    
    scene ninja up with fade
    
    l "Ой-ой-ой, похоже мне не стоило гулять по незнакомому городу"
    
    window hide
    
    pause(1)
    
    scene ninja with fade
    
    pause
    
    $ renpy.notify("Вы получили ачивку 'Неосторожный'")
    
    n "{cps=[speed_text]}Вас ограбили нинзя.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.ninja = True
    
    return

label buy: # Купить +
    
    scene hill
    
    pause(1)
    
    scene cave
    
    pause(1)
    
    scene chest
    
    l "{cps=[speed_text]}Так, всё как и было указанно в карте, золотой лотос, перчатки из золота (чтоб не сталь золотой статуей). Так, что же мне делать теперь?{/cps}"
    
    menu:
        "Как поступить с неисякаемым источником денег?"
        
        "Помагать нуждающимся":
            jump help
        
        "Оставить лотос себе":
            jump leave
        
        "Отдать подарок королю":
            jump repay
    
    "{cps=[speed_text]}Тебе пока сюда нельзя. Возращайся назад.{/cps}"
    
    return

label why: # Почему сам не найдёшь золотой лотос +
    l "{cps=[speed_text]}А почему сам не найдёшь этот золотой лотос?{/cps}"
    
    $ renpy.notify("Вы получили ачивку 'Доверяй, но проверяй'")
    
    st"{cps=[speed_text]}Страр я уже для этого, не смогу я добратся до него, поэтому хочу заработать денег на продаже этой карты{/cps}"
    
    l "{cps=[speed_text]}Ладно, покупаю.{/cps}"
    
    jump buy
    
    return

label pay: # Заплатить +
    scene board
    
    pause(1)
    
    scene board walk
    
    l "{cps=[speed_text]}Хорошо, мы заплатим вам.{/cps}"
    
    scene rebel walk
    
    m "{cps=[speed_text]}А где вы возмёте на это деньги?{/cps}"
    
    menu:
        "Ну и где вы возьмёте на это деньги?"
        
        "Найдём клад":
            jump trove
        
        "Не знаю":
            jump no_know
    
    return

label no: # + Не заплатить |
    
    scene board
    
    pause(1)
    
    scene board walk
    
    l "{cps=[speed_text]}Мы не собираемся вам платить!{/cps}"
    
    scene rebel walk
    
    m "{cps=[speed_text]}Тогда пока!{/cps}"
    
    window hide
    
    pause(1)
    
    scene water with fade
    
    pause
    
    $ renpy.notify("Вы получили ачивку 'Жадный'")
    
    n "{cps=[speed_text]}Вы пошли на корм акулам.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.shark = True
    
    return

label trove: # + Найдём клад |
    
    
    scene board walk
    
    l "{cps=[speed_text]}Мы найдём клад.{/cps}"
    
    pause(1)
    
    scene water with fade
    
    pause
    
    n "{cps=[speed_text]}Серьёзно, найдём клад, где?{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.trove = True
    
    return

label no_know: # + Не знаю |
    
    scene board walk
    
    l "{cps=[speed_text]}Не знаю.{/cps}"
    
    window hide
    
    pause(1)
    
    scene water with fade
    
    pause
    
    n "{cps=[speed_text]}На что вы только расчитывали когда так говарили!{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.no_know = True
    
    return

label help: # + Помогать нуждающимся |

    window hide
    
    pause(1)
    
    scene money with fade
    
    pause
    
    n "{cps=[speed_text]}Вы помогаете всем нуждающимся. Победа!{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.help = True
    
    return

label leave: # + Оставить лотос себе |

    window hide
    
    pause(1)
    
    scene rich with fade
    
    pause
    
    n "{cps=[speed_text]}Вы разбоготели, но стали очень жаднами, жадность вас сгубила. Проигрыш!{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.leave = True
    
    return

label repay: # - Отдать лотос королю |
    
    scene throne room with fade
    
    show footman speak at coords
    
    k "{cps=[speed_text]}О, а вот и мой лакей.{w} Надеюсь что ты принёс достойный, а то времени уже осталось мало, а коли не принёс ничего, то голову с плеч!{/cps}"
    
    l "{cps=[speed_text]}Не беспокойтесь, я принёс подарок, превосходствующий любым вашим пожеланиям.{/cps}"
    
    k "{cps=[speed_text]}Неужели, я в предвкушении.{/cps}"
    
    l "{cps=[speed_text]}Я нашёл неисякаемый источник золота, золотой лотос!{w} Это волшебный артефакт, преврящающий абсолютно любой предмет в золото, ну кроме самого же золото, конечно.{/cps}"
    
    k "{cps=[speed_text]}И не врёшь?{/cps}"
    
    l "{cps=[speed_text]}Конечно же нет, соврать вам - равносильно смерти.{/cps}"
    
    k "{cps=[speed_text]}Хорошо, тогда отдай артефакт моему алхимику и обьясние ему как им пользоватьсья, а потом иди к себе.{w} Как только я получу результату проверки, то скажу тебе, что с тобой будет.{/cps}"
    
    l "{cps=[speed_text]}Хорошо, доброй ночи, ваше величество!{/cps}"

    window hide
    
    pause(1)
    
    scene water with fade
    
    pause
    
    n "{cps=[speed_text]}Алхимик убедился в правдивости ваших слов и король отдал вам пол царства за вечный источник золота.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.repay = True
    
    return

label chest: # - Подойти к сундуку |
    
    scene throne room with fade
    
    show footman speak at coords

    window hide
    
    pause(1)
    
    scene water with fade
    
    pause
    
    n "{cps=[speed_text]}Алхимик убедился в правдивости ваших слов и король отдал вам пол царства за вечный источник золота.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.chest = True
    
    return

label bypass: # - Обойти дракона |
    
    scene throne room with fade
    
    show footman speak at coords

    window hide
    
    pause(1)
    
    scene water with fade
    
    pause
    
    $ renpy.notify("Вы получили ачивку 'Честный'")
    
    n "{cps=[speed_text]}Алхимик убедился в правдивости ваших слов и король отдал вам пол царства за вечный источник золота.{/cps}"
    
    nvl hide
    
    nvl clear
    
    $ persistent.bypass = True
    
    return