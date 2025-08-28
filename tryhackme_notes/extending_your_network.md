# Extending Your Network

## Port Forwarding
- Allows external devices to access services (e.g., web servers) inside a private network.  
- Without port forwarding, services are only accessible within the same intranet.   

Key Points:  
- Configured at the router.  
- Different from firewalls (which control what traffic is allowed once ports are open).  
- Enables private services to be made public.  

---

## Firewalls
- Control incoming/outgoing traffic, acting as border security.  
- Rules can filter based on source, destination, port, and protocol.  

Categories:  
- Stateful: Tracks connection state (e.g., TCP handshake). Resource-intensive but more secure.  
- Stateless: Uses static rules, less resource-intensive, less flexible. Often used for high-volume traffic filtering.  

OSI Layers: Operate mainly at Layers 3 and 4.  

---

## Virtual Private Network (VPN)
- Creates a secure tunnel between devices/networks over the Internet.  
- Forms a private “virtual network” across different geographical locations.  

Benefits:  
- Connects remote offices securely.  
- Protects data with encryption (useful on public Wi-Fi).  
- Provides privacy/anonymity (limited if VPN logs are kept).  
- Used in TryHackMe to safely access vulnerable machines.  

Common Technologies:  
- PPP / PPTP: Easy to configure, weak encryption.  
- IPsec: Strong encryption, harder to set up.  

---

## LAN Networking Devices

### Routers
- Connect networks and forward traffic between them.  
- Operate at OSI Layer 3.  
- Configurable for port forwarding, firewall rules, etc.  

Routing Path Factors: 
- Shortest path.  
- Most reliable path.  
- Medium speed (fiber vs copper).  

### Switches
- Dedicated devices that connect multiple machines via Ethernet.  

Types:  
- Layer 2 Switch: Uses MAC addresses, forwards frames.  
- Layer 3 Switch: Adds routing capabilities using IP addresses.  

VLAN Example:  
- VLANs (Virtual LANs) can separate traffic by department (e.g., Sales vs Accounting).  
- Devices on different VLANs can’t communicate with each other directly.  

---

## Quick Recap
- Port forwarding: Opens internal services to the Internet.  
- Firewalls: Enforce rules on traffic.  
- VPNs: Secure tunnels over public networks.  
- Routers/Switches: Forward traffic inside and between networks.  