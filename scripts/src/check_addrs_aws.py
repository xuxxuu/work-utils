from ipaddress import IPv4Address, IPv4Network

import requests
from rich import print


AWS_URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"


def get_aws_cidrs() -> list[str]:
    """Extract the cidr ranges from the aws json file"""
    response = requests.get(AWS_URL).json()
    ranges = [prefix["ip_prefix"] for prefix in response["prefixes"]]
    return ranges


def is_addr_aws(addr: IPv4Address) -> bool:
    ranges = [IPv4Network(cidr) for cidr in get_aws_cidrs()]
    return any(addr in network for network in ranges)


def main():
    from sys import argv
    if len(argv) == 1:
        print("Need ip address as an argument")
        exit()

    print(is_addr_aws(IPv4Address(argv[1])))

if __name__ == "__main__":
    main()
