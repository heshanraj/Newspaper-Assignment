from flask import jsonify
from flask_restx import Namespace, reqparse, Resource, fields
from ..model.editor import Editor
from ..model.agency import Agency
from ..model.newspaper import Newspaper
from ..model.issue import Issue

editor_ns = Namespace("editor", description="editor related operations")

# model for normal use, that will display all the information about the editor
editor_model = editor_ns.model('EditorModel', {
     'editor_id': fields.Integer(required=False,
                help='The unique identifier of an editor'),
     'editorname': fields.String(required=True,
                help='The name of the editor'),
     'editoraddress': fields.String(required=True,
                help='The address of the editor '),
     'issues' : fields.List(fields.Integer,required=True,
                help='The id of the editor'),
     'newspaper' : fields.List(fields.Integer,required=True,
                help='The id of the editor')
    })

#model for a user is allowed to edit the data, no id option/issues/newspaper is provided beacuse id is auto generated in agency class
editor_modelnoid = editor_ns.model('editor_modelnoid', {
     'editorname': fields.String(required=True,
                help='The name of the editor'),
     'editoraddress': fields.String(required=True,
                help='The address of the editor ')

    })


@editor_ns.route('/')
class EditorAPI(Resource):
# WE MKAE EDITOR
    @editor_ns.doc(editor_model, description="Add a new editor")
    @editor_ns.expect(editor_modelnoid, validate=True)
    @editor_ns.marshal_with(editor_model, envelope='editor')
    def post(self):
        # TODO: this is not smart! you should find a better way to generate a unique ID!
        editor_id = Agency.get_instance().editoridcreator()         # WE USE THE EDITOR ID CREATOR(my most innovative invention) to create an editor id

        # create a new editor object and add it
        new_editor = Editor(editor_id=editor_id,                          #since we using the no id model, i display the editor id that was assigned and the name and address which they were alowed to edit
                            editorname=editor_ns.payload['editorname'],
                            editoraddress=editor_ns.payload['editoraddress'])

        Agency.get_instance().add_editor(new_editor) #this stores it

        return new_editor

    @editor_ns.doc(editor_model, description="list of all editors in the agency")
    @editor_ns.marshal_list_with(editor_model, envelope='editor')
    def get(self):
        return Agency.get_instance().editors # this basiclally accesss the list of all editors in agency

@editor_ns.route('/<int:editor_id>')
class EditorInfo(Resource):

    @editor_ns.doc(editor_model, description="Get an editors information")
    @editor_ns.marshal_with(editor_model, envelope='editor')
    def get(self, editor_id):
        edi= Agency.get_instance().get_editor(editor_id)
        if not edi:
            return jsonify(f"Editor with ID {editor_id} was not found")
        else:
            return edi

    @editor_ns.doc(editor_model, description="Update an editors information")
    @editor_ns.expect(editor_modelnoid, validate=True)
    @editor_ns.marshal_with(editor_model, envelope='editor')
    def post(self,editor_id):
        e = Agency.get_instance().get_editor(editor_id)
        e.editorname=editor_ns.payload['editorname']
        e.editoraddress=editor_ns.payload['editoraddress']
        return e

    @editor_ns.doc(description="Delete an editor")
    def delete(self, editor_id):
        e = Agency.get_instance().get_editor(editor_id)
        if not e:
            return jsonify(f"Editor with ID {editor_id} was not found")
        Agency.get_instance().remove_editor(e)
        return jsonify(f"Editor with ID {editor_id} was removed")

@editor_ns.route('/<int:editor_id>/issues')
class EditorReturn(Resource):
    @editor_ns.doc(editor_model, description="Return a list of newspaper issues that the editor was responsible for.")
    @editor_ns.marshal_with(editor_model, envelope='editor')
    def get(self,editor_id):
        wew = Agency.get_instance().get_editor(editor_id)
        if wew:
            x=[]
            for paper in Agency.get_instance().all_newspapers():
                for issue in paper.issues:
                    if issue.editor_id == editor_id:
                        x.append(issue)
            wew.issues=x
            return jsonify(f"Editor with ID {editor_id}  not found")









