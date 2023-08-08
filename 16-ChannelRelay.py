#Type your wifi ncredentials with caution, dont let anyone see :)

ssid = "Your wifi"
password = "Your password!"


#Attaching pins to relays

import machine
relay1 = machine.Pin(0,machine.Pin.OUT)
relay1.on()
relay2 = machine.Pin(4,machine.Pin.OUT)
relay2.on()
relay3 = machine.Pin(32,machine.Pin.OUT)
relay3.on()
relay4 = machine.Pin(2,machine.Pin.OUT)
relay4.on()
relay5 = machine.Pin(5,machine.Pin.OUT)
relay5.on()
relay6 = machine.Pin(18,machine.Pin.OUT)
relay6.on()
relay7 = machine.Pin(19,machine.Pin.OUT)
relay7.on()
relay8 = machine.Pin(21,machine.Pin.OUT)
relay8.on()
relay9 = machine.Pin(22,machine.Pin.OUT)
relay9.on()
relay10 = machine.Pin(23,machine.Pin.OUT)
relay10.on()
relay11 = machine.Pin(13,machine.Pin.OUT)
relay11.on()
relay12 = machine.Pin(12,machine.Pin.OUT)
relay12.on()
relay13 = machine.Pin(33,machine.Pin.OUT)
relay13.on()
relay14 = machine.Pin(27,machine.Pin.OUT)
relay14.on()
relay15 = machine.Pin(26,machine.Pin.OUT)
relay15.on()
relay16 = machine.Pin(25,machine.Pin.OUT)
relay16.on()


#Conecting and setting up wifi
import network

#Waiting for an available server to conect to
import time

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("Server found")

# Set the countdown duration
countdown_duration = 30

# Start the countdown timer
countdown_timer(countdown_duration)

# Searching for server
sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    sta.connect(ssid, password)
print('network config:', sta.ifconfig())


# Setting up the relay values for web server

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

# All the buttons functions for the web page

