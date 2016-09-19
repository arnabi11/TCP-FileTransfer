import socket
import easygui
from Tkinter import Tk
# from tkFileDialog import askopenfilename
import tkFileDialog
def getfile():
    Tk().withdraw()
    filename = tkFileDialog.asksaveasfile()
    s = str(filename)
    lst = s.split("'")
    return lst[1]
def Main():
    host = easygui.enterbox(msg = 'Enter Server/Host IP:', title = 'HOST')
    port = int(easygui.enterbox(msg = 'enter the port no to listen at: ',\
                            title = 'PORT'))
    
    

    s = socket.socket()
    s.connect((host,port))

    #filename = raw_input('Filename? ->')
    filename = easygui.enterbox(msg = 'FileName you want from the server and q in order to exit.'\
                                ,title = 'FILENAME ?')
    
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            fileSize = long(data[6:])
            #message = raw_input('File Exists, '+str(fileSize)+'Bytes, downoald?(Y/N)?')
            message = easygui.enterbox(msg = 'File Exists, '+str(fileSize)+'Bytes, download?(Y/N)?',\
                                       title = 'CONFIRM')
                                
                                
            if message == 'Y':
                s.send('OK')
                # file_on_pc = filename
                file_on_pc = getfile()
                f = open(file_on_pc, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv<fileSize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print '{0:.2f}'.format((totalRecv/float(fileSize))*100)+\
                          '% done'
                print 'Downloading is Complete'
                easygui.msgbox(msg = 'Downloading is complete', title = 'COMPLETE')
        else:
            easygui.messgbox(msg = 'File does not exist',title = 'ERROR')
            print 'File does not exists'
    s.send('CLOSE THE CONNECTION')
    s.close()

if __name__=='__main__':
    Main()
