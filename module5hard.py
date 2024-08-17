import time

class User:
    
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    
    def __repr__(self):
        return f"{self.nickname}"

class Video:
    
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        
    def __repr__(self):
        return (f"Название: {self.title}, {self.duration} Секунд, "
                f"time_now: {self.time_now}, adult mode: {self.adult_mode})")
        
class UrTube:
    
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print("Неверный логин или пароль.")
        
    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
    
    def log_out(self):
        self.current_user = None
    
    def add(self, *videos: Video):
        for video in videos:
            if all(existing_video.title != video.title for existing_video in self.videos):
                self.videos.append(video)
    
    def get_videos(self, search_video: str):
        search_video = search_video.lower()
        return [video.title for video in self.videos if search_video in video.title.lower()]
    
    def watch_video(self, title: str):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
        
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)
                    
                print("Конец видео")
                video.time_now = 0
                return
        
        print("Видео не найдено.")
        
    def __repr__(self):
        return (f"Пользователи UrTube:{len(self.users)}, Видео: {len(self.videos)}, "
                f"Текущий пользователь: {self.current_user})")
        
        
        
        
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

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')