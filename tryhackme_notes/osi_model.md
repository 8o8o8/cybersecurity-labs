# TryHackMe – OSI Model Notes

## Overview
The Open Systems Interconnection (OSI) model defines seven layers, each with different responsibilities.  
Encapsulation occurs when information is wrapped with additional headers/trailers as it moves down the layers; decapsulation happens in reverse.

7 Application
6 Presentation
5 Session
4 Transport
3 Network
2 Data Link
1 Physical

---

## 1. Physical Layer
- Concerned with hardware and physical transmission.  
- Uses **electrical signals** (or light/RF) to transmit bits in binary.  
- Devices: cables, connectors, physical NIC interface.  

---

## 2. Data Link Layer
- Handles **physical addressing** via **MAC addresses**.  
- Adds the MAC address of the receiving endpoint.  
- MAC is burned into NIC hardware (though it can be spoofed).  
- Devices: **switches, bridges, NICs**.  

---

## 3. Network Layer
- Handles **routing** and **re-assembly** of data.  
- Uses **IP addresses** (e.g., 192.168.1.100).  
- Routing decisions: shortest path, reliability, medium type (copper vs fiber).  
- Example protocols: **OSPF, RIP**.  
- Devices: **routers, L3 switches**.  

---

## 4. Transport Layer
- Provides **end-to-end delivery** with either **TCP** or **UDP**.

**TCP (Transmission Control Protocol):**
- Reliable, connection-oriented, error-checked.  
- Synchronization prevents flooding.  
- Disadvantage: slower, can bottleneck connections.

**UDP (User Datagram Protocol):**
- Faster, connectionless, no error checking.  
- Useful for streaming, ARP, DHCP.  
- Disadvantage: unreliable on unstable networks.

---

## 5. Session Layer
- Creates, manages, and ends **sessions**.  
- Sessions can include **checkpoints** (resume data transfer from a certain point).  
- Unique: data travels only within its own session.  

---

## 6. Presentation Layer
- Acts as a **translator** for data formats between systems.  
- Handles **encryption/decryption** (e.g., HTTPS/TLS).  
- Example: sending an email → displays the same content regardless of email client.  

---

## 7. Application Layer
- The layer users interact with.  
- Defines **protocols and rules** for application data exchange.  
- Examples: **HTTP, DNS, SMTP, FTP, SSH**.  
- User-facing software: browsers, email clients, FTP clients.  

---

## Takeaways
- Layers work together through encapsulation/decapsulation.  
- TCP = reliability, UDP = speed.  
- Routers = Layer 3, Switches = Layer 2, Cables = Layer 1.  
- Troubleshooting often starts from the bottom (L1 physical issues) and moves up.
