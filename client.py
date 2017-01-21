import socket
import sys


def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429


    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.connect((HOST, PORT))
            sock.sendall(bytes(data, "utf-8"))
            sfile = sock.makefile()
            rline = sfile.readline()
            retString = ""
            while rline:
                retString += rline.strip()
                rline = sfile.readline()
            # print(retString)
            return retString
    except:
        print("Socket Timed Out")




def subscribe(user, password):
    HOST, PORT = "191.237.6.138", 17429

    data=user + " " + password + "\nSUBSCRIBE\n"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(bytes(data, "utf-8"))
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
