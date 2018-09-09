import cx_Oracle as cx, datetime

def main():

    connection = cx.connect('algda/601908@cytosine.nl')
    cursor = connection.cursor()
    #tweet(connection,cursor)
    todaystweets(connection, cursor)
    #hashtag(connection,cursor)
    cursor.close()
    connection.close()

def tweet(connection,cursor):
    tekst = input("Tweet iets: \n")
    newtweet = """insert  into tweets(tekst) values('{}')""".format(tekst)
    cursor.execute(newtweet)
    connection.commit()

def todaystweets(connection, cursor):
    todaystweet = "select s.voornaam,to_char(t.datum,'YYYY-MM-DD'),to_char(t.datum,'HH24:MI'), t.tekst from studenten s, tweets t where t.studnr = s.studnr"
    cursor.execute(todaystweet)
    for value in cursor:
        if str(datetime.date.today()) == str(value[1]):
            print(value)
    connection.commit()

def hashtag(connection,cursor):
    hashtag = "select s.voornaam,to_char(t.datum,'YYYY-MM-DD'),to_char(t.datum,'HH24:MI'), t.tekst from studenten s, tweets t where t.studnr = s.studnr"
    cursor.execute(hashtag)
    for value in cursor:
        try:
            if "#tag" in value[3]:
                print(value)
        except TypeError:
            pass
    
main()
