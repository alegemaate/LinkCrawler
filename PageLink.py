'''Named tuple creation and json lib'''
from typing import NamedTuple

class PageLink:
  ''' Strucutre for page link'''
  url = None
  internal = None
  external = None
  status = None
  depth = None

  def __init__(self, url, depth):
    self.url = url
    self.depth = int(depth)

  def set_links(self, internal, external):
    '''Set links'''
    self.internal = list(internal)
    self.external = list(external)

  def set_status(self, status):
    '''Set status'''
    self.status = int(status)
