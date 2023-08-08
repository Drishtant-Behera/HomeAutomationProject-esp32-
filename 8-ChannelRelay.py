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
        
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    
    conn.close()