# class Database:
#     def __init__(self):
#         self.data = {}
import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # nickname(имя пользователя, строка)
        self.password = hash(password)  # password(в хэшированном виде, число)
        self.age = age  # age(возраст, число)ass User:

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname

    def get_info(self):
        return self.nickname, self.password


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title  # title(заголовок, строка)
        self.duration = duration  # duration(продолжительность, секунды)
        self.time_now = time_now  # time_now(секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # bool (False по умолчанию)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    def __init__(self):
        # database = Database()
        self.users = []  # users(список объектов User),
        self.videos = []  # videos(список объектов Video),
        self.current_user = None  # current_user(текущий пользователь, User)

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == user.get_info():
                self.current_user = user
                return user

            # if nickname in self.users and hash(password) in user.password:
            #     self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        usser = User(nickname, password, age)

        if usser not in self.users:
            self.users.append(usser)
            self.current_user = usser
        else:
            print(f"Пользователь {nickname} уже существует")
            # users += self(User)
            # self.nickname += nickname
            # self.password += password
            # self.age += age
            # print(database.data)        #Для проверки

    def add(self, *videos: Video):
        for video in videos:
            if video.title not in videos:
                self.videos.append(video)
        # self.videos += self.videos:

    def get_videos(self, search):
        titles = []
        for video in self.videos:
            if search.lower() in str(video).lower():
                titles.append(video)
        return titles

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
            for i in range(video.time_now + 1, video.duration + 1):
                print(i, end=' ')
                time.sleep(1)
                video.time_now = i
            print("Конец видео")
            video.time_now = 0
            return
        print("Видео не найдено")


'''Метод watch_video, который принимает название фильма, 
если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, 
если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. 
После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. 
В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, 
т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"'''

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 11)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
