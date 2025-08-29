# DNS in Detail Notes

## What is DNS?
DNS (**Domain Name System**) provides a way to communicate with devices on the Internet without needing to remember IP addresses.  
- Every device has a unique IP address (e.g., 104.26.10.229).  
- DNS resolves names (e.g., `tryhackme.com`) to IPs for easier access.  

---

## Domain Hierarchy
- **TLD (Top-Level Domain)**: Rightmost part of a domain (e.g., `.com`).  
  - gTLD (Generic): `.com`, `.org`, `.edu`, `.gov`.  
  - ccTLD (Country Code): `.ca`, `.co.uk`.  
  - New gTLDs: `.online`, `.club`, `.website`, `.biz`.  
- **Second-Level Domain**: Directly to the left of the TLD (e.g., `tryhackme` in `tryhackme.com`).  
- **Subdomain**: Prefix before the Second-Level Domain, separated by dots (e.g., `admin.tryhackme.com`).  
  - Can chain multiple subdomains (e.g., `jupiter.servers.tryhackme.com`).  
  - Max length: 253 characters.

---

## DNS Record Types
- **A Record**: Resolves to IPv4 address (e.g., `104.26.10.229`).  
- **AAAA Record**: Resolves to IPv6 address (e.g., `2606:4700:20::681a:be5`).  
- **CNAME Record**: Resolves to another domain (e.g., `store.tryhackme.com → shops.shopify.com`).  
- **MX Record**: Email server records with priority order (e.g., `alt1.aspmx.l.google.com`).  
- **TXT Record**: Free text fields for email validation, domain ownership, etc.

---

## DNS Request Process
1. **Local Cache**: Computer checks if domain is already cached.  
2. **Recursive DNS Server**: Usually ISP-provided. Searches its cache or queries root servers.  
3. **Root Servers**: Direct request to correct TLD server (e.g., `.com`).  
4. **TLD Servers**: Hold records pointing to authoritative nameservers.  
5. **Authoritative Servers**: Store actual DNS records. Return result with TTL (time to live).  

**Result:** DNS record is cached locally for future requests, reducing lookup time.  

---

## Key Takeaways
- DNS translates human-readable domains into machine-readable IPs.  
- Hierarchical structure: Root → TLD → Second-Level Domain → Subdomain.  
- Multiple record types exist (A, AAAA, CNAME, MX, TXT).  
- Caching improves efficiency; TTL determines how long data stays valid.  
