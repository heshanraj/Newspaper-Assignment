from .newspaper import Newspaper
from typing import List

from .issue import Issue

class Subscriber(object):
    def __init__(self,sub_id,subname,subaddy):
        self.sub_id = sub_id
        self.subname = subname
        self.subaddy = subaddy
        self.newspaper:List[Newspaper] = []
        self.specialissues: List[Issue]=[]
        self.deliveredissues = []



