"""Imports"""
import sys
import json
import requests
from bs4 import BeautifulSoup
from PageLink import PageLink

def crawl_page(page, depth, base_url):
  """Get individual page"""

  # Set of next links
  internal = set()
  external = set()

  # Make request
  response = requests.get(page)
  status = response.status_code

  # Only existing pages allowed
  if status == 200:
    # Get all a tags
    soup = BeautifulSoup(response.text, "html.parser")

    # Get all a tags
    raw_links = soup.findAll('a')
    for i in range(0, len(raw_links) - 1):
      current_tag = raw_links[i]
      if not current_tag.has_attr('href'):
        continue

      next_link = current_tag['href']

      # Remove incorrect slashes and check domain
      next_link = next_link.replace('\\', '/')
      if base_url not in next_link:
        # External link
        if '://' in next_link:
          external.add(next_link)
        # Add base url to current
        else:
          internal.add(base_url + next_link)
      else:
        internal.add(next_link)

  page_link = PageLink(page, depth)
  page_link.set_links(internal, external)
  page_link.set_status(status)
  return page_link


def crawl(base_url, max_depth, debug=False):
  """Entry point"""

  # Track visited, external and to be visited links
  unvisited = {(base_url, 0)}
  visited = []

  # Run until stack is done
  while unvisited != set():
    # Pop first one off of set
    (url, depth) = unvisited.pop()

    # Skip if at max depth
    if depth > int(max_depth):
      continue

    # Ensure we do not begin already visited site
    if url not in map(lambda v: v.url, visited):
      # Get links from current page
      if debug:
        print("[depth {0}]: {1}".format(depth, url))
      page_link = crawl_page(url, depth, base_url)

      # Add to visited
      visited.append(page_link)

      # Add to unvisited, only unvisited
      unvisited_links = filter(lambda l: l not in map(lambda v: v.url, visited), page_link.internal)
      for link in unvisited_links:
        unvisited.add((link, depth + 1))

  print(json.dumps([ob.__dict__ for ob in visited]))


# Param check
if len(sys.argv) == 3:
  crawl(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
  crawl(sys.argv[1], sys.argv[2], sys.argv[3])
else:
  print("Please pass <url> <max depth> [show log]")
