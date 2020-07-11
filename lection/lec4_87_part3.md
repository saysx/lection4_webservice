```python
        def do_GET( self ): 
            print('--------------------------------------')
            print('GET')
            requested_url = self.requestline.split()[1] 
            parsed_url = urlparse.urlsplit( requested_url ) 
            cutted_url = urlparse.urlunsplit( ( '', '', parsed_url.path, parsed_url.query, '' ) ) 
            port = 80 if None == parsed_url.port else parsed_url.port 
            req_headers = {} 
            for x in self.headers.items(): 
              req_headers[x[0]] = x[1] 
            print(req_headers)

            conn = httplib.HTTPConnection( parsed_url.hostname, port ) 
            conn.request( 'GET', cutted_url ,'' ,req_headers ) 
            response = conn.getresponse() 
            self.name = '' 
            self.send_response( response.status ) 
            print(response.status)
            print(parsed_url.hostname, ':', port)
            print(response.msg.items())
            i=0 
            for x in response.msg.items(): 
              i=i+1 
              if(x[0]!='transfer-encoding'): 
                print('--- ', x[0],' : ' ,x[1])
                if(x[0]!='connection'): 
                  self.send_header( x[0], x[1] ) 
                else: self.send_header( 'connection', 'close' ) 
            self.end_headers() 
            html = response.read() 
            self.wfile.write( html ) 
            conn.close() 
            self.connection.close() 
            print('END -- GET') 
            return 0 
```    
