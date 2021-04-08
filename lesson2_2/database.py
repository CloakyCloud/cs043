class Simpledb:

    def __init__(self, file):
        self.file = file

    def __repr__(self):
        return("<" + self.__class__.__name__ + " file = " + self.file + ">" )
        
    #'''Insert info to file'''#
    
    
    
    def insert(self, key, value):
    #file is forced set to "dbinfo", key and value are inputs user provides#
    
        #simply opens or creates file if it does not exist
        #writes the input key and value on the same line seperated by a tab
        f = open(self.file, 'a')
        f.write(key + '\t' + value + '\n')
        f.close()
    
    
    
        '''Check for duplicate bag'''
    
    def check_for_duplicate(self, key, value):
        #file again forced set to "dbinfo"
        #key is the same grabbed from user
    
    
        #opens file and reads it to tempCheck
        #check if key user types in to add already exists
    
        f = open(file, 'r+')
        tempCheck = f.read()
        f.close()
    
        print(key)
        print(value)
    
        #checking if key already in use, if it is, start from begging
        if key in tempCheck:
            print('key already in use, please try again.')
            print()
           
            
            
    
        #if key is not in use, creates the new data in the db
        else:
            
            print('adding info')
            insert(file, key, value)
            print()
    
            print('New Database:')
            print()
            
            f = open(file, 'r')
            newFile = f.read()
            print(newFile)    
            f.close()
    
            return False
    
        
        '''Get info to add to file'''
    
    def grabInfo(self):
    
        #reads db file and prints info mostly for debugging purposes
        f = open(file, 'r')
        tempCheck = f.read()
        print(tempCheck)
    
    
        #get user key
        print('type your key:')
        global key
        key = input()
    
    #if user key has a '\' character we ask them to try again
    #this is to avoid issues in the code with special characters
    
        checkKey = True
        while checkKey == True:
            if '\\' in key:
                print('there cannot be a "\\" please try again:')
                key = input()
                checkKey == True
            else:
                checkKey == False
                break
    
    #ask for users value
        print('type your value:')
        global value
        value = input()
    
    
    #again to avoid character issues in code, prohibits values with '\' character
        
        checkValue = True
        while checkValue == True:
            if '\\' in value:
                print('there cannot be a "\\" please try again:')
                key = input()
                checkValue == True
            else:
                checkValue == False
                break
    
            
        '''Check for key in db by creating temp array for each line in db text file'''
    
    def search_for(self, key):
        print('checking for ' + key + ' in ' + self.file)
    
    
    #open file and readlines to checkMe#
    
        f = open(self.file, 'r')
        checkMe = f.readlines()
    
    #print output for debugging
        print(checkMe)
    
    #grabs amount of lines to use for final catch#
        amount = len(checkMe) 
        print(amount -1)
    
    #for each line, create a tempArray to differentiate between the key and value
    #on the same line of text
    
    
    #variable to use for loop to keep track of how many lines
    #have been searched
        count = 0
        
        for i in checkMe:
            print(count)
            print(amount)
            
            #printing each i for debugging
            print('Checking: ' + i + 'for: '+ key, end='')
    
            count += 1
            
            
            tempArray = i.split('\t')
            print(tempArray)
            print()
    #check if the key matches the one we are searching for
    
    #if the line we are going to check is over the amount of lines
    #that exist in the file, the key does not exist
            if tempArray[0] == key:
                #print('Key found. User assosiated with this Key is: ' + tempArray[1])
    
            
                
                return tempArray[1]
                break
                
                
    
    #if line we check matches the key, state so, get the value
    #assosiated with it and break the loop
            elif count == amount:
                #print('Key not found')
                return -402
                break
                
    
    
    #if we are not outside of the range of lines to check
    #and the line we are on does not match, then move to the next line
            
            
    
    '''delete key'''
    
    def edit_selected(self, key, value):
    
        #print('Enter the key to edit or change:')
        #oldKey = input()
        #print('Enter the new key this should be:')
        #newKey = input()
    
        #print('Enter the value that is to be assosiated with this')
        #value = input()
        #value = value + '\n'
    
        #open file and read to a tempData list#
        f = open(self.file, 'r')
        tempData = f.readlines()
        
        tempArray = []
    
        #read file to tempArray #
        for i in tempData:
            tempLine = i.split('\t')
            tempArray.append(tempLine)
    
        #debugging purposes, prints the temp data and temp array with key we are
        #looking for
        print(tempData)
        print(tempArray)
        print('looking for: ' + key)
        print()
    
    #variable to keep track of where we are in the array
        track = 0
        amount = len(tempArray)
        newData = ''
    
    
        print('begin looking for key to change')
        for i in tempArray:
    
            print(track)
            print(amount)
            checkMe = i[0]
            print(checkMe)
            print()
            
    
    
            
            if checkMe == key:
                print('key found, edit this one')
                track = int(track)
                print(track)
                print(tempArray[track])
    
                print(tempArray[track][0])
    
                #tempArray[track][0] = newKey
                tempArray[track][1] = value + '\n'
                
                #tempArray.replace(i[1], value)
    
                f = open(self.file, 'r')
                check = f.readlines()
                f.close()
                print('this is to check what is currently in the file')
                print(check)
                print()
    
                print('this is the new stuff we are gonna put into the file')
                print(tempArray)
                print()
    
                print('Deleting old data in file')
                f = open(self.file, 'w').close()
                
                
                
                
    
                for i in tempArray:
                    
                    print(i[0] + '\t' + i[1])
    
                    test = (i[0] + '\t' + i[1])
                    print('testing if we organized things correctly')
                    print(test)
    
                    print('Writing new line to the file')
                    f = open(self.file, 'a')
                    f.write(test)
    
                    f.close()
                        
                print('this is the new data')   
                print(newData)
                print()
                          
                
                print(tempArray)
                f.close()
                break
            elif track == amount-1:
                print('key not found')
                break
         
            else:
                track = track + 1
                continue
    
        
    
     #edit line of text in file#
    
    def delete_selected(self, key):
        
        #print('Enter key to delete from list:')
        #key = input()
    
        #open file and read to a tempData list#
        f = open(self.file, 'r')
        tempData = f.readlines()
        
        tempArray = []
    
    #read file to tempArray #
        for i in tempData:
            tempLine = i.split('\t')
            tempArray.append(tempLine)
    
        #debugging purposes, prints the temp data and temp array with key we are
        #looking for
        print(tempData)
        print(tempArray)
        print('looking for: ' + key)
        print()
    
    #variable to keep track of where we are in the array
        track = 0
        amount = len(tempArray)
        newData = ''
    
    
        print('begin looking for key to delete')
        for i in tempArray:
    
            print(track)
            print(amount)
            checkMe = i[0]
            print(checkMe)
            print()
            
    
    
            
            if checkMe == key:
                print('key found, delete this one')
                track = int(track)
                print(track)
                print(tempArray[track])
                tempArray.remove(i)
    
                f = open(self.file, 'r')
                check = f.readlines()
                f.close()
                print('this is to check what is currently in the file')
                print(check)
                print()
    
                print('this is the new stuff we are gonna put into the file')
                print(tempArray)
                print()
    
                print('Deleting old data in file')
                f = open(self.file, 'w').close()
                
                
    
                #Begin writing lines to just emptied file#
                for i in tempArray:
                    
                    print(i[0] + '\t' + i[1], end='')
    
                    test = (i[0] + '\t' + i[1])
                    print('testing if we organized things correctly')
                    print(test)
    
                    print('Writing new line to the file')
                    f = open(self.file, 'a')
                    f.write(test)
    
                    f.close()
                        
                print('this is the new data')   
                print(newData)
                print()
                #newData = tempArray.replace('[','').replace(']','')            
                
                print(tempArray)
                f.close()
                break
            elif track == amount-1:
                print('key not found')
                break
         
            else:
                track = track + 1
                continue
    #Prompt user for both key and value#
    def get_user_input(self):
        
        #print('Type your name:')
        global key
        key = input()
    
    
        #Check to make sure no unique chracters to prevent errors in code#
        checkKey = True
        while checkKey == True:
            if '\\' in key:
                print('there cannot be a "\\" please try again:')
                key = input()
                checkKey == True
            else:
                checkKey == False
                break
    
    
       # print('Type your phonenumber:')
        global value
        value = input()
    
    
        #Prevents unique characters that cause error in code#
        checkValue = True
        while checkValue == True:
            if '\\' in value:
                print('there cannot be a "\\" please try again:')
                key = input()
                checkValue == True
            else:
                checkValue == False
                break
    
    
    
    #This prompts user to type only the key#
    def get_key():
        #print('type the name:')
        global key
        key = input()
    
        #Check to make sure no unique chracters to prevent errors in code#
        checkKey = True
        while checkKey == True:
            if '\\' in key:
                print('there cannot be a "\\" please try again:')
                key = input()
                checkKey == True
            else:
                checkKey == False
                break
    
           
    
    #prompt user for just the value#
    def get_value(self):
         #print('type the name:')
        global value
        value = input()
        
        #Check to make sure no unique chracters to prevent errors in code#
        checkValue = True
        while checkValue == True:
            if '\\' in value:
                print('there cannot be a "\\" please try again:')
                value = input()
                checkValue == True
            else:
                checkValue == False
                break
    
        
    
db = Simpledb('recipes.txt')
#db.insert('relish', 'Pickled cucumber and sugar')
#db.insert('pesto', 'Basil and olive oil')
#db.search_for('pesto')
#db.delete_selected('pesto')
#db.edit_selected('relish', 'Pickled cucumber and sugar AND OREGANO')
print(db)
    
    
    
    
    
    
    
        
    
    
    
    
