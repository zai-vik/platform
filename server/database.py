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
                mes = ''
            else:
                suc = 0
                msg = 'неверный пароль'
        else:
            suc = 0
            msg = 'пользователь не найдем'
        
        return {'success': suc, 'message': mes}

    def insert_user(self, login, psword, email):
        req = {
            'login': login, 
            'password': psword, 
            'email': email
        }
        
        ins_result = self.users.insert_one(req)

        print (f'{login} был добавлен в БД! id: {ins_result.inserted_id}')
        return ins_result.inserted_id


db = Database()

# db.insert_user('kurva', 'dddddd', 'kurva@mail.ru')
# db.insert_user('aboba', '1234', 'fgfgfg@mail.ru')
# db.insert_user('stasy', 'zxcv', 'qw12erer@mail.ru')
# db.insert_user('annanushka', 'qwerty', 'jkjkjkjk@mail.ru')

print(db.check_info('kurva', 'dddddd'))
print(db.check_info('kurva', '1'))
print(db.check_info('annanushka', '1234'))
print(db.check_info('fapfap', 'dddddd'))
