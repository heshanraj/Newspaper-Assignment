
class Issue(object):

    def __init__(self, releasedate,price,issue_id,pagenumber,paper_id,editor_id,sub_id, released: bool = False):
        self.releasedate = releasedate
        self.released: bool = released
        self.editor_id = editor_id
        self.price = price
        self.issue_id = issue_id
        self.pagenumber = pagenumber
        self.subscriber = []
        self.sub_id = sub_id
        self.paper_id = paper_id

    def set_editor(self, editor_id):
        self.editor_id = editor_id

