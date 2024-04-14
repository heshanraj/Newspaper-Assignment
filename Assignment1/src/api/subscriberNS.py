from flask import jsonify
from flask_restx import Namespace, reqparse, Resource, fields

from ..model.agency import Agency
from ..model.newspaper import Newspaper
from ..model.issue import Issue
from ..model.subscriber import Subscriber
from .newspaperNS import paper_model_paper_id, paper_model, issues_model , issues_model_for_sub

subscriber_ns = Namespace("subscriber", description="Subscriber related operations")

#model which contains all the information about the subscriber
subscriber_model = subscriber_ns.model('SubscriberModel', {
     'sub_id': fields.Integer(required=False,
                help='The unique identifier of a subscriber'),
     'subname': fields.String(required=True,
                help='The name of the subscriber'),
     'subaddy': fields.String(required=True,
                help='The address of the subscriber '),
     'deliveredissues' : fields.List(fields.Integer,required=True,
                help='The issues of the subscriber'),
     'newspaper' : fields.List(fields.Nested(paper_model),required=True,
                help='The newspapers of the subscriber'),
     'specialissues' : fields.List(fields.Integer,required=True,
                help='The special issues of the subscriber')
    })
#model for a user to add subscriber, no id bcos id is auto generated
subscriber_modelnoid = subscriber_ns.model('Subscribermodelnoid', {
     'subname': fields.String(required=True,
                help='The name of the subscriber'),
     'subaddy': fields.String(required=True,
                help='The address of the subscriber ')

    })

#model for msisig issues model because i didnt like how the other one looked on the postman
missing_issues_model = subscriber_ns.model('missing_issues_model', {
     'missing_issues': fields.List(fields.Nested(issues_model_for_sub),required=True,
                help='The missing issues of the subscriber')


    })


@subscriber_ns.route('/')
class SubscriberAPI(Resource):
    @subscriber_ns.doc(subscriber_model, description="Get all subscribers")
    @subscriber_ns.marshal_list_with(subscriber_model, envelope='subscriber')
    def get(self):
        return Agency.get_instance().subscribers

    @subscriber_ns.doc(subscriber_modelnoid, description="Add a new subscriber")
    @subscriber_ns.expect(subscriber_modelnoid, validate=True)
    @subscriber_ns.marshal_with(subscriber_model, envelope='subscriber')
    def post(self):

        sub_id = Agency.get_instance().subidcreator()

        # create a new subscriber object and add it
        new_sub = Subscriber(sub_id=sub_id,
                                    subname=subscriber_ns.payload['subname'],
                                    subaddy=subscriber_ns.payload['subaddy'])

        Agency.get_instance().add_sub(new_sub)

        return new_sub


# i changed subscriber_id to sub_id
@subscriber_ns.route('/<int:sub_id>')
class SubscriberID(Resource):
    @subscriber_ns.doc(subscriber_model, description="Get a subscribers information")
    @subscriber_ns.marshal_list_with(subscriber_model, envelope='subscriber')
    def get(self,sub_id):
        return Agency.get_instance().get_sub(sub_id)
        # i return the sub id using the agnecy instance since, the ids are generated and stored in agency

    @subscriber_ns.doc(subscriber_model, description="Update a subscriber's information")
    @subscriber_ns.expect(subscriber_modelnoid, validate=True)
    @subscriber_ns.marshal_with(subscriber_model, envelope='subscriber')
    def post(self,sub_id):
        s = Agency.get_instance().get_sub(sub_id)
        s.subname=subscriber_ns.payload['subname']
        s.subaddy=subscriber_ns.payload['subaddy']
        return s
# i only let users change thier addys and names beacuse i dont want them to interfere with ids and issues/newspapers.
    @subscriber_ns.doc(description="Delete a subscriber")
    def delete(self,sub_id):
        gone_sub = Agency.get_instance().get_sub(sub_id)
        if not gone_sub:
            return jsonify(f"Subscriber with ID {sub_id} does not exist")
        Agency.get_instance().remove_sub(gone_sub)
        return jsonify(f"Subscriber with ID {sub_id} was removed")
# i get the sub id and if its delted it will say it dont exist otherwise it will delte using the remove function




@subscriber_ns.route('/<int:sub_id>/subscribe')
class SubscriberSubscribe(Resource):
    @subscriber_ns.doc(subscriber_modelnoid, description="Subscribe a subscriber to a newspaper. (Transmit the newspaper ID as parameter.)")
    @subscriber_ns.expect(paper_model_paper_id, validate=True)
    @subscriber_ns.marshal_with(subscriber_model, envelope='subscriber')
    def post(self,sub_id):
        sub = Agency.get_instance().get_sub(sub_id)
        if sub:
            paper_id= subscriber_ns.payload['paper_id']
            paper = Agency.get_instance().get_newspaper(paper_id)
            if paper:
                if paper not in sub.newspaper:
                    sub.newspaper.append(paper)
                    paper.subscriber.append(sub)
                return sub
        return jsonify('Error: no newspaper found')




@subscriber_ns.route('/<int:sub_id>/stats')
class SubscriberStats(Resource):
    @subscriber_ns.doc(subscriber_model, description="Get the number of newspaper subscriptions and the monthly and annual cost, as well as the number of issues that the subscriber received for each paper.")
    def get(self, sub_id):
        subscriber = Agency.get_instance().get_sub(sub_id)
        if subscriber:
            subscription_info = []
            for newspaper in subscriber.newspaper:
                subscription_data = {
                    "newspaper_id": newspaper.paper_id,
                    "newspaper_name": newspaper.name,
                    "subscriptions": len(newspaper.subscriber),
                    "monthly_cost": newspaper.price * (30 / newspaper.frequency),  # Assuming 30 days in a month
                    "annual_cost": newspaper.price * (360 / newspaper.frequency),  # Assuming 360 days in a year
                    "received_issues": len(
                        [issue for issue in newspaper.issues if issue.issue_id in subscriber.deliveredissues])
                }
                subscription_info.append(subscription_data)
            return subscription_info
        return jsonify(f"Subscriber with ID {sub_id} was not found")


@subscriber_ns.route('/<int:sub_id>/missingissues')
class SubscriberMissingIssues(Resource):
    @subscriber_ns.doc(subscriber_model, description="Check if there are any undelivered issues of the subscribed newspapers.")
    @subscriber_ns.marshal_list_with(missing_issues_model, envelope='subscriber')
    def get(self, sub_id):
        subscriber = Agency.get_instance().get_sub(sub_id)
        if subscriber:
            issuelist = []
            for paper_id in subscriber.newspaper:
                paper = Agency.get_instance().get_newspaper(paper_id)
                if paper:
                    for issue in paper.issues:
                        if issue.issue_id not in subscriber.deliveredissues:
                            issuelist.append(issue)
            return issuelist
        return 'Subscriber not found'


