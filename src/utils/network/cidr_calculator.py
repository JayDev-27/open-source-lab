"""Calculates CIDR network host range."""
import ipaddress
def cidr_info(subnet: str):
    net = ipaddress.ip_network(subnet, strict=False)
    return {'num_hosts': net.num_addresses, 'netmask': str(net.netmask)}
