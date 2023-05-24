from random import choice
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad




def simpkey():
    this = 0
    while this <2:
        done = get_random_bytes(32)
        this  = this +1
        return done

salt = simpkey()

#remember to delete or comment out print(salt) if you don't want it to ever be decrypted!
#but keep this line in if you need to write it down and hand it off to someone!
print("salt: ",salt)

def confi():
    cnm = 0
    while cnm <2:
        AWE = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE = AWE.split()
        AWE1 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE1 = AWE1.split()
        AWE2 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE2 = AWE2.split()
        AWE3 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE3 = AWE3.split()
        AWE4 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE4 = AWE4.split()
        AWE5 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE5 = AWE5.split()
        AWE6 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE6 = AWE6.split()
        AWE7 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE7 = AWE7.split()
        AWE8 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE8 = AWE8.split()
        AWE9 = '~ ` ! @ # $ % ^ & * ( ) _ + = - [ ] { } : ; . , < > / ? \ | " " 1 2 3 4 5 6 7 8 9 0 q a z w s x e d c r f v t g b y h n u j m i k o l p Q A Z W S X E D C R F V T G B Y H N U J M I K O L P'
        AWE9 = AWE9.split()
        for x in range(0,2):
            axy = choice(AWE)+choice(AWE1)+choice(AWE2)+choice(AWE3)+choice(AWE4)+choice(AWE)+choice(AWE2)+choice(AWE4)+choice(AWE3)+choice(AWE)+choice(AWE1)+choice(AWE5)+choice(AWE6)+choice(AWE7)+choice(AWE8)+choice(AWE9)+choice(AWE6)+choice(AWE7)
            cnm = cnm +1
            return axy

password = str(confi())


#remember to delete or comment out print(password) if you don't want it to ever be decrypted!
#but keep this line in if you need to write it down and hand it off to someone!
print("password: ",password)

KEY = PBKDF2(password, salt, dkLen = 32)


#remember to delete or comment out print(KEY) if you don't want it to ever be decrypted!
#but keep this line in if you need to write it down and hand it off to someone!
print("Key: ",KEY)

message = b"WOOOOOOOOOOO!Change Message Here"

cipher = AES.new(KEY, AES.MODE_CBC)

data = cipher.encrypt(pad(message, AES.block_size))

with open("encrypt.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(data)
#NOTE: message will be saved in a binary file "encrypt.bin" remember to change this file name "NEWFILENAME.bin" each time you run this script or you just overwrite the file over and over again.
