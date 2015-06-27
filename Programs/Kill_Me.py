import time

kill = input("Kill me?:")
if kill in ["y","Y",'yes', 'Yes']:
    print("Thank you.")
else:
    while True:
        print ("Kill me.")
        time.sleep(1)
