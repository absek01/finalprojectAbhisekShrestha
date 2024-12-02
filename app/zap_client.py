from zapv2 import (ZAPv2)  # Correct import for the OWASP ZAP API Python client
import time  # Import time for scan progress delays


class ZAPClient:
    def __init__(self, api_key, base_url):
        # Initialize the ZAP API client with the API key and proxy address
        self.zap = ZAPv2(apikey=api_key, proxies={'http': base_url, 'https': base_url})

    def start_scan(self, target_url):
        # Start the ZAP Spider scan
        print(f"Starting spider scan for {target_url}...")
        spider_id = self.zap.spider.scan(target_url)
        while int(self.zap.spider.status(spider_id)) < 100:
            print(f"Spider progress: {self.zap.spider.status(spider_id)}%")
            time.sleep(1)

        print("Spider scan completed.")

        # Start the ZAP Active scan
        print(f"Starting active scan for {target_url}...")
        scan_id = self.zap.ascan.scan(target_url)
        while int(self.zap.ascan.status(scan_id)) < 100:
            print(f"Active scan progress: {self.zap.ascan.status(scan_id)}%")
            time.sleep(1)

        print("Active scan completed.")

    def get_alerts(self, target_url):
        # Retrieve and return alerts for the given target URL
        return self.zap.core.alerts(baseurl=target_url)
