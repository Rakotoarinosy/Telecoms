from ldap3 import Server,Connection,ALL
from outil_telecoms.settings import LDAP_DOMAIN

class Database :
    connection = None
    
    def __init__(self,username=None,password=None,**kwargs):
        print(Database.connection)
        try:
            server = Server(LDAP_DOMAIN,get_info=ALL)
            conn = Connection(server,auto_bind=True,user="{}\\{}".format("BASAN",username),password=password)
            Database.connection = conn
        except Exception as error:
            print("Error: Connexion not establised {}".format(error))
        self.connection = Database.connection
        
class Login:
    
    def authentification(self,username=None,password=None):
        try:
            db = Database(username=username,password=password)
            conn = db.connection
            if not conn.bind():
                print("error in bind")
            conn.search('DC=basan,DC=mg',"(&(objectClass=person)(sAMAcountName=" + username + "))",attributes=['*'])
        except Exception as error:
            return str(error)
        
        # user = Utilisateurs().checkUser(username)
        # if user is not None:
        #     conn.unbind()
        #     return user
        # return None 