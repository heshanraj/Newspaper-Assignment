from .newspaper import Newspaper
from typing import List

from .issue import Issue

class Editor(object):
    def __init__(self,editor_id,editorname,editoraddress):
        self.newspapers=[]
        self.editor_id = editor_id
        self.editorname = editorname
        self.editoraddress = editoraddress
        self.newspaper:List[Newspaper] = []
        self.issues: List[Issue]=[]



