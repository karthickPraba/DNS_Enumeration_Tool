import dns.resolver
import sys



record_types=["A","AAAA","NS","MX","PTR","SOA"]
try:
    domain= sys.argv[1]
except IndexError:
    print("Syntax Error - Python3 DNS_enum.py <domainname>")
    quit()
for records in record_types:
    try:
        answer = dns.resolver.resolve(domain, records)
        print(f"\n{records} Records")
        print("-"*30)
        for server in answer:
            print(server.to_text() )
    except dns.resolver.NoAnswer:
        print("No Records Found....")
        pass
    
    except dns.resolver.NXDOMAIN:
        print(f"The Provided Domain Name {domain} does not exist, Please Check and try again.")
        quit()
    except KeyboardInterrupt:
        print("\nGood Bye  :)")
        quit()
    