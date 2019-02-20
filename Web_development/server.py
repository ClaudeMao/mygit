import os
from wsgiref.simple_server import make_server
from whos_your_daddy import application

#cwd = os.getcwd()
#files = os.listdir(cwd)
#os.chdir(a) #change current working didrectory
def main():
    httpd = make_server('', 8000, application)
    print('Serving Http on port 8000')
    httpd.serve_forever()

if __name__ == '__main__':
    main()
