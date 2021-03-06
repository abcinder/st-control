import time
import serial
import io
import struct

dev = "/dev/ttyACM0"
#ser = serial.Serial(dev,9600,timeout=0.1,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)
ser = serial.Serial(dev, 9600)
time.sleep(0.1)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

INITIALIZED = False
MENU = False
DEMO = False
PIN = False
#print "Outside init"

while INITIALIZED == False:
    #temp = ser.readline()
    #if temp == "Soft Touch initialized.\r\n":
    #print "Not init"
    if ser.readline() == "1\r\n":
        time.sleep(0.5)
        ser.write("establish contact\r\n")
        time.sleep(0.5)
        #print 'contact'
        #sio.write(unicode("hello\n")
        #sio.flush()
        INITIALIZED = True
        print "INIT"
        #time.sleep(0.2)
        #ser.flushInput()
        #ser.flushOutput()
        #ser.write("\r\n")
        #time.sleep(1)
        #ser.write("hello\n")
        ser.flushInput()

while INITIALIZED:
    #print "INIT"
    time.sleep(0.5)
    if ser.inWaiting():
        #temp = ser.readline()
        #print "read line:", temp
        #if temp == "menu\r\n":
        if ser.readline() == "menu\r\n":
            MENU = True
            print "MENU"
        #if ser.readline() == "Soft Touch Demo\r\n":
            print "Soft Touch Demo"
            print "Enter 1 for demo."
            print "Enter 2 for pin."
            answer = int(raw_input('...'))
            #print str(answer) + '\r\n'
            #ser.write(str(answer) + '\r\n')
            ser.write(str(answer))
            
            time.sleep(0.5)
            
            while MENU:
                #print "MENU"
                #time.sleep(0.5)
                if ser.inWaiting():
                    temp = ser.readline()
                    print temp
                    time.sleep(0.5)
                    if temp == "1\r\n":
                        DEMO = True
                        print "DEMO"
                        #print "Demo: ", DEMO
                        #print "got 1"
                        
                        while DEMO:
                            #print "DEMO"
                            #time.sleep(0.5)
                            answer = raw_input('...')
                            #ser.flushOutput()
                            ser.write(str(answer) + '\r\n')
                            time.sleep(0.5)
                            if ser.inWaiting():
                                print ser.readline()
                        
                    elif temp == "2\r\n":
                        PIN = True
                        print "Pin: ", PIN
                        print "got 2"
                    else:
                        print "ERROR MENU CHOICE NOT 1 OR 2"