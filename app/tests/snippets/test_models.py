import pytest

from snippets.models import Snippet, CustomUser, Tag

@pytest.mark.django_db
def test_user_model():
    user = CustomUser(username="user1", email="user1@test.com", first_name="User", last_name="Doe")
    user.save()

    assert user.username == "user1"
    assert str(user) == "user1"

@pytest.mark.django_db
def test_tags_model():
    tag = Tag(tag='peace')
    tag.save()
    assert tag.tag == 'peace'


@pytest.mark.django_db
def test_snippets_model():
    user = CustomUser(username="user1", email="user1@test.com", first_name="User", last_name="Doe")
    user.save()

    tag = Tag(tag='peace')
    tag.save()
    
    payload = {
        'title': 'title of snippet',
        'text': 'text of the snippet',
        'author': user,
    }

    snippet = Snippet(**payload)
    snippet.save()
    snippet.tags.add(tag)
    snippet.save()
    assert snippet.title == payload['title']
    assert snippet.text == payload['text']
    assert len(snippet.tags.all()) == 1
    assert snippet.tags.all()[0].tag == "peace"
    assert snippet.author == payload['author']
