import mysql.connector
from difflib import get_close_matches
con = mysql.connector.connect(
user = "ardit700_student", 
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
crsr = con.cursor()

query = crsr.execute("SELECT * FROM Dictionary")
wordSet = dict(crsr.fetchall())
wordList = wordSet.keys()

def translate(word):
    #print(type(wordSet))
    #print(wordSet)
    l = get_close_matches(word, wordList, 3, 0.7)
    word = word.lower()
    if word in wordSet:
        q = crsr.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = crsr.fetchall()
        return results
    elif word.title() in wordSet:
        q = crsr.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = crsr.fetchall()
        return results
    elif word.upper() in wordSet:
        q = crsr.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = crsr.fetchall()
        return results
    elif len(l) > 0:
        choice = input("Did you mean %s instead of %s (Y / N) : " % (l[0], word))
        print()
        if choice == "Y":
            q = crsr.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % l[0])
            results = crsr.fetchall()
            return results
        elif choice == "N":
            return "Oops the word doesn't exitst :( !! check it again!!"
        else:
            return "Sorry!!! unable to understand your entry"
    else:
        return "Oops the word doesn't exists :( !! Check it again!!"


def main():
    while True:
        word = input("\nEnter the word or '.' to exit : ")
        print()
        if word == '.':
            break
        else:
            res = translate(word)
            if isinstance(res, list):
                for i in res:
                    print(i[0])
                    print()
            else:
                print(res)
                print()
    print("***************Thank You!!!***************\n")

main()