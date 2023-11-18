# Importing the Required Library
import pywhatkit
import env 
import numpy as np
 

def send_message(message):
    # Defining the Phone Number and Message
    phone_number = env.phone
    message = "hola, soy un bot y estoy probando si puedo enviar mensajes de whatsapp desde python. Mensaje: " + message

    # Sending the WhatsApp Message
    pywhatkit.sendwhatmsg_instantly(phone_number, message,13, 12, 32)
    
    # Displaying a Success Message
    print("WhatsApp message sent!")