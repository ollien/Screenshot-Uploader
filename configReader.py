class ConfigReader():
    def __init__(self,name="config.txt"):
        self.keys={}
        self.name = name
    #Read Keys from file
    def readKeys(self):
        keysFile=open(self.name,"r")
        fileLines=keysFile.readlines()
        keysFile.close()
        self.keys.clear()
        for item in fileLines:
            #If last char is \n
            if (item[-1]=='\n'):
                item=item[:-1]
            #If a commented line
            if (item[0]=='#'):
                continue
            #If a new line is the first char
            elif (item[0]=='\n'):
                continue
            else:
                #Get Position of equal sign
                pos=item.find('=')
                if pos != -1:
                    #Name of the key is [0:pos], Value of the key is [pos+1:-1] (Stripping the \n char at the end)
                    self.keys[item[0:pos]]=item[pos+1:]

    #Return the keys, read allows you to get the keys without re-reading the file.
    def getKeys(self,read=True):
        if read:
            self.readKeys()
        return self.keys
