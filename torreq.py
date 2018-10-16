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
    try:
        res = session.get(url)
        print("Website reachable. Response 200. OK") if res.status_code is 200\
            else print("Resource unavailable. Response not 200. Not OK.")
        try:
            if (str(input("View headers? (y/n): "))) is 'y':
                print(res.headers)
        except: print("No headers.")
    except:
        print("Website unreachable.")

main()
