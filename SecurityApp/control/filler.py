# coding=utf8
import psycopg2
import random
import time
from contextlib import suppress


conn = psycopg2.connect("dbname='Supermarket' user='postgres' password='Lovunod2302' host='localhost' port='5432'")
cur = conn.cursor()
names = ['Азамат', 'Азат', 'Александр', 'Алексей', 'Альберт', 'Анатолий', 'Андрей', 'Антон', 'Артём', 'Аркадий', 'Арсений', 'Артур', 'Богдан', 'Борис', 'Валерий', 'Валентин', 'Василий', 'Вадим', 'Владимир', 'Владислав', 'Виктор', 'Виталий', 'Вячеслав', 'Григорий', 'Глеб', 'Герман', 'Георгий', 'Геннадий', 'Давид', 'Даниил', 'Дмитрий', 'Денис', 'Евгений', 'Егор', 'Захар', 'Иван', 'Игорь', 'Ильдар', 'Илья', 'Кирилл', 'Константин', 'Леонид', 'Марат', 'Марк', 'Максим', 'Михаил', 'Назар', 'Никита', 'Николай', 'Олег', 'Павел', 'Пётр', 'Рашид', 'Ринат', 'Роберт', 'Роман', 'Руслан', 'Рустам', 'Святослав', 'Станислав', 'Степан', 'Сергей', 'Семён', 'Тарас', 'Тимофей', 'Филипп', 'Фёдор', 'Эрик', 'Эльдар', 'Эмиль', 'Эдуард', 'Юрий', 'Ярослав', 'Яков']
surnames = ["Абрамов", "Авдеев", "Агафонов", "Аксёнов", "Александров", "Алексеев", "Андреев", "Анисимов", "Антонов", "Артемьев", "Архипов", "Афанасьев", "Баранов", "Белов", "Белозёров", "Белоусов", "Беляев", "Беляков", "Беспалов", "Бирюков", "Блинов", "Блохин", "Бобров", "Бобылёв", "Богданов", "Большаков", "Борисов", "Брагин", "Буров", "Быков", "Васильев", "Веселов", "Виноградов", "Вишняков", "Владимиров", "Власов", "Волков", "Воробьёв", "Воронов", "Воронцов", "Гаврилов", "Галкин", "Герасимов", "Голубев", "Горбачёв", "Горбунов", "Гордеев", "Горшков", "Григорьев", "Гришин", "Громов", "Гуляев", "Гурьев", "Гусев", "Гущин", "Давыдов", "Данилов", "Дементьев", "Денисов", "Дмитриев", "Доронин", "Дорофеев", "Дроздов", "Дьячков", "Евдокимов", "Евсеев", "Егоров", "Елисеев", "Емельянов", "Ермаков", "Ершов", "Ефимов", "Ефремов", "Жданов", "Жуков", "Журавлёв", "Зайцев", "Захаров", "Зимин", "Зиновьев", "Зуев", "Зыков", "Иванков", "Иванов", "Игнатов", "Игнатьев", "Ильин", "Исаев", "Исаков", "Кабанов", "Казаков", "Калашников", "Калинин", "Капустин", "Карпов", "Кириллов", "Киселёв", "Князев", "Ковалёв", "Козлов", "Колесников", "Колобов", "Комаров", "Комиссаров", "Кондратьев", "Коновалов", "Кононов", "Константинов", "Копылов", "Корнилов", "Королёв", "Костин", "Котов", "Кошелев", "Красильников", "Крылов", "Крюков", "Кудрявцев", "Кудряшов", "Кузнецов", "Кузьмин", "Кулагин", "Кулаков", "Куликов", "Лаврентьев", "Лазарев", "Лапин", "Ларионов", "Лебедев", "Лихачёв", "Лобанов", "Логинов", "Лукин", "Лыткин", "Макаров", "Максимов", "Мамонтов", "Марков", "Мартынов", "Маслов", "Матвеев", "Медведев", "Мельников", "Меркушев", "Миронов", "Михайлов", "Михеев", "Мишин", "Моисеев", "Молчанов", "Морозов", "Муравьёв", "Мухин", "Мышкин", "Мясников", "Назаров", "Наумов", "Некрасов", "Нестеров", "Никитин", "Никифоров", "Николаев", "Никонов", "Новиков", "Носков", "Носов", "Овчинников", "Одинцов", "Орехов", "Орлов", "Осипов", "Павлов", "Панов", "Панфилов", "Пахомов", "Пестов", "Петров", "Петухов", "Поляков", "Пономарёв", "Попов", "Потапов", "Прохоров", "Рогов", "Родионов", "Рожков", "Романов", "Русаков", "Рыбаков", "Рябов", "Савельев", "Савин", "Сазонов", "Самойлов", "Самсонов", "Сафонов", "Селезнёв", "Селиверстов", "Семёнов", "Сергеев", "Сидоров", "Силин", "Симонов", "Ситников", "Соболев", "Соколов", "Соловьёв", "Сорокин", "Степанов", "Стрелков", "Субботин", "Суворов", "Суханов", "Сысоев", "Тарасов", "Терентьев", "Тетерин", "Тимофеев", "Титов", "Тихонов", "Третьяков", "Трофимов", "Туров", "Уваров", "Устинов", "Фадеев", "Фёдоров", "Федосеев", "Федотов", "Филатов", "Филиппов", "Фокин", "Фомин", "Фомичёв", "Фролов", "Харитонов", "Хохлов", "Цветков", "Чернов", "Шарапов", "Шаров", "Шашков", "Шестаков", "Шилов", "Ширяев", "Шубин", "Щербаков", "Щукин", "Юдин", "Яковлев", "Якушев", "Смирнов"]
patronimics = ["Александрович", "Алексеевич", "Анатольевич", "Андреевич", "Антонович", "Аркадьевич", "Арсеньевич", "Артемович", "Афанасьевич", "Вадимович", "Валентинович", "Валериевич", "Васильевич", "Викторович", "Витальевич", "Владимирович", "Всеволодович", "Вячеславович", "Давыдович", "Данилович", "Денисович", "Дмитриевич", "Кириллович", "Константинович", "Корнеевич", "Леонидович", "Львович", "Евгеньевич", "Егорович", "Емельянович", "Ефимович", "Гаврилович", "Геннадиевич", "Георгиевич", "Глебович", "Григорьевич", "Богданович", "Борисович", "Назарович", "Наумович", "Николаевич", "Робертович", "Родионович", "Романович", "Тарасович", "Тимофеевич", "Тихонович", "Савельевич", "Семенович", "Сергеевич", "Станиславович", "Степанович"]
i = 1
sellers = ["Gazprom", "Lukoil", "Rosneft", "Sberbank of Russia", "Russian Railways", "Rostec", "VTB", "Otkritie Holding", "Alfa-Bank", "Rostelecom", "Sakhalin Energy", "United Shipbuilding Corporation", "SUEK", "VimpelCom", "T Plus", "Stroygazmontazh", "Metalloinvest", "Lenta", "MegaFon", "RusHydro", "Ural Mining and Metallurgical Company", "Magnitogorsk Iron and Steel Works", "Mobile TeleSystems", "United Aircraft Corporation", "Severstal", "Aeroflot", "Norilsk Nickel", "Rusal", "Sibur", "Novatek", "NLMK", "Evraz", "Gazprombank", "Tatneft", "Sistema", "Rosatom", "Transneft", "Inter RAO", "Rosseti", "Magnit", "Surgutneftegas", "X5 Retail Group"]
types = ["Цветы", "Газ", "Ягоды", "Конфеты", "Инструмент", "Картина", "Овощи", "Фрукты", "Техника", "Услуга"]
products = ["Assemble Products", "Build-It-Now", "Construction Gods", "Imagination Creation", "New Authors House", "Blossom", "The Come Up", "Make It Right", "Gold Works", "Brick-And-Stone", "Good Times Fun", "Design Dynasty", "Cultivate Excellence", "Write It Up!", "Stone Cold Products", "Bread And Butter Designs", "Composure Products", "Sweet Lines", "Pull Together Products", "We Make Things", "Manufactured Mavens", "The Real Deal Products", "The Collection Products", "Weproduce", "Make Believe Products", "Gold Stuff", "Show Owt Products", "Designed For Greeks Products", "Get It To The Greeks", "Flowerframe Products", "Make An Offer", "Come Through Products", "Show The Goods", "The Original Products", "Open Here Products", "Gifts Galore", "The Best Kept Secret", "Mystery Boxes Unopened", "Reinvent You Products", "Creators Collab", "Procreate Genius", "Genius Bros Products", "Brainstorm Babe Product", "Conjured Gold Product", "Alchemical Products", "Fancy Babies", "Vision Forward Product Line" ,"Featured Fantasy Products", "Nurture Brilliance"]
ms = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

