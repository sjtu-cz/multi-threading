import json
import re
from urllib import request
import bs4
import requests
from selenium import webdriver
import threading


class MyThread(threading.Thread):
    """docstring for MyThread"""

    def __init__(self, thread_id, name, num) :
        super(MyThread, self).__init__()  #调用父类的构造函数 
        self.thread_id = thread_id
        self.name = name
        self.num = num
    def run(self) :
        print ("Starting " + self.name)
        crawler(self.num,self.name)
        print ("Exiting " + self.name)
def crawler(num,name):    
    fw=open(name,'w',encoding='utf-8')
    for i in range((num-1)*40,num*40):
        if i >= len(href):
            break;
        line = href[i]
        web=requests.get(line,timeout=20)
        content=web.text
        web1=content
        html=bs4.BeautifulSoup(content,'lxml')
        web1=html.find_all('p',class_="FR_field")
        web2=html.find('table',class_="FR_table_noborders")
        try:
            web3=web2.find('td',class_="fr_address_row2")
            print (web3)
            Address=re.findall(r'<td class="fr_address_row2">(.*) <',str(web3))
            print (Address)
        except Exception as e:
            Address=''
        
    
       
        email=re.findall(r'<span class="FR_label">E-mail Addresses:.*</span><a href=".*">(.*)</a>',str(web1))
        print (email)
        #EMAIL.append(email)
        reprint=re.findall(r'</span>(.*) \(reprint author\) </p>',str(web1))#<span class="FR_label">Reprint Address:.*</span>(.*)</p>
        print (reprint)
        #REPRINT.append(reprint)
        fw.write(author[i]+'\t'+''.join(email)+'\t'+''.join(Address)+'\t'+title[i]+'\t'+''.join(reprint)+'\n')
        i=i+1
        print (name + str(i))
    fw.close()
if __name__=='__main__':
    with open('BMC-BIOINFORMATICS(1).json','r',encoding='utf-8') as fp:
    # with open('NANOBIOSCIENCE.json','r',encoding='utf-8') as fp:
        content=fp.read()
    # print (content)
    href=re.findall(r'"href": "(.*)"',content)
    # print (href)
    title=re.findall(r'"title": "(.*)"',content)
    # print (title)
    author=re.findall(r'"author": "(.*)"',content)
    print (type(author))
    

    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)
    thread3 = MyThread(3, "Thread-3", 3)
    thread4 = MyThread(4, "Thread-4", 4)
    thread5 = MyThread(5, "Thread-5", 5)
    thread6 = MyThread(6, "Thread-6", 6)
    #开启线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
