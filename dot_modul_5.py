from time import sleep
import bcrypt


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.age = age

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'Video({self.title}, {self.duration}, {self.time_now}, {self.adult_mode})'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and bcrypt.checkpw(password.encode(), user.password):
                self.current_user = user
                return f"Пользователь {nickname} успешно вошел."
        return "Неверный логин или пароль."

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print( f"Пользователь {nickname} уже существует.")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        return f"Пользователь {new_user.nickname} зарегистрирован и вошел в систему."

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None
            print("Вы вышли из аккаунта.")
        else:
            print("Вы не вошли в систему.")

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word=search_word.lower()
        matching_titles = []
        for video in self.videos:
            if search_word in video.title.lower():
                matching_titles.append(video.title)
        return matching_titles
    def watch_video(self,title):
            if self.current_user is not None:
                found_video = next((video for video in self.videos if video.title == title), None)
                if not found_video:
                    print(f"Видео '{title}' не найдено.")
                    return
                if found_video.adult_mode and self.current_user.age < 18:
                    print ("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(found_video.time_now + 1, found_video.duration + 1):
                    print(second, end=' ')
                    sleep(1)
                found_video.time_now = 0
                print("Конец видео")
            else:
                print("Войдите в аккаунт, чтобы смотреть видео")







ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
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
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
