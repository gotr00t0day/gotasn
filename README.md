# gotasn
Extract the IP range associated with a given ASN (Autonomous System Number) and subsequently utilize the Masscan tool to identify open HTTP ports within that range. 

gotasn will save the ip ranges extracted from asnmap to a file called ipranges.txt, masscan will scan the ipranges.txt file and save any ips that has any http ports open to an xml file. It will then parse the file and extract the ips and save them to a file called ip_addr.txt.

## INSTALL

git clone https://github.com/gotr00t0day/gotasn.git

cd gotasn

pip3 install -r requirements.txt

## USAGE

python3 gotasn.py ASN
