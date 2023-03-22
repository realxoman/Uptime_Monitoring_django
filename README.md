# Uptime Monitoring Django

This project uses PyCurl to measure various performance metrics for web requests, including status, DNS lookup time, TCP time, SSL/TLS time, TTFB, data transfer time, and total time.

## Installation

To install the dependencies required to run this project, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use this project, you can import the curl.py module and use the CurlUptime class to measure the performance metrics of a website.


### Importing the module

To import the curl.py module, you can use the following code:

```python
from curl import CurlUptime

url = "https://www.example.com"
curl = CurlUptime(url)

metrics = curl.get_metrics()

print(metrics)
```
This will output a dictionary containing the various performance metrics for the given URL.


## Contributing
If you find a bug or would like to suggest a new feature, feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the GPL 3.0 license - see the LICENSE file for details.




