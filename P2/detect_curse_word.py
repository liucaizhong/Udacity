import urllib.request

def read_text():
    quotes = open(r'C:\Users\liucaizhong\Desktop\DFZQ\forever_cmd.txt')
    contents_of_file = quotes.read()
    # print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    url = u'http://www.wdylike.appspot.com/?q=' + text_to_check
    # url = u'http://www.baidu.com'
    connection = urllib.request.urlopen(url)
    output = connection.read()
    # print(output)
    connection.close()
    if 'true' in output:
        print('Profanity Alert')
    elif 'false' in output:
        print('This document has no curse words!')
    else:
        print('Could not scan the document properly')

read_text()
