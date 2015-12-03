import subprocess
import re
def IPaddr(addr1,zn):
     if zn == 1 :
         dd=re.search('(?<=:).+',addr1)
         return dd.group(0).strip("]'").strip()
     else:
         dd=re.search('(?<==).+',addr1)
         return dd.group(0).strip("]'").strip()





def Nslook(str1,strser):
    proc=subprocess.Popen(['/usr/bin/nslookup',str1.strip(),'8.8.8.8'],stdout=subprocess.PIPE)
    Addr1=filter(lambda x: x.__contains__(strser),   proc.stdout.read().split('\n'))
    return Addr1

for  str1  in  open("ho.ho"):
    #cmd='nslookup '+str.strip()+' 8.8.8.8'
    #print(cmd)
    #   proc=subprocess.Popen(['/usr/bin/nslookup',str1.strip(),'8.8.8.8'],stdout=subprocess.PIPE)
    #  Addr1=filter(lambda x: x.__contains__('Address: '),   proc.stdout.read().split('\n'))
    AddrE=Nslook(str(str1),'Address: ')
    IPAddrE=IPaddr(str(AddrE),1)
    Ptr1=Nslook(str(IPAddrE),'name = ')
    if  Ptr1:
        PtrE=IPaddr(str(Ptr1),20)
    else:
        PtrE=" Not resolved"
    print("IP address: "+IPAddrE+" |  Host name : "+str1.strip()+"|  PTR: "+PtrE)


