import os

from log_cleaner import notify_admin


def check_dns_status(primary_dns, secondary_dns):
    # Check the status of the primary DNS server
    if not is_server_reachable(primary_dns):
        # If primary DNS is down, switch to secondary DNS
        failover_to_secondary_dns(secondary_dns)
        notify_admin("Switched to secondary DNS: {}".format(secondary_dns))

def is_server_reachable(server_ip):
    # Ping the server to check if it is reachable
    response = os.system("ping -c 1 " + server_ip)
    return response == 0

def failover_to_secondary_dns(secondary_dns):
    # Command to switch to secondary DNS
    os.system("dnsTool -a failover -s {}".format(secondary_dns))

# Example usage
check_dns_status("192.168.1.1", "192.168.1.2")
