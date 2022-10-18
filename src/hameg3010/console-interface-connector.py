from device import Device


if __name__ == "__main__":
    hameg_device_handle = Device.connect_using_vid_pid(
        idVendor=0x0403, idProduct=0xED72
    )
    print(
        """
 /$$   /$$                                                    /$$$$$$  /$$$$$$
| $$  | $$                                                   /$$__  $$|_  $$_/
| $$  | $$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$       | $$  \__/  | $$  
| $$$$$$$$ |____  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$      | $$        | $$  
| $$__  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$      | $$        | $$  
| $$  | $$ /$$__  $$| $$ | $$ | $$| $$_____/| $$  | $$      | $$    $$  | $$  
| $$  | $$|  $$$$$$$| $$ | $$ | $$|  $$$$$$$|  $$$$$$$      |  $$$$$$/ /$$$$$$
|__/  |__/ \_______/|__/ |__/ |__/ \_______/ \____  $$       \______/ |______/
                                             /$$  \ $$                        
                                            |  $$$$$$/                        
                                             \______/                         """
    )
    print("by me")

    while True:
        x = input("command: ")
        resp = hameg_device_handle.send_await_resp(x)
        print(f"response: {resp[0]}")
        print(f"          {resp[1]}")