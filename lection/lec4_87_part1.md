# Прокси на Python
```python
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    from SocketServer import ThreadingMixIn
    import urllib2, sys, re, httplib, urlparse

    class ThreadedHTTPServer( ThreadingMixIn, HTTPServer ): 
        #поток-демон уничтожается при уничтожении главного потока
        #пользовательский поток может не уничтожаться, программа висит
          daemon_threads = True 
        if __name__ == '__main__': 
          proxy = ThreadedHTTPServer( ( 'localhost', 19277 ), ProxyHandler ) 
          try: 
            proxy.serve_forever() 
          except KeyboardInterrupt: 
            print('End of server')
          proxy.server_close() 

    class ProxyHandler(BaseHTTPRequestHandler):
        server_version = ''
        sys_version = ''
        def do_HEAD(self):
            print("HEAD")
        def log_message(self, format, *args):
            return
```
