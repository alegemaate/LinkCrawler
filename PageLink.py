'''Named tuple creation and json lib'''
from typing import NamedTuple

class PageLink:
  ''' Strucutre for page link'''
  url = None
  internal = None
  external = None
  status = None
  depth = None

  def __init__(self, url, internal, external, status, depth):
    self.url = url
    self.internal = internal
    self.external = external
    self.status = status
    self.depth = depth

class DepthLink(NamedTuple):
  ''' Basic structure with deptha and url'''
  url: str
  depth: int
