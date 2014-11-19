import time
import serial
import io
import struct

dev = "/dev/ttyACM0"
#ser = serial.Serial(dev,9600,timeout=0.1,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)
ser = serial.Serial(dev, 9600)
#time.sleep(0.5)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

INITIALIZED = False

while INITIALIZED == False:
    #temp = ser.readline()
    #if temp == "Soft Touch initialized.\r\n":
    if ser.readline() == "Soft Touch initialized.\r\n":
        ser.write("Establish contact\r\n")
        #print 'contact'
        #sio.write(unicode("hello\n"))
        #sio.flush()
        INITIALIZED = True
        time.sleep(2)
        ser.flushInput()
        #ser.flushOutput()
        ser.write("hello\n")
        #time.sleep(1)
        #ser.write("hello\n")

while INITIALIZED:
    if ser.inWaiting():
        temp = ser.readline()
        if temp == "d\r\n":
        #if ser.readline() == "Soft Touch Demo\r\n":
            print "Soft Touch Demo"
            print "Enter 1 for demo."
            print "Enter 2 for pin."
            answer = raw_input('')
            ser.write(str(answer + '\n'))