def web_page():
    if relay1.value()==1:
        relay1_state = 'OFF'
        print('relay1 is OFF')
    elif relay1.value()==0:
        relay1_state = 'ON'
        print('relay1 is ON')
        
    if relay2.value()==1:
        relay2_state = 'OFF'
        print('relay2 is OFF')
    elif relay2.value()==0:
        relay2_state = 'ON'
        print('relay2 is ON')
        
    if relay3.value()==1:
        relay3_state = 'OFF'
        print('relay3 is OFF')
    elif relay3.value()==0:
        relay3_state = 'ON'
        print('relay3 is ON')
        
    if relay4.value()==1:
        relay4_state = 'OFF'
        print('relay4 is OFF')
    elif relay4.value()==0:
        relay4_state = 'ON'
        print('relay4 is ON')
        
    if relay5.value()==1:
        relay5_state = 'OFF'
        print('relay5 is OFF')
    elif relay5.value()==0:
        relay5_state = 'ON'
        print('relay5 is ON')
        
    if relay6.value()==1:
        relay6_state = 'OFF'
        print('relay6 is OFF')
    elif relay6.value()==0:
        relay6_state = 'ON'
        print('relay6 is ON')
        
    if relay7.value()==1:
        relay7_state = 'OFF'
        print('relay7 is OFF')
    elif relay7.value()==0:
        relay7_state = 'ON'
        print('relay7 is ON')
        
    if relay8.value()==1:
        relay8_state = 'OFF'
        print('relay8 is OFF')
    elif relay8.value()==0:
        relay8_state = 'ON'
        print('relay8 is ON')
        
    if relay9.value()==1:
        relay9_state = 'OFF'
        print('relay9 is OFF')
    elif relay9.value()==0:
        relay9_state = 'ON'
        print('relay9 is ON')
        
    if relay10.value()==1:
        relay10_state = 'OFF'
        print('relay10 is OFF')
    elif relay10.value()==0:
        relay10_state = 'ON'
        print('relay10 is ON')
        
    if relay11.value()==1:
        relay11_state = 'OFF'
        print('relay11 is OFF')
    elif relay11.value()==0:
        relay11_state = 'ON'
        print('relay11 is ON')
        
    if relay12.value()==1:
        relay12_state = 'OFF'
        print('relay12 is OFF')
    elif relay12.value()==0:
        relay12_state = 'ON'
        print('relay12 is ON')
        
    if relay13.value()==1:
        relay13_state = 'OFF'
        print('relay13 is OFF')
    elif relay13.value()==0:
        relay13_state = 'ON'
        print('relay13 is ON')
        
    if relay14.value()==1:
        relay14_state = 'OFF'
        print('relay14 is OFF')
    elif relay14.value()==0:
        relay14_state = 'ON'
        print('relay14 is ON')
        
    if relay15.value()==1:
        relay15_state = 'OFF'
        print('relay15 is OFF')
    elif relay15.value()==0:
        relay15_state = 'ON'
        print('relay15 is ON')
        
    if relay16.value()==1:
        relay16_state = 'OFF'
        print('relay16 is OFF')
    elif relay16.value()==0:
        relay16_state = 'ON'
        print('relay16 is ON')
        
        
    # Setting the layout of the web page


    html_page = """   
      <html>   
      <head>   
       <meta content="width=device-width, initial-scale=1" name="viewport"></meta>   
      </head>   
      <body>   
        <center><h2>ESP32 Web Server in MicroPython </h2></center>   
        <center>   
         <form>   
          <button name="RELAY1" type="submit" value="0"> RELAY1 ON </button>   
          <button name="RELAY1" type="submit" value="1"> RELAY1 OFF </button>
          <center>
          <button name="RELAY2" type="submit" value="0"> RELAY2 ON </button>   
          <button name="RELAY2" type="submit" value="1"> RELAY2 OFF </button>
          <center>
          <button name="RELAY3" type="submit" value="0"> RELAY3 ON </button>   
          <button name="RELAY3" type="submit" value="1"> RELAY3 OFF </button>
          <center>
          <button name="RELAY4" type="submit" value="0"> RELAY4 ON </button>   
          <button name="RELAY4" type="submit" value="1"> RELAY4 OFF </button>
          <center>
          <button name="RELAY5" type="submit" value="0"> RELAY5 ON </button>   
          <button name="RELAY5" type="submit" value="1"> RELAY5 OFF </button>
          <center>
          <button name="RELAY6" type="submit" value="0"> RELAY6 ON </button>   
          <button name="RELAY6" type="submit" value="1"> RELAY6 OFF </button>
          <center>
          <button name="RELAY7" type="submit" value="0"> RELAY7 ON </button>   
          <button name="RELAY7" type="submit" value="1"> RELAY7 OFF </button>
          <center>
          <button name="RELAY8" type="submit" value="0"> RELAY8 ON </button>   
          <button name="RELAY8" type="submit" value="1"> RELAY8 OFF </button>
          <center>
          <button name="RELAY9" type="submit" value="0"> RELAY9 ON </button>   
          <button name="RELAY9" type="submit" value="1"> RELAY9 OFF </button>
          <center>
          <button name="RELAY10" type="submit" value="0"> RELAY10 ON </button>   
          <button name="RELAY10 type="submit" value="1"> RELAY10 OFF </button>
          <center>
          <button name="RELAY11" type="submit" value="0"> RELAY11 ON </button>   
          <button name="RELAY11" type="submit" value="1"> RELAY11 OFF </button>
          <center>
          <button name="RELAY12" type="submit" value="0"> RELAY12 ON </button>   
          <button name="RELAY12" type="submit" value="1"> RELAY12 OFF </button>
          <center>
          <button name="RELAY13" type="submit" value="0"> RELAY13 ON </button>   
          <button name="RELAY13" type="submit" value="1"> RELAY13 OFF </button>
          <center>
          <button name="RELAY14" type="submit" value="0"> RELAY14 ON </button>   
          <button name="RELAY14" type="submit" value="1"> RELAY14 OFF </button>
          <center>
          <button name="RELAY15" type="submit" value="0"> RELAY15 ON </button>   
          <button name="RELAY15" type="submit" value="1"> RELAY15 OFF </button>
          <center>
          <button name="RELAY16" type="submit" value="0"> RELAY16 ON </button>   
          <button name="RELAY16" type="submit" value="1"> RELAY16 OFF </button>
         </form>   
        </center>   
        <center><p>RELAY1 is now <strong>""" + relay1_state + """</strong>.</p></center>
        <center><p>RELAY2 is now <strong>""" + relay2_state + """</strong>.</p></center>
        <center><p>RELAY3 is now <strong>""" + relay3_state + """</strong>.</p></center>
        <center><p>RELAY4 is now <strong>""" + relay4_state + """</strong>.</p></center>
        <center><p>RELAY5 is now <strong>""" + relay5_state + """</strong>.</p></center>
        <center><p>RELAY6 is now <strong>""" + relay6_state + """</strong>.</p></center>
        <center><p>RELAY7 is now <strong>""" + relay7_state + """</strong>.</p></center>
        <center><p>RELAY8 is now <strong>""" + relay8_state + """</strong>.</p></center>
        <center><p>RELAY9 is now <strong>""" + relay9_state + """</strong>.</p></center>
        <center><p>RELAY10 is now <strong>""" + relay10_state + """</strong>.</p></center>
        <center><p>RELAY11 is now <strong>""" + relay11_state + """</strong>.</p></center>
        <center><p>RELAY12 is now <strong>""" + relay12_state + """</strong>.</p></center>
        <center><p>RELAY13 is now <strong>""" + relay13_state + """</strong>.</p></center>
        <center><p>RELAY14 is now <strong>""" + relay14_state + """</strong>.</p></center>
        <center><p>RELAY15 is now <strong>""" + relay15_state + """</strong>.</p></center>
        <center><p>RELAY16 is now <strong>""" + relay16_state + """</strong>.</p></center>

      </body>   
      </html>"""  
    return html_page


