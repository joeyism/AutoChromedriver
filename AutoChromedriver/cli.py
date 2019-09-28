#!/usr/bin/env python
import sys

import AutoChromedriver

def main():
    try:
        version = sys.argv[1]
        AutoChromedriver.download_chromedriver(version=version)
    except:
        AutoChromedriver.download_chromedriver()

if __name__ == "__main__":
    main()
