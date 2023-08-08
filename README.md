# Relays with Server Control on ESP32 - README

## **Introduction**

This repository provides the code and documentation for a relay module controlled by an ESP32 microcontroller and managed via a server-based interface. The ESP32 is a powerful Wi-Fi and Bluetooth-enabled microcontroller, allowing remote control and automation of various devices using relays. The relay module allows you to switch high-voltage appliances, lights, motors, and other electrical devices on and off safely. By connecting the ESP32 to a local server, you can control the relays conveniently from a web-based interface or even integrate it into your own smart home automation system.

## **Features**

**Any Amount of Channel Relay Control:** The ESP32 drives a different channels of relays, allowing you to control up to 16 separate electrical devices independently. You can edit the amount of relays by adding another line to the html code.

**Server-Based Control:** The ESP32 connects to a local server using Wi-Fi, enabling remote control of the relays from any device with a web browser and access to the server.

**Responsive Web Interface:** The server hosts a user-friendly web interface where you can toggle the relays on and off with a simple click or tap.

**Expandability:** The project's open-source nature allows you to modify and extend the codebase to integrate additional features or connect the ESP32 to cloud-based services for broader control options.

## **Getting Started**

**Hardware Setup:** Connect the 4-channel relay module to the ESP32 following the provided wiring diagram.

**Software Setup:** Install the necessary libraries and dependencies as specified in the documentation.

**Configure Wi-Fi Credentials:** Enter your Wi-Fi network credentials in the ESP32 code to enable it to connect to your local server.

**Server Setup:** Deploy the server code on your local network or cloud platform and configure it accordingly.

**Access the Interface:** Once everything is set up, open your web browser and navigate to the server's IP address. You should now see the interface to control the relays remotely.

## **Disclaimer**

This project deals with high-voltage electrical devices, which can be dangerous if not handled properly. Be cautious during the setup and always follow safety guidelines. The creators of this repository are not responsible for any damage or harm caused by improper use of the code or hardware. Use this project at your own risk.
