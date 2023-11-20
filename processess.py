#! /usr/bin/python3

import psutil

def list_processes():
    print(f'{"PID":<10} {"User":<10} {"Name":<10} {"CPU %":<10} {"Memory %":<10}')
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        print(f'{proc.info["pid"]:<10} {proc.info["username"]:<10} {proc.info["name"]:<10} {proc.info["cpu_percent"]:<10} {proc.info["memory_percent"]:<10}')

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f'Process with PID {pid} has been terminated.')
    except psutil.NoSuchProcess:
        print(f'No process found with PID: {pid}')

def search_processes(name):
    print(f'{"PID":<10} {"User":<10} {"Name":<10} {"CPU %":<10} {"Memory %":<10}')
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        if proc.info["name"] == name:
            print(f'{proc.info["pid"]:<10} {proc.info["username"]:<10} {proc.info["name"]:<10} {proc.info["cpu_percent"]:<10} {proc.info["memory_percent"]:<10}')

def get_process_info(pid):
    try:
        process = psutil.Process(pid)
        print(f'PID: {process.pid}, Name: {process.name()}, CPU Usage: {process.cpu_percent()}%, Memory Usage: {process.memory_percent()}%')
    except psutil.NoSuchProcess:
        print(f'No process found with PID: {pid}')

if __name__ == "__main__":
    while True:
        print("1. List all processes")
        print("2. Kill a process")
        print("3. Search for processes by name")
        print("4. Get process info")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_processes()
        elif choice == '2':
            pid = int(input("Enter the PID of the process to kill: "))
            kill_process(pid)
        elif choice == '3':
            name = input("Enter the name of the process to search: ")
            search_processes(name)
        elif choice == '4':
            pid = int(input("Enter the PID of the process to get info: "))
            get_process_info(pid)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

