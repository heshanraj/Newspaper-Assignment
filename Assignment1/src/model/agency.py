from typing import List, Union, Optional

from .newspaper import Newspaper, Issue

from .editor import Editor

from .subscriber import Subscriber

from .issue import Issue

class Agency(object):
    singleton_instance = None

    def __init__(self):
        self.newspapers: List[Newspaper] = []
        self.subscribers: List[Subscriber] = []
        self.paper_id = 1
        self.editor_id = 1
        self.issue_id = 1
        self.sub_id = 1
        self.editors: List[Editor] = []
        self.issue=[]


# everything below generates reandom ids
    def paperidcreator(self):
        self.paper_id+=1
        return self.paper_id

    def editoridcreator(self):
        self.editor_id+=1
        return self.editor_id

    def issueidcreator(self):
        self.issue_id+=1
        return  self.issue_id

    def subidcreator(self):
        self.sub_id +=1
        return self.sub_id


    @staticmethod
    def get_instance():
        if Agency.singleton_instance is None:
            Agency.singleton_instance = Agency()

        return Agency.singleton_instance

    #add newspaper
    def add_newspaper(self, new_paper: Newspaper):
        id_list = [paper.paper_id for paper in self.newspapers]
        assert new_paper.paper_id not in id_list, "Newspaper with this id already exists."
        self.newspapers.append(new_paper)

    def get_newspaper(self, paper_id: Union[int,str]) -> Optional[Newspaper]:
        for paper in self.newspapers:
            if paper.paper_id == paper_id:
                return paper
        return None

    def all_newspapers(self) -> List[Newspaper]:
        return self.newspapers

#helps with the get all method
    def all_subscribers(self) -> List[Subscriber]:
        return self.subscribers

#helps with deleting papaer
    def remove_newspaper(self, paper: Newspaper):
        self.newspapers.remove(paper)

# help get one particular issue
    def get_issues(self,paper_id,issue_id:Union[int,str]):
        paper = self.get_newspaper(paper_id)
        if paper:
            for issue in paper.issues:
               if issue.issue_id == issue_id:
                   return issue
        return None
#help get one particlar editor
    def get_editor(self,editor_id:Union[int,str]):
        for editor in self.editors:
            if editor.editor_id == editor_id:
                return editor
        return None
#help get one particualrasdas sub
    def get_sub(self,sub_id:int):
        for sub in self.subscribers:
            if sub.sub_id == sub_id:
                return sub
        return None
# helps remove a sub
    def remove_sub(self,sub:Subscriber):
        self.subscribers.remove(sub)
# helps remove an editor
    def remove_editor(self,ed:Editor):
        self.editors.remove(ed)

# OMG ITS ADD HELP AN EDITOR WUT WOW
    def add_editor(self,ed:Editor):
        id_list = [editor.editor_id for editor in self.editors]
        assert ed.editor_id not in id_list, "Editor with this id already exists."
        self.editors.append(ed)


# so BASICALLY, in a nutsheell, this in a way, NAY, MOST definently helps with the fucntion GET ALL EDITORS WHICH happily resides in the editor_ns file, i hope it works im 50/50 abt it
    def all_editors(self) -> List[Editor]:
        return self.editors

#add sub = it helps with the create a subscirber methof
    def add_sub(self,new_sub:Subscriber):
        id_list = [sub.sub_id for sub in self.subscribers]
        assert new_sub.sub_id not in id_list, "Subscriber with this id already exists."
        self.subscribers.append(new_sub)


    def get_missing_issues(self):
        return [issue for issue in self.issue if not issue.released]


    def remove_instance():
        Agency.singleton_instance = None



