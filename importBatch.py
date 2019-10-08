import MySQLdb.cursors
from sagendatabas import settings

dbHost = settings.DATABASES['default']['HOST']
dbName = settings.DATABASES['default']['NAME']
dbUser = settings.DATABASES['default']['USER']
dbPASSWORD = settings.DATABASES['default']['PASSWORD']

# TODO: should be replaced with django-ORM
conn = MySQLdb.connect(host = dbHost, user = dbUser, passwd = dbPASSWORD, db = dbName)
cursor = conn.cursor()
cursor.execute("SELECT id, accnr, borjar, slutar, uppgiften_ror FROM svenska_sagor.import_record where id is not null AND accnr is not null AND borjar is not null and slutar is not null and uppgiften_ror is not null")
for round in cursor:
    print(round)
    #duplicates = round[1].split(',')

    # Insert all rows
    cursorupdate = conn.cursor()
    # cursorupdate.execute("update placenames.cards set ortid = " + str(round[0])  + " where ortid = " + i)
    cursorupdate.close()
    for i in range(int(round[2]), int(round[3]) + 1):
        number = str(i).zfill(4)
        filename = str(round[1]) + '_' + number + '.jpg'
        print(filename)
        # print()
        val = int(i)

        # Insert all media
        cursor2 = conn.cursor()
        # cursor2.execute("SELECT ortname, alok, hid, sid FROM placenames.ortnamnt where ortid = ?", (val,))
        #for row in cursor2:
        #    print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3]) + ' ' + str(row[4]))
        cursor2.close()
cursor.close()
conn.close()
