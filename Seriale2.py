import serial

    
ser = serial.Serial(
    port='COM3',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1000)
ser.isOpen()
print("connected to: " + ser.portstr)
input("Press Enter to continue...")

data=[0x41,0x41,0x41,0x41,0x41,0x41,0x41,0x41,0x71,0x08,0x00,0x08]



print (serial.to_bytes(data))
ser.write(serial.to_bytes(data))


seq = []
count = 0 
        
while True:
        try:
            for c in ser.read():
                seq.append(chr(c)) #convert from ANSII
                joined_seq = ''.join(str(v) for v in seq) #Make a string from array

            if chr(c) == '\n':
                print("Line " + str(count) + ': ' + joined_seq)
                seq = []
                joined_seq=''
                count += 1
                break
        except Exception as e:
            print(e)
            ser.close()


    
input("Press Enter to continue...")
ser.close()
