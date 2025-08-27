# Packets and Frames (TryHackMe)

## Packets vs Frames
- Packets: Operate at Layer 3 (Network Layer). Contain IP headers and payload.
- Frames: Operate at Layer 2 (Data Link Layer). Encapsulate packets with MAC addresses.
- Analogy: Frames act like envelopes carrying packets (letters).
- Data is sent in smaller units to reduce bottlenecks and reassembled on the receiving end.

---

## Transmission Control Protocol (TCP)
- Connection-oriented protocol designed for reliable communication.
- Uses encapsulation and decapsulation across TCP/IP layers.

### Three-Way Handshake
1. SYN – Client initiates connection.
2. SYN/ACK – Server responds and acknowledges.
3. ACK – Client confirms, connection established.

### Key Headers
- Source/Destination IP and Port
- Sequence and Acknowledgment numbers
- Checksum for error detection
- Flags for control (handshake, termination)
- Payload (data)

### Advantages
- Ensures data arrives intact and in order
- Prevents flooding through synchronization
- Reliable communication across networks

### Disadvantages
- Higher overhead, slower than UDP
- Lost packets halt progress until retransmitted
- Requires more resources

---

## User Datagram Protocol (UDP)
- Stateless protocol with no handshake or persistent connection.
- Prioritizes speed over reliability, common in streaming and gaming.

### Advantages
- Faster due to low overhead
- Application controls send rate

### Disadvantages
- No guarantee of delivery or order
- Susceptible to poor user experience with unstable connections

### Packet Structure
- Time to Live (TTL)
- Source and Destination IP
- Source and Destination Ports
- Data payload
- No acknowledgments or connection setup

---

## Ports
- Serve as endpoints for data exchange, like harbors for ships.
- Range: 0–65535

### Common Ports
- 21 – FTP (File Transfer)
- 22 – SSH (Secure Shell)
- 80 – HTTP (Web traffic)
- 443 – HTTPS (Secure web traffic)
- 445 – SMB (File/device sharing)
- 3389 – RDP (Remote Desktop)

Standardized ports ensure consistent communication across applications, though alternatives (e.g., 8080) are often used.

---

## Summary
- Packets (Layer 3) and Frames (Layer 2) are the core data units in networking.
- TCP is reliable but resource-heavy, while UDP is faster with less reliability.
- Ports standardize communication for applications across networks.
