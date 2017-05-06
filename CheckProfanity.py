'''this code will check whetehr your texts contains any profanity or not'''

import urllib 
def read_test():
    file_read = open(r"C:\mooo\test.txt")
    text=file_read.read()
    file_read.close()
    check_profanity(text)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connection.read()
   # print(output)
    connection.close()
    if "true" in output:
        print("P")
    else:
        print("its a safe document. Go ahead")
     

read_test()

