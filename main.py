import sql

user = 'mastergandar'

def bug_report(func):
    def wrapped(arg1,arg2):
        try:
            assert func(arg1,arg2) == 6, "Must be 6"
        except Exception as error:
            print("Ошибка! Итоговое значение не совпадает!\nНа наши срервера будет отправлена информация об ошибке!")
            sql.curs.execute("INSERT INTO bug_report (id, users, err_code) VALUES (default, %s, %s);", (user, str(error)))
            sql.conn.commit()
            sql.curs.close()
            sql.conn.close()
            #print(user, str(error))
        finally:
            print("Sum = " + str(func(arg1,arg2)))
    return wrapped

@bug_report
def sum(a,b):
    y = a + b
    return y

if __name__ == "__main__":
    sum(4,5)