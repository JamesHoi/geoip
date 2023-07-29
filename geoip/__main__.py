import sys
from argparse import ArgumentParser
import socket
import requests
import json

API = "http://demo.ip-api.com/json/"

def get_ip(domain: str, is_ipv4: bool, is_ipv6: bool):
    ip_list = []
    family = 0
    if is_ipv4: family = socket.AF_INET
    elif is_ipv6: family = socket.AF_INET6
    
    try:
        ais = socket.getaddrinfo(domain,0,family,0,0)
        for result in ais:
            ip_list.append(result[-1][0])
            ip_list = list(set(ip_list))
            return ip_list
    except:
        print("cannot find domain ip")


def main():
    parser = ArgumentParser(
        prog="geoip",
        description="A toy for check domain geographic location",
        epilog="example: geoip google.com"
    )
    parser.add_argument("domain",help="domain or ip that you want to locate")
    parser.add_argument("-4","--ipv4",help="force to use ipv4",action="store_true",default=False)
    parser.add_argument("-6","--ipv6",help="force to use ipv6",action="store_true",default=False)
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    try:
        opt = parser.parse_args()
        ip_list = get_ip(opt.domain,
                         is_ipv4=opt.ipv4,
                         is_ipv6=opt.ipv6)
        for i in range(len(ip_list)):
            r = requests.get(API+ip_list[i])
            assert r.status_code == 200, "geoip api error"
            data = json.loads(r.content)
            print(f"ip{i+1}: {ip_list[i]}")
            print(f"location: {data['country']} {data['regionName']} {data['city']}")
            print(f"lambda: {data['lat']} longitude: {data['lon']}")
            print("")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()