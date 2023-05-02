import pymongo


class Database:
    def __init__(self):
        db_client = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = db_client["platform"]
        self.users = self.db["users"]
        self.temp_users = self.db["temp_users"]
    
    def check_info(self, login, psword):
        user = self.users.find_one({'login': login})

        if user:
            if user['password'] == psword:
                log = {'success': 1, 'message': ''}
            else:
                log = {'success': 0, 'message': 'Неверный пароль!'}
        else:
            log = {'success': 0, 'message': 'Пользователь не найдем!'}
        
        return log
    
    def check_new_user(self, ent_login, ent_email):
        login = self.users.find_one({'login': ent_login})
        email = self.users.find_one({'email': ent_email})

        if login:
            log = {'success': 0, 'message': 'Никнейм занят!'}
        elif email:
            log = {'success': 0, 'message': 'E-mail занят!'}
        else:
            log = {'success': 1, 'message': ''}

        return log
