import time, serial, struct, sys

from serial import SerialException
dev_prefix = "/dev/ttyACM"
dev_num = 0
dev = dev_prefix + str(dev_num)
connected = False
while not connected:
    if len(sys.argv) == 1:
        try:
            ser = serial.Serial(dev, 9600, timeout=0)
            connected = True
            print dev
        except SerialException:
            #print 'SerialException'
            dev_num += 1
            dev = dev_prefix + str(dev_num)
    else:
        dev_num = sys.argv[1]
        print dev_num
        dev = dev_prefix + str(dev_num)
        try:
            ser = serial.Serial(dev, 9600, timeout=0)
            connected = True
            print dev
        except SerialException:
            print 'SerialException'
        
#dev = '/dev/ttyACM0'
#ser = serial.Serial(dev, 9600, timeout=0)
time.sleep(1)
ser.flushInput()
ser.flushOutput()

#menu = False

def lePack(n, l):
    """ Converts integer to bytes. If length after conversion
    is smaller than given as param returned value is right-filled
    with 0x00 bytes. Use Little-endian byte order."""
    return b''.join([chr((n >> ((l - i - 1) * 8)) % 256) for i in xrange(l)][::-1])

def leUnpack(byte):
    """ Converts byte string to integer. Use Little-endian byte order."""
    return sum([ord(b) << (8 * i) for i, b in enumerate(byte)])

def bePack(n, l):
    """ Converts integer to bytes. If length after conversion
    is smaller than given as param returned value is right-filled
    with 0x00 bytes. Use Big-endian byte order."""
    return b''.join([chr((n >> ((l - i - 1) * 8)) % 256) for i in xrange(l)])

def beUnpack(byte):
    """ Converts byte string to integer. Use Big-endian byte order."""
    return sum([ord(b) << (8 * i) for i, b in enumerate(byte[::-1])])

while 1:
    if ser.inWaiting():
        #print 'avail'
        #if int(ser.read()) == 0:
        temp = struct.unpack('c', ser.read())
        #print struct.unpack('c', ser.read())
        ##print temp
        #if struct.unpack('c', ser.read()) == 0:
        if temp == ('\x00',):
        #if struct.unpack('c', ser.read()) == ('\x00',):
            print "\nSoft Touch Menu:"
            print "(1) demo"
            print "(2) single pad control"
            ans = int(raw_input('...'))
            #print ans
            #ser.flushInput()
            ser.write(struct.pack('B', ans))
            #print struct.pack('B', ans)
            #time.sleep(1)
#menu = False
        #elif struct.unpack('c', ser.read()) == ('\x01',):
        elif temp == ('\x01',):
        #elif int(ser.read()) == 1:
            print "\nDemo started."
            ans = raw_input('Press any key and enter to stop.\n...')
            #ser.flushInput()
            ser.write(struct.pack('B', 0))
            print ""
            #menu = True
        #elif int(ser.read()) == 2:
        elif temp == ('\x02',):
            #print "\nEnter a pad (2-19) and value (0-1):"
            #print "ex: 5 1"
            #raw = raw_input('...')
            #print 'raw:', raw
            #pad = int(raw[0])
            #print 'pad:', pad
            #value = int(raw[2])
            #print 'value:', value
            print "\nEnter a pad (2-19):"
            pad = int(raw_input('...'))
            print "Enter a value (0-1):"
            #try:
            value = int(raw_input('...'))
            #ser.flushInput()
            ser.write(struct.pack('BB', pad, value))
            time.sleep(0.1)
            
            #print 'struct pad:', struct.pack('B', pad)
            #print 'struct value:', struct.pack('B', value)
            #print 'struct both:', struct.pack('BB', pad, value)
	    
            #while ser.inWaiting() == 0:
            #while not ser.inWaiting():
            #time.sleep(0.001)
            #print 'waiting for data'

            while ser.inWaiting() < 2:
                #print "Have", ser.inWaiting(), "bytes."
                time.sleep(0.01)

            #print "Bytes:", ser.inWaiting()
            #time.sleep(0.5) #delay until both bytes are here
            if ser.inWaiting() == 2:
                time.sleep(0.1)
            b1 = struct.unpack('c', ser.read())
            b2 = struct.unpack('c', ser.read())

            #print 'pad:', b1, ', value:', b2
            toggle = 'on'
            if beUnpack(b2) == 1:
                toggle = 'on'
            elif beUnpack(b2) == 0:
                toggle = 'off'
            else:
                toggle = 'a mystery'

            print '\nPad', beUnpack(b1), 'is now', toggle, '\b.'

            #print 'pad:', bytes.fromhex(b1).decode('utf-8'), ', value:', bytes.fromhex(b2).decode('utf-8')

            #print 'pad:', int(b1), ', value:', b2

            #print 'pad:', reduce(lambda rst, d: rst * 10 + d, b1), ', value:', reduce(lambda rst, d: rst * 10 + d, b2)

            #time.sleep(0.1)
            #print 'done sleeping'
                #while ser.inWaiting() == 0:
            #pass
            #if ser.inWaiting():
            #byte = struct.unpack('c', ser.read())
            #print byte
            #print 'Pad ' + struct.unpack('c', ser.read()) + ' toggled."


                #menu = True
        else:
            print temp
    #ser.flushInput() definitely not a flushInput right before we check inWaiting()