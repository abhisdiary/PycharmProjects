import time
from datetime import datetime as dt

hosts_path_mac = r"/private/etc/hosts"  # use 'r' at the beginning when you write something like: \n
hosts_path_win = r"C:\Windows\System32\drivers\etc\hosts"
host_temp = "hosts"

redirect = "127.0.0.1"
website_lists = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          23):
        print("Working")
        with open(hosts_path_mac, 'r+') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Playing")
        with open(hosts_path_mac, "r+") as file:
            content = file.readlines()
            file.seek(0)  # refer to the Python Mega Course: 148. Implementing the second part
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)

            file.truncate()
    time.sleep(5)  # sleeps the code for 5 seconds
