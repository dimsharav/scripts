iptables -A OUTPUT -p tcp --dport 443 -j DROP
iptables -A OUTPUT -p tcp --dport 80 -j DROP
