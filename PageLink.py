'''Page link def'''

class PageLink:
  ''' Strucutre for page link'''
  url = None
  depth = None
  content_type = None
  status = None
  internal = None
  external = None

  def __init__(self, url, depth, content_type):
    self.url = url
    self.depth = int(depth)
    self.content_type = content_type

  def set_links(self, internal, external):
    '''Set links'''
    self.internal = list(internal)
    self.external = list(external)

  def set_status(self, status):
    '''Set status'''
    self.status = int(status)
