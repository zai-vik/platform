import pymongo


class Database:
    def __init__(self):
        db_client = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = db_client["platform"]
        self.users = self.db["users"]
    
    def check_info(self, login, psword):
        user = self.users.find_one({'login': login})

        if user:
            if user['password'] == psword:
                suc = 1
                msg = ''
            else:
                suc = 0
                msg = 'Неверный пароль!'
        else:
            suc = 0
            msg = 'Пользователь не найдем!'
        
        return {'success': suc, 'message': msg}

    def insert_user(self, ent_login, ent_psword, ent_email):
        login = self.users.find_one({'login': ent_login})
        email = self.users.find_one({'email': ent_email})

        if login:
            suc = 0
            msg = 'Никнейм занят!'
        elif email:
            suc = 0
            msg = 'E-mail занят!'
        else:
            suc = 1
            msg = ''
        
            ins_result = self.users.insert_one({'login': ent_login, 'password': ent_psword, 'email': ent_email})
            print (f'{login} был добавлен в БД! id: {ins_result.inserted_id}')
        
        return {'success': suc, 'message': msg}
