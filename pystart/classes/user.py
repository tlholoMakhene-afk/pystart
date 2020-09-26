class User:
    
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def displayUsername(self):
    print("Username: " + self.username)

  
  def populateUsers(self):
    Userlist = []
    Userlist.append(User('Tlholo','P@ssword'))
    Userlist.append(User('Ofentse','P@ssword'))
    Userlist.append(User('Tumisho','P@ssword'))
    return Userlist
  
  def validateUser(self):
     bFlag = False
     for i in self.populateUsers():
         if(i.username ==self.username):
             if(i.password == self.password):
                  bFlag = True
     return bFlag
 
    