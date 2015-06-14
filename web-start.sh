iptables -D OUTPUT -p tcp --dport 443 -j DROP
iptables -D OUTPUT -p tcp --dport 80 -j DROP
