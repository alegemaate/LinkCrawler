"""Imports"""
import requests
import sys
from bs4 import BeautifulSoup
from PageLink import PageLink

def crawl_page(page, depth):
  """Get individual page"""
  # Echo page
  print("Travelling to: ", page)

  # Set of next links
  links = set()

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

      # Ensure we are going to html page
      links.add(next_link)

  return PageLink(page, links, status, depth + 1)


def crawl(base_url):
  """Entry point"""

  # Set of links still needing visiting
  unvisited = {base_url}

  # External links
  external = set()

  # Tracking of links visited and graph
  visited = set()

  # Link objects
  link_obj = []

  while unvisited != set():
    # Pop first one off of set
    current = unvisited.pop()

    # Remove incorrect slashes and check domain
    current = current.replace('\\', '/')
    if base_url not in current:
      # External link
      if '://' in current:
        external.add(current)
      # Add base url to current
      else:
        current = base_url + current

    # Ensure we do not begin in external site
    if current not in external and current not in visited:
      # Add to visited
      visited.add(current)

      # Get links from current page
      page_link = crawl_page(current, 1)
      link_obj.append(page_link)

      # Add to unvisited, only unvisited
      new_links = page_link.links.difference(visited)
      unvisited = unvisited.union(new_links)

  print('Vistited:')
  print(visited)
  print('External:')
  print(external)
  #print('obj:')
  #print(link_obj)


# Param check
if len(sys.argv) < 2:
  print("Please pass a site to crawl")
else:
  crawl(sys.argv[1])
