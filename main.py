from machine import Pin
from utime import sleep

print("Hello, World!")

ledVerde = Pin(15, Pin.OUT)
ledVermelho = Pin(23, Pin.OUT)
ledAmarelo = Pin(4, Pin.OUT)

while True:
    ledVerde.on()
    print("Led Verde ON!")
    sleep(20)
    ledVerde.off()
    print("Led Verde OFF!")
    sleep(0.5)

    ledVermelho.on()
    print("Led Vermelho ON!")
    sleep(7)
    ledVermelho.off()
    print("Led Vermelho OFF!")
    sleep(0.5)

    ledAmarelo.on()
    print("Led Amarelo ON!")
    sleep(10)
    ledAmarelo.off()
    print("Led Amarelo OFF!")
    sleep(0.5)

