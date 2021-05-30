import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host='localhost',user='root',password='',database='quizapp')
            self.mycursor=self.con.cursor()
            print("Connected to DB")
        except Exception as e:
            print(e)

    def check_login(self,email,password):
        self.mycursor.execute("SELECT *  FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
        data=self.mycursor.fetchall()

        return data

    def insert_user(self,name, email, password,college,dob,filename):
        try:
            if name=="" or email=="" or password=="" or college=="":
                pass
                #print("Fill the ragistration form properly")
            else:
                self.mycursor.execute("INSERT INTO users (user_id,name,email,password,college,DOB,dp) VALUES (NULL,'{}','{}','{}','{}','{}','{}')"
                                      .format(name,email,password,college,dob,filename))
                self.con.commit()
                return 1
        except BaseException as e:
            print(e)
            return 0

    def quiz_set(self,q_no):

        self.mycursor.execute("SELECT * FROM `quizset` WHERE q_no={}".format(q_no))
        question=self.mycursor.fetchall()

        return  question
    def fetch_questions(self,q_no):

        self.mycursor.execute("SELECT * FROM `quizset` WHERE q_no NOT LIKE {}".format(q_no))
        questions = self.mycursor.fetchall()
        return  questions

    def check_db(self,user_id):
        self.mycursor.execute("SELECT * FROM scoretable WHERE user_id LIKE {}".format(user_id))
        check=self.mycursor.fetchall()
        if  len(check)==0:
            return False
        else:
            return True

    def score_update(self,user_id,score):

        self.mycursor.execute("SELECT * FROM `quizset`")
        q_set=self.mycursor.fetchall()
        q_set_size=len(q_set)
        wrong=q_set_size-score
        check_return=self.check_db(user_id=user_id)

        if check_return:
            try:
                self.mycursor.execute(
                    "UPDATE scoretable SET score={},wrong={} WHERE user_id={}".format(score, wrong, user_id))
                self.con.commit()
            except Exception as e:
                print(e)
        else:
            try:
                self.mycursor.execute(
                    "INSERT INTO `scoretable` (`user_id`, `score`, `wrong`) VALUES ({},{},{})".format(user_id, score,
                                                                                                      wrong))
                self.con.commit()
            except Exception as e:
                print(e)

    def leader_board(self):

        self.mycursor.execute("SELECT name,score FROM users JOIN scoretable WHERE users.user_id=scoretable.user_id ORDER BY scoretable.score DESC")
        leaders=self.mycursor.fetchall()
        return leaders





#obj=DBhelper()