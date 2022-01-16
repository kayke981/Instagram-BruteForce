## Instagram BruteForce
Instagram BruteForce is for password cracker bruteforce, you can use proxy but is optional
<hr>

## Installation

```bash
$ git clone https://github.com/kayke981/Instagram-BruteForce brute-insta
$ cd brute-insta
$ pip install -r requirements.txt
```
## Usage:
```bash
$ python3 instagram.py --wordlist path/to/wordlist.txt -username Username_Of_Target
```
## Help:
```
usage: instagram.py [-h] [-w WORDLIST] [-u USERNAME]
                    [-p PROXY] [-pf PROXY_FILE]
                    [-d DELAY] [--update] [--version]

Brute force instagram for hacking

optional arguments:
  -h, --help            show this help message and
                        exit
  -w WORDLIST, --wordlist WORDLIST
                        List of passwords (ins't
                        optional)
  -u USERNAME, --username USERNAME
                        Username of target (ins't
                        optional)
  -p PROXY, --proxy PROXY
                        List of proxy file (is
                        optional)
  -pf PROXY_FILE, --proxy-file PROXY_FILE
                        List of proxy file (is
                        optional)
  -d DELAY, --delay DELAY
                        Delay between requests
                        (default is 5)
  --update              Update repositore
  --version             Version
```

## LICENSE

Refer to LICENSE file. `[MIT]`