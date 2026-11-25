def port_check(target_port):
    ports = ("22", "443", "8080", "3306", "5432")
    print(type(target_port))
    print(target_port.isdigit())
    is_port_open = target_port in ports
    if type(target_port).__name__ == 'str':
        print(f"Type of target port is { type(target_port).__name__ } and it's { target_port.isdigit() } digit")
        is_port_open = target_port in ports
        print(f"Status of target port {target_port} is {is_port_open}")
    #target_port = 8080
    if target_port in ports:
        print(f"Port {target_port} is open.")
        return is_port_open
    else:
        print(f"Port {target_port} is closed.")
        return False

is_open = False
while not is_open:
    port=input("Enter the target port number \n")
    if port.strip().lower() == 'exit':
        print("Stopping engine, Goodbye!!")
        break
    elif port.isdigit():
        is_open = port_check(port)
    else:
        print(f"You have given invalid input")
        break
    if is_open:
        print(f"Port { port } has been opened and the status is { is_open }")
    else:
        print(f"port has been closed and status of the port is {is_open}")
    print("@" * 40)
