import urllib2
def read_test():
    file_read = open(r"C:\mooo\test.txt")
    text=file_read.read()
    file_read.close()
    check_profanity(text)

def check_profanity(text):
    connection = urllib2.urlopen("http://www.wdylike.appspot.com/?q="+text,0,0)
    output=connection.read()
    #print(output)
    connection.close()
read_test()