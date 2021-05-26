import mysql.connector


def baseWP():
    base = mysql.connector.connect(
        host="",
        port="",
        user="",
        passwd="",
        database="")

    return base

def baseLocal():
    # base = mysql.connector.connect(
    #     host="",
    #     port="",
    #     user="",
    #     passwd="",
    #     database="")

    base = mysql.connector.connect(
        host="",
        port="",
        user="",
        passwd="",
        database="")

    return base