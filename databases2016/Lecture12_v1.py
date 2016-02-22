# Lecture 12 BINF8211
# Written by: D. Andrew Carr
# February 18, 2016
# ###########################
# Example script:
# shows how mysql.connector attaches to MySql database
# shows how to simply create a table
# shows how to simply insert a row of data
# ############################

# import the connection
import mysql.connector

# Make database connection
config = {
  'user': 'DAC_icloud',
  'password': 'Temp1',
  'host': '127.0.0.1',
  'database': 'Lecture12_2',
  'raise_on_warnings': True,
}

# open the connection
cnx = mysql.connector.connect(**config)

#cnx.close()

cmd2 = "CREATE TABLE Fastqdata3 (\
    idFastq_data3 int(11), \
    Header varchar(150) DEFAULT NULL,\
    Sequence varchar(150) DEFAULT NULL,\
    Score varchar(150) DEFAULT NULL,\
    PRIMARY KEY (idFastq_data3)) ENGINE=InnoDB"

cursor = cnx.cursor()
cursor.execute(cmd2)


add_fastq = ("INSERT INTO Fastqdata3 "
               "(idFastq_data3, Header, Sequence, Score) "
               "VALUES (%s, %s, %s, %s)")


data_fastq = ('1', 'h.1', 'ATCAAGATGCATTGAC', 'lskdjfoalslls')

# Insert new employee
cursor.execute(add_fastq, data_fastq)


cnx.commit()

cursor.close()
cnx.close()
