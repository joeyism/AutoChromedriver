# AutoChromedriver
A helper library to automatically download chromedriver to current directory

## Installation

```
pip3 install --user autochromedriver
```

## Usage

### Commandline

```bash
autochromdriver [optional:version]
```

### Library
If you want to download the latest version, run 
```python
import AutoChromedriver

AutoChromedriver.download_chromedriver()
```
If you want to download a specific version, run
```python
import AutoChromedriver

AutoChromedriver.download_chromedriver(version="2.46")
```
If you want to download a specific version to a specific location, run 
```python
import AutoChromedriver

AutoChromedriver.download_chromedriver(version="2.46", location=".")
```

## Documentation
```python
def download_chromedriver(version="2.46")
```
Passing in a version is possible, and it defaults to `2.46`.
