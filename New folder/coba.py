import mindwave, time

headset = mindwave.Headset('COM4', '1425')
time.sleep(2)

headset.connect()
print "Connecting..."

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print "Retrying connect..."
print "Connected."

while True:
    #print "Attention: %s, Meditation: %s" % (headset.attention, headset.meditation)
    #print headset.serial_open()
    print "raw_value: %s" % (headset.raw_value)
    time.sleep(0.1)