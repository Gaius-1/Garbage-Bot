# import necessary modules
import serial
import schedule
import time

from Cortex.shots import take_photo
from predict import predict_waste

major_class = {"left": "biodegradable", "right": "non_biodegradable"}
biodegradable_class = ["food_waste", "wood_waste", "leaf_waste", "paper_waste"]
non_biodegradable_class = ["plastic_bags", "plastic_bottles", "ewaste", "metal_cans"]


def omega_bot():
    """ Send instruction to the Robotic Arm to move based on its prediction"""
    waste_imgfile = take_photo()
    payload = predict_waste(waste_imgfile)
    # include exception
    if payload in biodegradable_class:
        # pass data to arduino for move to biodegradable
        data_tmp_1 = "biodegradable"
        serial.write(bytes(data_tmp_1, 'utf-8'))
        print("Waiting for ACK...")
    elif payload in non_biodegradable_class:
        # pass data to arduino for move to non_biodegradable
        data_tmp_2 = "non_biodegradable"
        serial.write(bytes(data_tmp_2, 'utf-8'))
        print("Waiting for ACK...")
    
    while True:
        data_from_arduino = serial.readline().decode('utf-8').strip()
        time.sleep(0.5)

        if len(data_from_arduino) >= 3:
            print(f"Returned from arduino: {data_from_arduino}")
            if data_from_arduino == "#ACK":
                print("ACK received...")
                break
    
# entry point
if __name__ == '__main__':
    while True:
        # run repeated until interrupted by user or keyboard
        schedule.run_pending(omega_bot)
        time.sleep(1)


