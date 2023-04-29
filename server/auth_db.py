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
    
    def replace_user(self, email):
        user = self.temp_users.find_one({'email': email})

        self.temp_users.delete_one({'email': email})
        
        res = self.users.insert_one({'login': user['login'], 'password': user['password'], 'email': user['email']})
        print (f"{user['login']} был добавлен в БД! id: {res.inserted_id}")
        
        return {'success': 1, 'message': ''}
    
    def insert_temp_user(self, ent_login, ent_psword, ent_email, code):
        login = self.users.find_one({'login': ent_login})
        email = self.users.find_one({'email': ent_email})

        if login:
            log = {'success': 0, 'message': 'Никнейм занят!'}
        elif email:
            log = {'success': 0, 'message': 'E-mail занят!'}
        else:
            log = {'success': 1, 'message': ''}
        
            res = self.temp_users.insert_one({
                'login': ent_login, 
                'password': ent_psword, 
                'email': ent_email, 
                'code': code
                })
            
            print (f'{ent_login} был добавлен в temp БД! id: {res.inserted_id}')
        
        return log
    
    def check_code(self, code):
        user = self.temp_users.find_one({'code': code})

        if user:
            log = {'success': 1, 'message': ''}
        else:
            log = {'success': 0, 'message': 'Неверный код аутентификации!'}
        
        return log
