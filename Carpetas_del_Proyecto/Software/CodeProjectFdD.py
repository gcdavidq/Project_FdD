import RPi.GPIO as GPIO
import time
import os
import cv2
import base64
import requests
import pygame
import signal 
import subprocess

GPIO.setwarnings(False)  # Desactiva las advertencias

ultrasonic_sensor_trig = 25
ultrasonic_sensor_echo = 6
pin_izquierda = 17
pin_derecha = 27
ultrasonic_sensor_trig2 = 5
ultrasonic_sensor_echo2 = 16
pin_izquierda2 = 26
pin_derecha2 = 22
pin_buzzer = 21


GPIO.setmode(GPIO.BCM)
GPIO.setup(ultrasonic_sensor_trig, GPIO.OUT)
GPIO.setup(ultrasonic_sensor_echo, GPIO.IN)
GPIO.setup(pin_izquierda, GPIO.OUT)
GPIO.setup(pin_derecha, GPIO.OUT)
GPIO.setup(ultrasonic_sensor_trig2, GPIO.OUT)
GPIO.setup(ultrasonic_sensor_echo2, GPIO.IN)
GPIO.setup(pin_izquierda2, GPIO.OUT)
GPIO.setup(pin_derecha2, GPIO.OUT)
GPIO.setup(pin_buzzer, GPIO.OUT)


# Define una función para mover el motor hacia adelante
def mover_adelante():
    GPIO.output(pin_izquierda, GPIO.HIGH)
    GPIO.output(pin_derecha, GPIO.LOW)

# Define una función para mover el motor hacia atrás
def mover_atras():
    GPIO.output(pin_izquierda, GPIO.LOW)
    GPIO.output(pin_derecha, GPIO.HIGH)

# Define una función para detener el motor
def detener_motor():
    GPIO.output(pin_izquierda, GPIO.LOW)
    GPIO.output(pin_derecha, GPIO.LOW)

# Define una función para mover el motor hacia adelante
def mover_adelante_segundo():
    GPIO.output(pin_izquierda2, GPIO.HIGH)
    GPIO.output(pin_derecha2, GPIO.LOW)

# Define una función para mover el motor hacia atrás
def mover_atras_segundo():
    GPIO.output(pin_izquierda2, GPIO.LOW)
    GPIO.output(pin_derecha2, GPIO.HIGH)

# Define una función para detener el motor
def detener_motor_segundo():
    GPIO.output(pin_izquierda2, GPIO.LOW)
    GPIO.output(pin_derecha2, GPIO.LOW)
    
    
def activar_buzzer():
    GPIO.output(pin_buzzer, GPIO.HIGH)

# Función para desactivar el buzzer
def desactivar_buzzer():
    GPIO.output(pin_buzzer, GPIO.LOW)


def detectar_objeto(ultrasonic_sensor_trig, ultrasonic_sensor_echo):
    GPIO.output(ultrasonic_sensor_trig, False)
    time.sleep(0.5)

    GPIO.output(ultrasonic_sensor_trig, True)
    time.sleep(0.00001)
    GPIO.output(ultrasonic_sensor_trig, False)

    start_time = time.time()
    end_time = time.time()

    while GPIO.input(ultrasonic_sensor_echo) == 0:
        start_time = time.time()

    while GPIO.input(ultrasonic_sensor_echo) == 1:
        end_time = time.time()

    duration = end_time - start_time
    distance = (duration * 34000) / 2  # Velocidad del sonido en cm/s
    return distance  # Devuelve la distancia medida

def detectar_segundo_objeto(ultrasonic_sensor_trig, ultrasonic_sensor_echo):
    GPIO.output(ultrasonic_sensor_trig2, False)
    time.sleep(0.5)

    GPIO.output(ultrasonic_sensor_trig2, True)
    time.sleep(0.00001)
    GPIO.output(ultrasonic_sensor_trig2, False)

    start_time2 = time.time()
    end_time2 = time.time()

    while GPIO.input(ultrasonic_sensor_echo2) == 0:
        start_time2 = time.time()

    while GPIO.input(ultrasonic_sensor_echo2) == 1:
        end_time2 = time.time()

    duration2 = end_time2 - start_time2
    distance2 = (duration2 * 34000) / 2  # Velocidad del sonido en cm/s
    return distance2  # Devuelve la distancia medida


