import pymysql






def insert_data(nombre, apellido, telefono, mail, conexion=connect()):
    '''Agrega datos a la Base de Datos'''

    cursor = conexion.cursor()

    datos = (nombre, apellido, telefono, mail)

    sql = 'INSERT INTO contactos(nombre, apellido, telefono,mail) VALUES (%s, %s, %s, %s)'


def update_data(nom_buscado,nombre, apellido, telefono, mail,conexion=connect()):
    '''Actualiza un registro en la Base de datos'''
    cursor = conexion.cursor()
    datos = (nombre, apellido, telefono, mail, nom_buscado)
    sql = ('UPDATE contactos SET nombre = %s, apellido = %s, telefono= %s, mail=%s WHERE nombre= %s')
    try:
        cursor.execute(sql,datos)
        print("Datos actualizados con exito")
    except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrio un error al actualizar los datos:,", e)
    conexion.commit()
    conexion.close()


def delete_data(nom_buscado, conexion=connect()):
    '''Elimina datos de un registro en la Base de datos'''

    sql = 'DELETE FROM contactos WHERE nombre=%s'
    try:
        with conexion.cursor() as cursor:
            cursor.execute(sql, nom_buscado)
            print("Datos eliminados con exito")
    except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrio un error al eliminar los datos:,", e)
    conexion.commit()
    conexion.close()

def get_all_data(conexion=connect()):
    '''Lista todos los registros de la Base de Datos'''
    cursor = conexion.cursor()
    sql = 'SELECT * FROM contactos'
    try:
        cursor.execute(sql)
        records= cursor.fetchall()

        for row in records:
            if row == '':
                print("No hay contactos guardados")
            else:
                print('id:', row[0],'\n Nombre:',row[1], '\n Apellido:',row[2], '\n Telefono:',row[3], '\n E-mail:', row[4], "\n----------")
    except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error al leer los datos de la Base de datos", e)
    finally:
        conexion.close()
        cursor.close()
        print("Se cerro la conexion SQL")


def get_data(nombre):
    '''Busca un solo valor en la Base de datos'''
    try:
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='123456',
                                    db='agenda')
        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM contactos WHERE nombre=%s'
                cursor.execute(sql,nombre)
                listanombres=cursor.fetchall()
                for lista in listanombres:
                    print(lista)
        finally:
            conexion.close()
            print("hola mundito jijiji");
    except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Errror consultando la tabla de contactos:", e)

print("hola mundo");
print("hola mundo x2");