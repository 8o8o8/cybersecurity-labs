import ipaddress

def subnet_calculator():
    user_input = input("Enter an IP network (example: 192.168.1.0/24): ")

    try:
        network = ipaddress.ip_network(user_input, strict=False)
        print(f"\n Network Information for {network}")
        print(f" Network address : {network.network_address}")
        print(f" Broadcast address : {network.broadcast_address}")
        print(f" Subnet mask : {network.netmask}")
        print(f" Prefix length : /{network.prefixlen}")
        print(f" Total addresses : {network.num_addresses}")

        if network.prefixlen <= 30:
            hosts = list(network.hosts())
            print(f" Usable hosts: {len(hosts)}")
            print(f" First host: {hosts[0]}")
            print(f" Last host: {hosts[-1]}")
        else:
            print(" No usable hosts in this subnet (prefix to large)")
    
    except ValueError:
        print("Invalid input. Please enter in CIDR notation (e.g., 192.168.1.0/24)")

if __name__ == "__main__":
    subnet_calculator()