def capture_image():
    cam = cv2.VideoCapture(0)  # Cámara para el contenedor de botellas
    ret, frame = cam.read()
    if ret:
        image_directory = "/home/joota/Desktop/imagenes_botella"
        file_name = "photo.jpg"
        image_path = os.path.join(image_directory, file_name)
        cv2.imwrite(image_path, frame)
        print("Image captured and saved to", image_path)
        return image_path
    else:
        print("Error capturing the image.")
        return None

def call_api(image_path):
    if image_path is None:
        return None

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
	
    api_key = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    prompt_text = (
        "Please analyze the image provided and identify each item ingresed."
        "Decide if the items are made of plastic or not(bottle), if it are, categorize the items based on the following guidelines:\n"
        "1. Plastic: For items are made for plastic like bottles of drink.\n"
        "2. No plastic: Anything item that are made of any type of material that are not made for plastic.\n"
        "If the image contains multiple different items, categorize them collectively as No plastic (2). "
        "If all items are of the same type, categorize them according to the appropriate categorize. "
        "In cases of uncertainty or non-identifiable items, label these as 'NotSure' and categorize them as Non-Recyclable Waste (2).\n\n"
        "If there are doubts or non-recognizable items, include 'NotSure' in the list. "
        "For example:\n"
        "- '2: Papel higienico'\n"
        "- '1: Botella de agua mineral'\n"
        "- '2: bolsa de galleta'\n"
        "- '1: Gaseosa, botella vacia'\n"
        "This approach will assist in sorting the waste correctly, especially in cases with multiple items or uncertainty."
        "Respond ONLY with the number of the bin where the items should be placed, without any additional text. "
        "For example, respond with '1' or '2' based on the categorization.\n\n"
        "This format is critical for the automation process in the waste sorting system.")

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    response_data = response.json()
    content = response_data["choices"][0]["message"]["content"]
    bin_num = int(content)
    return bin_num

# Función para mostrar un mensaje en pantalla completa
def mostrar_mensaje_pantalla(mensaje):
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    font = pygame.font.Font(None, 36)
    text = font.render(mensaje, True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(4000)  # Mostrar el mensaje durante 5 segundos
    pygame.quit()

def mostrar_mensaje_inicio():
    pygame.init()
    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Acerque su botella a la box cam", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.update()

def ejecutar_juegos_retro():
    timeout_s =10

    try:
        proceso_retropie = subprocess.Popen(["emulationstation"])

        proceso_retropie.wait(timeout=timeout_s)
        
    except subprocess.TimeoutExpired:
        
        
        os.killpg(os.getpgid(proceso_retropie.pid), signal.SIGTERM)


mostrar_mensaje_inicio()

while True:
    distance = detectar_objeto(ultrasonic_sensor_trig, ultrasonic_sensor_echo)
    if distance < 6:
        mover_adelante()
        time.sleep(1)
        
        # Detenerse por 3 segundos
        detener_motor()
        time.sleep(3)
        
        # Mover hacia atrás durante 2 segundos
        mover_atras()
        time.sleep(1)
        
        # Detener el motor
        detener_motor()
        distance2 = detectar_segundo_objeto(ultrasonic_sensor_trig2, ultrasonic_sensor_echo2)  # Se detecta el segundo objeto aquí
        
        if distance2 < 11:
            image_path = capture_image()
            bin_number = call_api(image_path)
            print(bin_number)
            
            if bin_number == 1:
                mover_atras_segundo()  # SUELTA
                time.sleep(1.2)
                
                detener_motor_segundo()
                time.sleep(2)
                                
                mover_adelante_segundo() #PRESIONA
                time.sleep(1.2)
                
                detener_motor_segundo()
                
                ejecutar_juegos_retro()
                
            elif bin_number == 2:
                # Activar el buzzer
                activar_buzzer()
                time.sleep(4)  # Mantener el buzzer activado durante 5 segundos
                desactivar_buzzer()  # Desactivar el buzzer después de 5 segundos
                
                mensaje = "NO debes colocar este objeto en el contenedor"
                print("Mostrar mensaje en pantalla completa...")
                mostrar_mensaje_pantalla(mensaje)