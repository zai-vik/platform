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
                msg = 'неверный пароль'
        else:
            suc = 0
            msg = 'пользователь не найдем'
        
        return {'success': suc, 'message': msg}

    def insert_user(self, login, psword, email):
        req = {
            'login': login, 
            'password': psword, 
            'email': email
        }
        
        ins_result = self.users.insert_one(req)

        print (f'{login} был добавлен в БД! id: {ins_result.inserted_id}')
        return ins_result.inserted_id