#Socket request

while True:
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
    
    request=conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    request = str(request)
    
    relay1_on = request.find('/?RELAY1=1')
    relay1_off = request.find('/?RELAY1=0')
    
    relay2_on = request.find('/?RELAY2=1')
    relay2_off = request.find('/?RELAY2=0')
    
    relay3_on = request.find('/?RELAY3=1')
    relay3_off = request.find('/?RELAY3=0')
    
    relay4_on = request.find('/?RELAY4=1')
    relay4_off = request.find('/?RELAY4=0')
    
    relay5_on = request.find('/?RELAY5=1')
    relay5_off = request.find('/?RELAY5=0')
    
    relay6_on = request.find('/?RELAY6=1')
    relay6_off = request.find('/?RELAY6=0')
    
    relay7_on = request.find('/?RELAY7=1')
    relay7_off = request.find('/?RELAY7=0')
    
    relay8_on = request.find('/?RELAY8=1')
    relay8_off = request.find('/?RELAY8=0')
    
    relay9_on = request.find('/?RELAY9=1')
    relay9_off = request.find('/?RELAY9=0')
    
    relay10_on = request.find('/?RELAY10=1')
    relay10_off = request.find('/?RELAY10=0')
    
    relay11_on = request.find('/?RELAY11=1')
    relay11_off = request.find('/?RELAY11=0')
    
    relay12_on = request.find('/?RELAY12=1')
    relay12_off = request.find('/?RELAY12=0')
    
    relay13_on = request.find('/?RELAY13=1')
    relay13_off = request.find('/?RELAY13=0')
    
    relay14_on = request.find('/?RELAY14=1')
    relay14_off = request.find('/?RELAY14=0')
    
    relay15_on = request.find('/?RELAY15=1')
    relay15_off = request.find('/?RELAY15=0')
    
    relay16_on = request.find('/?RELAY16=1')
    relay16_off = request.find('/?RELAY16=0')
    
    
