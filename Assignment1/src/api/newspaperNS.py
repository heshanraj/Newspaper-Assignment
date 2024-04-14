import random
from flask import jsonify
from flask_restx import Namespace, reqparse, Resource, fields

from ..model.agency import Agency
from ..model.newspaper import Newspaper
from ..model.issue import Issue
from ..model.editor import Editor


newspaper_ns = Namespace("newspaper", description="Newspaper related operations")
issues_ns = Namespace("issues",description="Issue related operation")

paper_model = newspaper_ns.model('NewspaperModel', {
    'paper_id': fields.Integer(required=False,
            help='The unique identifier of a newspaper'),
    'name': fields.String(required=True,
            help='The name of the newspaper, e.g. The New York Times'),
    'frequency': fields.Integer(required=True,
            help='The publication frequency of the newspaper in days (e.g. 1 for daily papers and 7 for weekly magazines'),
    'price': fields.Float(required=True,
            help='The monthly price of the newspaper (e.g. 12.3)')

   })



paper_model_noid = newspaper_ns.model('paper_model_noid', {
    'name': fields.String(required=True,
            help='The name of the newspaper, e.g. The New York Times'),
    'frequency': fields.Integer(required=True,
            help='The publication frequency of the newspaper in days (e.g. 1 for daily papers and 7 for weekly magazines'),
    'price': fields.Float(required=True,
            help='The monthly price of the newspaper (e.g. 12.3)')
   })


paper_model_paper_id = newspaper_ns.model('paper_model_paper_id', {
    'paper_id': fields.Integer(required=True,
            help='The name of the newspaper, e.g. The New York Times'),
   })

issues_model = issues_ns.model('IssueModel',{
    'issue_id': fields.Integer(required=False,
            help='The unique identifier of a newspaper'),
    'editor_id': fields.Integer(required=False,
            help='The id of the editor'),
    'price': fields.Float(required=True,
            help='The monthly price of the newspaper (e.g. 12.3)'),
    'subscriber': fields.List(fields.Integer,required=True,
            help='The number of subscribers'),
    'pagenumber': fields.Integer(required=True,
            help='the page number'),
    'released': fields.Boolean(required=True,
            help='The monthly price of the newspaper (e.g. 12.3)'),
    'paper_id':fields.Integer(required = True,
            help = 'The unique identifier of a paper'),
    'releasedate':fields.String(required = True,
            help='The date of which the issue was released')


})

issues_model_noid = issues_ns.model('IssueModel_noid',{
    'price': fields.Float(required=True,
            help='The monthly price of the newspaper (e.g. 12.3)'),
    'subscriber': fields.List(fields.Integer,required=True,
            help='The number of subscribers'),
    'pagenumber': fields.Integer(required=True,
            help='the page number'),
    'released': fields.Boolean(required=True,
            help='The monthly price of the newspaper (e.g. 12.3)'),
    'releasedate':fields.String(required = True,
            help='The date of which the issue was released')

})

issues_model_with_editor = issues_ns.model('issue_model_with_editor',{
    'editor_id': fields.Integer(required=False,
            help='The id of the editor'),

})

issues_model_for_sub = issues_ns.model('issues_model_for_sub',{
    'issue_id': fields.Integer(required=False,
            help='The id of the issue'),
    'paper_id':fields.Integer(required = True,
            help = 'The unique identifier of a paper')

})

deliver_issue_model = issues_ns.model('deliver_issue_model',{
    'sub_id': fields.Integer(required=False,
            help='The id of the subscriber'),

})



@newspaper_ns.route('/')
class NewspaperAPI(Resource):

    @newspaper_ns.doc(paper_model, description="Create a new newspaper.")
    @newspaper_ns.expect(paper_model_noid, validate=True)
    @newspaper_ns.marshal_with(paper_model, envelope='newspaper')
    def post(self):
        # TODO: this is not smart! you should find a better way to generate a unique ID!
        paper_id = Agency.get_instance().paperidcreator()

        # create a new paper object and add it
        new_paper = Newspaper(paper_id=paper_id,
                              name=newspaper_ns.payload['name'],
                              frequency=newspaper_ns.payload['frequency'],
                              price=newspaper_ns.payload['price'])
        Agency.get_instance().add_newspaper(new_paper)

        # return the new paper
        return new_paper

    @newspaper_ns.marshal_list_with(paper_model, envelope='newspapers')
    def get(self):
        return Agency.get_instance().all_newspapers()


@newspaper_ns.route('/<int:paper_id>')
class NewspaperID(Resource):

    @newspaper_ns.doc(description="Get a newspaper's information")
    @newspaper_ns.marshal_with(paper_model, envelope='newspaper')
    def get(self, paper_id):

        search_result = Agency.get_instance().get_newspaper(paper_id)
        if search_result:
            return search_result
        return jsonify('Error: no newspaper found')

    @newspaper_ns.doc(paper_model, description="Update a new newspaper.")
    @newspaper_ns.expect(paper_model_noid, validate=True)
    @newspaper_ns.marshal_with(paper_model, envelope='newspaper')
    def post(self, paper_id):
        paper = Agency.get_instance().get_newspaper(paper_id)
        if not paper:
            return jsonify(f"Newspaper with ID {paper_id} was not found")
        paper.name = newspaper_ns.payload['name']
        paper.frequency = newspaper_ns.payload['frequency']
        paper.price = newspaper_ns.payload['price']
        return paper

    @newspaper_ns.doc(description="Delete a new newspaper")
    def delete(self, paper_id):
        targeted_paper = Agency.get_instance().get_newspaper(paper_id)
        if not targeted_paper:
            return jsonify(f"Newspaper with ID {paper_id} was not found")
        Agency.get_instance().remove_newspaper(targeted_paper)
        return jsonify(f"Newspaper with ID {paper_id} was removed")



