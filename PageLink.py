'''Named tuple creation'''
from typing import NamedTuple

class PageLink(NamedTuple):
  ''' Strucutre for page link'''
  url: str
  links: set
  status: int
  depth: int
