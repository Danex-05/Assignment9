#! /usr/bin/python3

import os
import sys

def set_static(ip, netmask, gateway):
    config = f"""
    auto eth0
    iface eth0 inet static
    address {ip}
    netmask {netmask}
    gateway {gateway}
    """
    with open('/etc/network/interfaces', 'w') as f:
        f.write(config)
    os.system('service networking restart')

def set_dynamic():
    config = """
    auto eth0
    iface eth0 inet dhcp
    """
    with open('/etc/network/interfaces', 'w') as f:
        f.write(config)
    os.system('service networking restart')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./ipchange.py [static|dynamic] [ip] [netmask] [gateway]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == 'static':
        if len(sys.argv) != 5:
            print("Usage: python3 script.py static [ip] [netmask] [gateway]")
            sys.exit(1)
        ip = sys.argv[2]
        netmask = sys.argv[3]
        gateway = sys.argv[4]
        set_static(ip, netmask, gateway)
    elif mode == 'dynamic':
        set_dynamic()
    else:
        print("Invalid mode. Use 'static' or 'dynamic'.")

