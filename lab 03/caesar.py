class Caesar:
    def __init__(self):
        self._shift = None

    #getter for the shift value, denoted as key
    def get_key(self):
        return self._shift
    
    #setter
    def set_key(self,value):
        self._shift = value



    def encrypt(self, text):
        result = ''
        for char in text:
            if  char == ' ':    #leave the space
                result += ' '
            else:
                if char.isalpha():
                    if ord(char) >= 65 and ord(char) <= 90:
                        char = chr(ord(char) + 32)   #change the uppercase to lowercase
                    result += chr((ord(char) - 97 + self._shift) % 26 + 97)   #change the letters to unicode and shift it within letter range, the value that exceed the unicode range will be mod by 24. All are add with 96 to start from 'a'
                else:
                    result += chr((ord(char) + self._shift) % 1114112)   #if the character is not a letter, just shift it
        return result

    def decrypt(self, text):
        result = ''
        for char in text:
            if  char == ' ':    #leave the space
                result += ' '
            else:
                if char.isalpha():
                    if ord(char) >= 65 and ord(char) <= 90:
                        char = chr(ord(char) + 32)   #change the uppercase to lowercase
                    result += chr((ord(char) - 97 - self._shift) % 26 + 97)   #reverse the shift
                else:
                    result += chr((ord(char) - self._shift) % 1114112)   #if the character is not a letter, just reverse it
        return result
    

#test
cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt("hello WORLD!")); # prints “khoor zruog$”
print(cipher.decrypt("KHOOR zruog$")); #prints “hello world!”
cipher.set_key(6);
print(cipher.encrypt("zzz")); #prints “fff”
print(cipher.decrypt("FFF")); #prints “zzz”
cipher.set_key(-6); # Negative keys should be supported!
print(cipher.encrypt("FFF")); #prints “zzz”