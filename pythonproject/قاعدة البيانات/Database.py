import sqlite3

class Database:
    def __init__(self,path):
        self.path =path
        #5athyat path tdl 3ala mathar sqlite3
        self.connection =None
        #connection ka2en el etethal elly hynsha2 3nd eletethal bnga7
        self.connected = False
        #connected hwa mt3'er w yomathl 7alet el etesal bnga7
        self.connect()
        #l egra2 etesal 3nd en4a2 el nos5a database


    def connect(self):
        #fe python ynfz 2mr elly ta7t try w eza lm ynfz yntql l except
        try:
            self.connection =sqlite3.connect(self.path)
            self.connected =True
        except sqlite3.Error as e:
            print(e)
        return self.connection

    #yothabet el tab3 commit el ta3del ely tara2 3ala qa3det el byanat
    def commit (self):
        self.connection.commit()

    #el 2mr close y3'leq el database b3d el ta7qok mn el 2mr connect
    def close (self):
        if self.connected:
            self.connection.close()
        self.connected =False

#يتم إنشاء جدول من model& user








