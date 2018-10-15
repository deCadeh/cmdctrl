#!/bin/python
import requests

def main():
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    
    onion = str(input("Enter URL (without protocol identifier): "))
    url = "http://" + onion
    
    # res = session.get("http://3g2upl4pq6kufc4m.onion") # DuckDuckGo
    res = session.get(url)
    print ("Website reachable") if res.status_code is 200 else\
        print("Website unreachable")
    if (str(input("View headers? (y/n): "))) is 'y':
        print(res.headers)
    
main()