#Recieving input from users
    
    if relay1_on == 6:
        print('RELAY1 ON')
        print(str(relay1_on))
        relay1.value(1)
    elif relay1_off == 6:
        print('RELAY1 OFF')
        print(str(relay1_off))
        relay1.value(0)
        
    if relay2_on == 6:
        print('RELAY2 ON')
        print(str(relay2_on))
        relay2.value(1)
    elif relay2_off == 6:
        print('RELAY2 OFF')
        print(str(relay2_off))
        relay2.value(0)
        
    if relay3_on == 6:
        print('RELAY3 ON')
        print(str(relay3_on))
        relay3.value(1)
    elif relay3_off == 6:
        print('RELAY3 OFF')
        print(str(relay3_off))
        relay3.value(0)
        
    if relay4_on == 6:
        print('RELAY4 ON')
        print(str(relay4_on))
        relay4.value(1)
    elif relay4_off == 6:
        print('RELAY4 OFF')
        print(str(relay4_off))
        relay4.value(0)
        
    if relay5_on == 6:
        print('RELAY5 ON')
        print(str(relay5_on))
        relay5.value(1)
    elif relay5_off == 6:
        print('RELAY5 OFF')
        print(str(relay5_off))
        relay5.value(0)
        
    if relay6_on == 6:
        print('RELAY6 ON')
        print(str(relay6_on))
        relay6.value(1)
    elif relay6_off == 6:
        print('RELAY6 OFF')
        print(str(relay6_off))
        relay6.value(0)
        
    if relay7_on == 6:
        print('RELAY7 ON')
        print(str(relay7_on))
        relay7.value(1)
    elif relay7_off == 6:
        print('RELAY7 OFF')
        print(str(relay7_off))
        relay7.value(0)
        
    if relay8_on == 6:
        print('RELAY8 ON')
        print(str(relay8_on))
        relay8.value(1)
    elif relay8_off == 6:
        print('RELAY8 OFF')
        print(str(relay8_off))
        relay8.value(0)
        
    if relay9_on == 6:
        print('RELAY9 ON')
        print(str(relay9_on))
        relay9.value(1)
    elif relay9_off == 6:
        print('RELAY9 OFF')
        print(str(relay9_off))
        relay9.value(0)
        
    if relay10_on == 6:
        print('RELAY10 ON')
        print(str(relay10_on))
        relay10.value(1)
    elif relay10_off == 6:
        print('RELAY10 OFF')
        print(str(relay10_off))
        relay10.value(0)
        
    if relay11_on == 6:
        print('RELAY11 ON')
        print(str(relay11_on))
        relay11.value(1)
    elif relay11_off == 6:
        print('RELAY11 OFF')
        print(str(relay11_off))
        relay11.value(0)
        
    if relay12_on == 6:
        print('RELAY4 ON')
        print(str(relay4_on))
        relay12.value(1)
    elif relay12_off == 6:
        print('RELAY12 OFF')
        print(str(relay12_off))
        relay12.value(0)
        
    if relay13_on == 6:
        print('RELAY13 ON')
        print(str(relay13_on))
        relay13.value(1)
    elif relay13_off == 6:
        print('RELAY13 OFF')
        print(str(relay13_off))
        relay13.value(0)
        
    if relay14_on == 6:
        print('RELAY14 ON')
        print(str(relay14_on))
        relay14.value(1)
    elif relay14_off == 6:
        print('RELAY14 OFF')
        print(str(relay14_off))
        relay14.value(0)
        
    if relay15_on == 6:
        print('RELAY15 ON')
        print(str(relay15_on))
        relay15.value(1)
    elif relay15_off == 6:
        print('RELAY15 OFF')
        print(str(relay15_off))
        relay15.value(0)
        
    if relay16_on == 6:
        print('RELAY16 ON')
        print(str(relay16_on))
        relay16.value(1)
    elif relay16_off == 6:
        print('RELAY16 OFF')
        print(str(relay16_off))
        relay16.value(0)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    
    conn.close()