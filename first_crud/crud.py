import mysql.connector 

#
 
connexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python'
  
)

#create

def create_user(name,email):
    cursor=connexion.cursor()
    cursor.execute("""
                   INSERT INTO user(name,mail)
                   VALUES(%s,%s)
                   """,(name,email))
    connexion.commit()
    print("connexion ok")
    
   

create_user("random","r@gmail.com")

#read

def read_user():
    cursor=connexion.cursor()
    cursor.execute("""SELECT * FROM user""")
    for(id,name,email) in cursor:
        print(f"Id:{id},Nom:{name},Emai:{email}")
read_user()

#update 

def update_user(id,email):
     cursos=connexion.cursor()
     cursos.execute("""
                        UPDATE user
                        SET mail=%s
                        WHERE id=%s
                        """,(email, id))
     connexion.commit()
     print(f"utilisateur {id} à bien modifié son profile")

update_user(16,"random16@gmail.com")

#delete
 
def delete_user(id):
     cursor = connexion.cursor()
     cursor.execute("""
                                   DELETE FROM user
                                   WHERE id = %s
                                   """, (id,))
     connexion.commit()
     print(f"L'utilisateur {id} a été supprimé")

delete_user(4)