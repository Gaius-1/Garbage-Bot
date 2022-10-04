# import necessary modules
from multiprocessing import Process
import serial
import time

# from shots import take_photo
from predict import predict_waste

ser = serial.Serial("COM4", 9600)

major_class = {"left": "biodegradable", "right": "non_biodegradable"}
biodegradable_class = ["food_waste", "wood_waste", "leaf_waste", "paper_waste"]
non_biodegradable_class = ["plastic_bags", "plastic_bottles", "ewaste", "metal_cans"]


def omega_bot():
    """ Send instruction to the Robotic Arm to move based on its prediction"""
    # waste_imgfile = take_photo()
    waste_imgfile = "./image.jpg"
    payload = predict_waste(waste_imgfile)
    # include exception
    if payload in biodegradable_class:
        # pass data to arduino for move to biodegradable
        data_tmp_1 = "biodegradable"
        if ser.is_open:
            ser.write(bytes(data_tmp_1, 'utf-8'))
        else:
            print("Serial Port not opening...")
        # print("Waiting for ACK...")
    elif payload in non_biodegradable_class:
        # pass data to arduino for move to non_biodegradable
        data_tmp_2 = "non_biodegradable"
        ser.write(bytes(data_tmp_2, 'utf-8'))
        # print("Waiting for ACK...")
    # ser.close()

    while True:
        print("Waiting for ACK...")

        data_from_arduino = ser.readline().decode('utf-8').strip()
        print(f"G: {data_from_arduino}")
        time.sleep(0.5)

        if len(data_from_arduino) >= 3:
            print(f"Returned from arduino: {data_from_arduino}")
            if data_from_arduino == "#ACK":
                print("ACK received...")
                break
    
# entry point
if __name__ == '__main__':
    omega_bot()
    time.sleep(1)


