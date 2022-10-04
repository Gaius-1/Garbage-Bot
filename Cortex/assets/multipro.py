from multiprocessing import Process, Value
import time

def robot():
    print("Robot Initialized...")
    time.sleep(10)
    print("Robot at Rest...")

def service():
    print("Service Initialized...")
    time.sleep(2)
    print("Job1 Done...")
    time.sleep(2)
    print("Job2 Done...")
    time.sleep(3)
    print("Ended Service...")

if __name__ == "__main__":
    for i in range(2):
        p1 = Process(target=service)
        p2 = Process(target=robot)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("\n\n")
        time.sleep(0.2)

    print("whewww....")