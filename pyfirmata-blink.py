# Copyright (c) 2012, Fabian Affolter <fabian@affolter-engineering.ch>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of the pyfirmata team nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pyfirmata
from pyfirmata import Arduino, util






def menu():
    print '\nMenu: '
    print '1. Turn on/off individual point'
    print '2. Demos'
    print '3. See queue'
    print '4. See history'
    print '5. Check output buffer'
    print '6. Check input buffer'
    print '7. Advance queue'
    choice = None
    while choice == None:        
        try:
            choice = int(raw_input('...'))
        except ValueError:
            print '  ***Must enter an integer.'
            choice = None
            continue
    
        if choice == 1:
            raw_pin()
        elif choice == 2:
            raw_line()
        elif choice == 3:
            que.display()
        elif choice == 4:
            hist.display()
        elif choice == 5:
            buf.inside()
        elif choice == 6:
            pass
        elif choice == 7:
            que.execute()
        else:
            print '\n***Not a valid choice.\n'
            choice = None
            
def raw_pin():
    print 'Enter a pin and value:'
    pin = int(raw_input('pin: '))
    value = int(raw_input('value (1 or 0): '))
    if pin >= 2 and pin <= 13:
        board.digital[pin].write(value)
        board.pass_time(DELAY)
    elif pin >= 14 and pin <= 19:
        board.analog[pin-14].write(value)
        board.pass_time(DELAY)
    else:
        print "Invalid pin."
    #board.digital[pin].write(value)

    
    
    
    
    
    

DELAY = 0.5 # in seconds

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/ttyACM0'

# Creates a new board 
board = pyfirmata.Arduino(PORT)
#print pyfirmata.BOARDS['arduino']

#board.analog[0].mode = pyfirmata.PWM
#board.analog[1].mode = pyfirmata.OUTPUT
#board.analog[2].mode = pyfirmata.OUTPUT 
#board.analog[3].mode = pyfirmata.OUTPUT
#board.analog[4].mode = pyfirmata.OUTPUT
#board.analog[5].mode = pyfirmata.OUTPUT

pinA0 = board.get_pin('a:0:i')
pinA0.mode = pyfirmata.OUTPUT

#pinA0 = board.get_pin('a:0:i')
#pinA0.mode = pyfirmata.OUTPUT

board.analog[1].write(255)
#board.analog[1].write(0)
#board.analog[2].write(0)
#board.analog[3].write(0)
#board.analog[4].write(0)
#board.analog[5].write(255)




while True:
    menu()