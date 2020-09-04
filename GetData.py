# DB
import pymysql

# Conexion
# //////////////////////////////////////
from Settings import Conexion

def GetData ():
    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
            with connection.cursor() as cursor:
                # Read a single record
                #sql = "SELECT * FROM `Pichincha91` WHERE `Id` = %s"

                sql = "SELECT * FROM `Pichincha91` LIMIT 20"

                cursor.execute(sql) 
                result = cursor.fetchall()
                #print ("Resultado:", result)
                #TestID = int(result.get('Id'))
                #print ("Id", TestID)
                #input ()
                
    finally:
        connection.close()

    return result

