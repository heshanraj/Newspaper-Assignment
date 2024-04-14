import pytest

from ...src.model.newspaper import Newspaper, Issue
from ..fixtures import app, client, agency
from ...src.model.editor import Editor
from ...src.model.subscriber import Subscriber




def test_add_newspaper(agency):
    before = len(agency.newspapers)
    new_paper = Newspaper(paper_id=9,
                          name="New Straight Times",
                          frequency=7,
                          price=0.10)
    agency.add_newspaper(new_paper)
    assert len(agency.all_newspapers()) == before + 1


def test_add_newspaper_same_id_should_raise_error(agency):
    before = len(agency.newspapers)
    new_paper = Newspaper(paper_id=999,
                          name="Simpsons Comic",
                          frequency=7,
                          price=3.14)


    agency.add_newspaper(new_paper)

    new_paper2 = Newspaper(paper_id=999,
                          name="Superman Comic",
                          frequency=7,
                          price=13.14)


    with pytest.raises(AssertionError, match='Newspaper with this id already exists'):

       agency.add_newspaper(new_paper2)

def test_get_newspaper(agency):
    new_paper = Newspaper(paper_id=44,
                          name="The Star",
                          frequency=12,
                          price=2.04)

    agency.add_newspaper(new_paper)
    assert agency.get_newspaper(44) == new_paper


def test_all_newspapers(agency):

    paper = Newspaper(paper_id=44,
                      name="The Star",
                      frequency=12,
                      price=2.04)

    agency.add_newspaper(paper)
    assert len(agency.all_newspapers()) == len(agency.newspapers)


def test_remove_newspaper(agency):
    newspaper = Newspaper(paper_id=18,
                            name="Simpsons Comic",
                            frequency=7,
                            price=3.14)

    agency.add_newspaper(newspaper)
    before = len(agency.newspapers)
    agency.remove_newspaper(newspaper)
    assert len(agency.all_newspapers()) == before - 1

def test_add_sub(agency):
    before = len(agency.subscribers)
    new_sub = Subscriber(sub_id=999,
                         subname="Simpsons Comic",
                         subaddy="No 14b USJ4/4C")
    agency.add_sub(new_sub)
    assert len(agency.all_subscribers()) == before + 1


def test_add_sub_same_id_should_raise_error(agency):
    before = len(agency.subscribers)
    new_sub = Subscriber(sub_id=9,
                         subname="Jesus Christ",
                         subaddy="Heaven")


    agency.add_sub(new_sub)

    new_sub2 = Subscriber(sub_id=9,
                          subname="Johhny Cola",
                          subaddy=" Sunway Pyramid")


    with pytest.raises(AssertionError, match='Subscriber with this id already exists.'):

       agency.add_sub(new_sub2)

def test_get_sub(agency):
    new_sub = Subscriber(sub_id=55,
                         subname="Damien Yu",
                         subaddy="Empire Shopping Gallery")

    agency.add_sub(new_sub)
    assert agency.get_sub(55) == new_sub

def test_all_subscribers(agency):

    sub = Subscriber(sub_id=55,
                         subname="Damien Yu",
                         subaddy="Empire Shopping Gallery")
    agency.add_sub(sub)

    assert len(agency.all_subscribers()) == len(agency.subscribers)

def test_remove_sub(agency):
    sub = Subscriber(sub_id=99,
                    subname="Simpsons Comic",
                    subaddy="No 14b USJ4/4C")

    agency.add_sub(sub)
    before = len(agency.subscribers)
    agency.remove_sub(sub)
    assert len(agency.all_subscribers()) == before - 1




def test_add_editor(agency):
    before = len(agency.editors)
    new_editor = Editor(editor_id=99,
                        editorname="Jinn",
                        editoraddress="USJ 2 Park Avenue")
    agency.add_editor(new_editor)
    assert len(agency.all_editors()) == before + 1



def test_add_editor_same_id_should_raise_error(agency):
    before = len(agency.editors)
    new_editor = Editor(editor_id=32,
                         editorname="Uncle Roger",
                         editoraddress="Uncle Soons Fried Rice") # THE BEST FRIED RICE IN MALAYSIA, "NAY" THE WORLD AND ILL FIGHT ANYONE WHO DISAGREES


    agency.add_editor(new_editor)

    new_editor2 = Editor(editor_id=32,
                          editorname="Tan Sun Seng",
                          editoraddress="Sri Kuala Lumpur International School")


    with pytest.raises(AssertionError, match='Editor with this id already exists.'):
       agency.add_editor(new_editor2)



def test_get_editor(agency):
    new_editor = Editor(editor_id=12,
                        editorname="Ben",
                        editoraddress="Alauntalstrase 97, 35001 Kaiserslautern")
    agency.add_editor(new_editor)
    assert agency.get_editor(12) == new_editor



def test_all_editors(agency):

    editor = Editor(editor_id=12,
                    editorname="Ben",
                    editoraddress="Alauntalstrase 97, 35001 Kaiserslautern")
    agency.add_editor(editor)

    assert len(agency.all_editors()) == 1

def test_remove_editor(agency):
    editor = Editor(editor_id=12,
                    editorname="Ben",
                    editoraddress="Alauntalstrase 97, 35001 Kaiserslautern")
    agency.add_editor(editor)

    before = len(agency.editors)

    agency.remove_editor(editor)

    assert len(agency.all_editors()) == before - 1