@newspaper_ns.route("/<int:paper_id>/issue")
class IssueList(Resource):
    @issues_ns.doc(description="List all issues of a specific newspaper.")
    @issues_ns.marshal_with(issues_model, envelope='issue')
    def get(self, paper_id):
        return Agency.get_instance().get_newspaper(paper_id).issues

    @issues_ns.doc(issues_model, description="Add a new issue")
    @issues_ns.expect(issues_model_noid, validate=True)
    @issues_ns.marshal_with(issues_model, envelope='issue')
    def post(self,paper_id):
        # TODO: this is not smart! you should find a better way to generate a unique ID!
        issue_id = Agency.get_instance().issueidcreator()
        paper = Agency.get_instance().get_newspaper(paper_id)

        # create a new paper object and add it
        new_issue = Issue(releasedate=issues_ns.payload['releasedate'],
                          price=issues_ns.payload['price'],
                          issue_id=issue_id,
                          pagenumber=issues_ns.payload['pagenumber'],
                          paper_id = paper_id,
                          editor_id = 1,
                          sub_id = 1,
                          released=issues_ns.payload['released'],
                          )

        paper.issues.append(new_issue)
        return new_issue

@newspaper_ns.route("/<int:paper_id>/issue/<int:issue_id>")
class NewspaperIssueInformation(Resource):
    @issues_ns.doc(description="Get information of a newspaper issue")
    @issues_ns.marshal_with(issues_model, envelope='issue')
    def get(self,paper_id,issue_id):
        return Agency.get_instance().get_issues(paper_id,issue_id)


@newspaper_ns.route("/<int:paper_id>/issue/<int:issue_id>/release")
class ReleaseIssue(Resource):
    @issues_ns.doc(issues_model, description="Release an issue")
    @issues_ns.expect(issues_model_noid, validate=True)
    @issues_ns.marshal_with(issues_model, envelope='issue')
    def post(self, paper_id, issue_id):
         issue = Agency.get_instance().get_issues(paper_id,issue_id)
         if issue:
            issue.released = True
            return issue
         return jsonify('Error: no issue found')


@newspaper_ns.route("/<int:paper_id>/issue/<int:issue_id>/editor")
class SpecifyEditor(Resource):
    @issues_ns.doc(issues_model, description="Specify an editor for an issue")
    @issues_ns.expect(issues_model_with_editor, validate=True)
    @issues_ns.marshal_with(issues_model, envelope='issue')
    def post(self,paper_id,issue_id):
        issue = Agency.get_instance().get_issues(paper_id, issue_id)
        if issue:
            editor = Agency.get_instance().get_editor(issues_ns.payload['editor_id'])
            if editor:
                issue.set_editor(editor.editor_id)
                editor.issues.append(issue.issue_id)
                return issue
            return jsonify(f"Editor with ID {issues_ns.payload['editor_id']} was not found")
        return jsonify(f"Issue with ID {issue_id} was not found")




@newspaper_ns.route("/<int:paper_id>/issue/<int:issue_id>/deliver")
class SendIssue(Resource):
    @issues_ns.doc(issues_model, description="Send an issue to a subscriber. This means there should be a record of the subscriber receiving")
    @issues_ns.expect(deliver_issue_model, validate=True)
    @issues_ns.marshal_with(issues_model, envelope='issue')
    def post(self, paper_id, issue_id):
        issue = Agency.get_instance().get_issues(paper_id, issue_id)
        if issue:
            subscriber = Agency.get_instance().get_sub(issues_ns.payload['sub_id'])
            if subscriber:
                issue.subscriber.append(subscriber.sub_id)
                subscriber.deliveredissues.append(issue.issue_id)
                return issue
            return jsonify(f"Subscriber with ID {subscriber.subscriberid} was not found")
        return jsonify(f"Issue with ID {issue_id} was not found")



@newspaper_ns.route("/<int:paper_id>/stats")
class ReturnStats(Resource):
    @newspaper_ns.doc(description="Return information about the specific newspaper (number of subscribers, monthly and annual revenue)")
    def get(self, paper_id):
        paper = Agency.get_instance().get_newspaper(paper_id)
        if paper:
            paper_subs = len(paper.subscriber)
            paper_revenue = paper.price * paper_subs
            annual_revenue = paper_revenue * 12
            return{'subs': paper_subs, 'revenue': paper_revenue, 'anual_revenue': annual_revenue}
        else:
            return jsonify(f"Newspaper with ID {paper_id} was not found")


















