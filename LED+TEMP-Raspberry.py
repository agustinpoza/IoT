## CODIGO TEMP + LED Funcionando (Final, We did it)

import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

arduino = serial.Serial('/dev/ttyACM0', 9600)

class IOT():
    def __init__(self):
        cred = credentials.Certificate('/home/pi/Desktop/IoT/cred2.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://electronica-703.firebaseio.com/'
        })

        self.refHome = db.reference("Casa")
        #self.Inicial()
        self.refTemp = self.refHome.child("Temperatura")
        self.refLuz  = self.refHome.child("Luz")
        self.Enviar()
        
    def Inicial(self):
        self.refHome.set({
            "Luz": True,
            "Temperatura": True
            })

    def Enviar(self):
        while True:
            leer = self.refLuz.get()
            print (leer)
            if leer == True:
                Envio = 'A'
            else:
                Envio = 'a'

            arduino.write (Envio.encode ())
            self.EnviarTemp()

    def EnviarTemp(self):
        temp = arduino.readline()
        temperatura = temp.decode('utf-8').strip()
        self.refTemp.set(temperatura)

print ("Start!")
iot = IOT()