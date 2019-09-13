# LinkCrawler
Basic python link crawler that crawls websites up to a given depth and outputs JSON. 

Created using python 3, use the appropriate pip and python commands.

## Dependencies
```pip install requests```

```pip install beautifulSoup4```

## Running
```python scrape.py <url> <max depth> [show log]```

## Output
Outputs in JSON format with the following structure
```
[
  {
    "url": <page>,
    "status": <http status code>,
    "internal": [<internal links>],
    "external": [<external links>],
    "depth": <depth from base>
  }
]
```
