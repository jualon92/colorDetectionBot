# Importing the Required Library
import pywhatkit
import env
# Defining the Phone Number and Message
phone_number = env.phone
message = "hola, este es un mensaje de prueba desde python"

# Sending the WhatsApp Message
pywhatkit.sendwhatmsg_instantly(phone_number, message)

# Displaying a Success Message
print("WhatsApp message sent!")