import pycurl

class CurlUptime:
    def __init__(self, url) -> None:
        self.url = url
        self.curl_session = pycurl.Curl()
        self.curl_session.setopt(self.curl_session.URL, self.url) # set url
        self.curl_session.setopt(self.curl_session.NOBODY, 1) # Don't waste time to download the body
        self.curl_session.perform()
        self.getinfo = self.curl_session.getinfo

    def get_status(self):
        return (self.getinfo(self.curl_session.RESPONSE_CODE))
    
    def get_dns_lookup(self):
        return self.getinfo(self.curl_session.NAMELOOKUP_TIME)

    def get_tcp(self):
        return self.getinfo(self.curl_session.CONNECT_TIME) - self.getinfo(self.curl_session.NAMELOOKUP_TIME)

    def get_ssl_tls(self):
        return self.getinfo(self.curl_session.APPCONNECT_TIME) - self.getinfo(self.curl_session.CONNECT_TIME)

    def get_ttfb(self):
        return self.getinfo(self.curl_session.STARTTRANSFER_TIME) - self.getinfo(self.curl_session.PRETRANSFER_TIME)
    
    def get_data_transfer(self):
        return self.getinfo(self.curl_session.TOTAL_TIME) - self.getinfo(self.curl_session.STARTTRANSFER_TIME)
    
    def get_total(self):
        return self.getinfo(self.curl_session.TOTAL_TIME)

    def get_full_dict(self) -> dict:
        final_dictionary = dict()
        final_dictionary.update({
            'status_code': self.get_status(),
            'dns_lookup': self.get_dns_lookup(),
            'tcp': self.get_tcp(),
            'ssl_tls': self.get_ssl_tls(),
            'ttfb': self.get_ttfb(),
            'data_transfer': self.get_data_transfer(),
            'total': self.get_total()
        })
        self.close_session()
        return final_dictionary
        

    def close_session(self):
        self.curl_session.close()

