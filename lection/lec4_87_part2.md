```python
        def do_POST( self ): 
            print('-------------------------------')
            print("POST") 
            requested_url = self.requestline.split()[1] 
            parsed_url = urlparse.urlsplit( requested_url ) 
            cutted_url = urlparse.urlunsplit( ( '', '', parsed_url.path, parsed_url.query, '' ) ) 
            print(parsed_url.hostname)
            print(parsed_url.path)
            print(parsed_url.query) 
            print(requested_url)
            port = 80 if None == parsed_url.port else parsed_url.port 
            req_headers = {} 
            for x in self.headers.items(): 
              req_headers[x[0]] = x[1] 
            print(req_headers)
            body = self.rfile.read(int(self.headers['content-length'])) 
            print('body -- ', body)
            conn = httplib.HTTPConnection( parsed_url.hostname, port ) 
            conn.request( 'POST', cutted_url, body,headers = req_headers ) 
            response = conn.getresponse() 
            print(response.status)
            self.send_response( response.status ) 
            for x in response.msg.items(): 
              self.send_header( x[0], x[1] ) 
            self.end_headers() 

            html = response.read() 
            self.wfile.write( html ) 
            self.connection.close() 
            conn.close() 
            print('End - post')
            return 
```