def do_the_thing(i):
    name = random.choice(names)
    surname = random.choice(surnames)
    patronimic = random.choice(patronimics)
    points = random.randrange(200, 300)
    with suppress(Exception):
        cur.execute("insert into names (name, surname, patronimic, points) values (%s, %s, %s, %s)", (name, surname, patronimic, points))
        conn.commit()
    time.sleep(0.05)
    do_the_thing(i)


def seller():
    for i in range(42):
        cur.execute("insert into seller (seller) values ('{}')".format(sellers[i]))
        conn.commit()


def p_type():
    for i in range(10):
        cur.execute("insert into p_type (p_type) values ('{}')".format(types[i]))
        conn.commit()


def buyer():
    for i in range(250):
        cur.execute("insert into buyer (name, last, balance) values ('{}', '{}', {})".format(random.choice(names), random.choice(surnames), int(random.randint(1, 100))*1000))
        conn.commit()


def product():
    for i in range(250):
        cost = random.randint(10, 5000)
        cur.execute("insert into product (product, price, cost, quantity, supply_drop, seller, p_type) values ('{}', {}, {}, {}, '{}', {}, {})".format(random.choice(products), cost*1.25, cost, random.randint(1, 1000), str(random.randint(1, 30))+" числа", random.randint(1, 42), random.randint(1, 10)))
        conn.commit()


def order():
    for i in range(1000):
        cur.execute(
            "insert into orders(item, amount, date_time, buyer) values ({}, {}, '{}', {})".format(random.randint(1, 247), random.randint(1, 100), str(random.randint(1, 30)) + " " + random.choice(ms), random.randint(1, 250)))
        conn.commit()

# do_the_thing(i)
order()
