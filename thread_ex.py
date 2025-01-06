import threading

def work():
    print("Working...")

t = threading.Thread(target = work)
t.start()
t.join() #Waits for thread to finish before moving on to next step in main program