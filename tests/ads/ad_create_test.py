import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category):

    expected_response = {
        'id': user.id,
        'name': 'Test 10 characters minimum',
        'author': user.username,
        'price': 2500,
        'description': 'Test description',
        'is_published': False,
        'image': None,
        'category': category.name
    }

    data = {
        'author_id': user.id,
        'name': 'Test 10 characters minimum',
        'price': 2500,
        'description': 'Test description',
        'is_published': False,
        'image': None,
        'category_id': category.id
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_price(client, user, category):

    expected_response = {
        'price': ['Ensure this price is more or equal to 0']

    }

    data = {
        'author_id': user.id,
        'name': 'Test 10 characters minimum',
        'price': -1,
        'description': 'Test description',
        'is_published': False,
        'image': None,
        'category_id': category.id
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_is_published(client, user, category):

    expected_response = {
        'is_published': ['This field may not be True']
    }

    data = {
        'author_id': user.id,
        'name': 'Test 10 characters minimum',
        'price': 2500,
        'description': 'Test description',
        'is_published': False,
        'image': None,
        'category_id': category.id
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response


@pytest.mark.django_db
def test_ad_create_name_less_10_characters(client, user, category):
    expected_response = {
        'name': ['This field may have at least 10 characters.']
    }

    data = {
        'author_id': user.id,
        'name': 'Test',
        'price': 2500,
        'description': 'Test description',
        'is_published': False,
        'category_id': category.id
    }

    response = client.post(
        '/ad/create/',
        data,
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.data == expected_response

