import mysql.connector


class DBhelper:

    def __init__(self):
        # to connect to the database
        try:
            self.conn = mysql.connector.connect(host='localhost', port='8889', user='root', password='root', database= 'finder')
            self.mycursor = self.conn.cursor()
            print("Connected to DB")
        except Exception as e:
            print(e)

    def check_login(self, email, password):

        self.mycursor.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password))
        data = self.mycursor.fetchall()

        # print(data)


        if len(data) > 0:
            return data
        else:
            return []
    #registration database handler
    def insert_user(self, name, email, password,age):

        if len(age)==2:
            in_age= int(age)
            # print(type(age))
            if in_age >= 18:

                try:

                    self.mycursor.execute("INSERT INTO users (user_id,name,email,password,bio,age,gender,city,dp) VALUES (NULL, '{}', '{}', '{}', '', {}, '', '', '')".format(name, email, password,age))
                    self.conn.commit()
                    return 1
                except Exception as e:
                    print(e)
                    return 0
            else: return 2
        else:
            return 0


    def update_profile(self, user_id, info):

        try:
            self.mycursor.execute("UPDATE users SET bio='{}',age={},gender='{}',city='{}',dp='{}' WHERE user_id={}".format(info[0], info[1], info[2], info[3],info[4], user_id))
            self.conn.commit()
            return 1
        except:
            return 0
    #update main window after edit profile
    def submit_reg_check(self,user_id):
        # print(user_id)
        self.mycursor.execute("SELECT * FROM users WHERE user_id = {}".format(user_id))
        data = self.mycursor.fetchall()

        return data[0]
    #fetch other profile data
    def fetch_profile(self,user_id):
        #int_user=user_id
        try:
            self.mycursor.execute("SELECT * FROM users WHERE user_id != {}".format(user_id))
            data = self.mycursor.fetchall()
            # print(data)
            return data
        except Exception as e:
            print(e)
    def propose(self,romeo_id,juliet_id):

        self.mycursor.execute("SELECT * FROM proposals WHERE romeo_id={} AND juliet_id={}".format(romeo_id,juliet_id))
        data=self.mycursor.fetchall()
        if len(data)!=0:
            return -1
        # else:
        #     try:
        #         self.mycursor.execute("INSERT INTO proposals (proposal_id,romeo_id,juliet_id) VALUES (NULL,{},{})".format(romeo_id,juliet_id))
        #         self.conn.commit()
        #         return 1
        #     except:
        #         return 0 
