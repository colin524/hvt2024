import time
from time import sleep
import os
import sys
import random

def main():
    os.system("clear")
    print("Hack virus tool 2024 (version 1.0)")
    target = input("Enter hack target: ")
    print("starting hack...")
    time.sleep(0.5)
    print("getting target IP address...")
    time.sleep(random.randint(1, 5))
    ip_second = str(random.randint(10, 999))
    ip_third = str(random.randint(10, 999))
    ip_end = str(random.randint(10, 99))
    target_ip = "192." + ip_second + "." + ip_third + "." + ip_end
    print("Target IP address: " + target_ip + ", getting os...")
    time.sleep(random.randint(1, 5))
    os_type = random.randint(1, 5)
    os_version = 0
    if os_type == 1 or os_type == 4 or os_type == 5:
        oss = "Windows"
        os_version = str(random.randint(7, 11))
        if os_version == "9":
            os_version = "8.1"
    else:
        if os_type == 2:
            oss = "Mac OS"
        else:
            oss = "Linux"
        os_version = str((random.randint(50, 140) / 10))
    print("OS used: " + oss + " version " + os_version + ", starting attack...")
    time.sleep(random.randint(1, 5))

    def update_percentage(percentage):
        print(f"\rHacking : {percentage:.0f}%", end="", flush=True)

    def count():
        total_steps = 100  # You can set the total number of steps here
        for i in range(total_steps + 1):
            percentage = (i * 100) / total_steps
            update_percentage(percentage)
            wait = random.randint(1, 5000)
            divide = random.randint(1000, 10000)
            time.sleep(wait / divide)  # Simulating some work being done

    count()
    print("\n")
    print("hack done !")

    # Create and save results to a log file
    log_file_path = f"{target}-results.txt"
    if os.path.exists(log_file_path):
        user_response = input(f"The file {log_file_path} already exists. Do you want to replace it? (yes/no): ")
        if user_response.lower() != "yes":
            print("Results not saved.")
            input("Press enter to exit")
            return

    with open(log_file_path, "w") as log_file:
        log_file.write(f"Attack with Hack Virus Tool 2024 results\nTarget: {target}\n")
        log_file.write(f"Target IP Address: {target_ip}\n")
        log_file.write(f"Operating System: {oss} version {os_version}\n")
        log_file.write("Extracted data : readme.txt\n")
        log_file.write(f"Contents of readme.txt : Well, all of this was fake because this program is totally fake and you did not hack {target} (or even anybody), so please don't take it seriously. But if this was to scare your friends I gess I pranked you :) \nAlso all the data about the \"victim\" computer is fake and randomly generated. Please do not use this program or this data to harass anybody.")

    print("Hack successfull")
    print(f"Results file saved at: {log_file_path}")
    input("Press enter to exit")

main()
