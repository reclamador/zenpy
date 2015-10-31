
import dateutil.parser
from zenpy.lib.objects.base_object import BaseObject

class Group(BaseObject):
    def __init__(self, api=None):
        self.api = api
        self._name = None
        self._url = None
        self.created_at = None
        self.updated_at = None
        self.deleted = None
        self.id = None
        
    
    