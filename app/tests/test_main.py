import pytest

from ..main import main, Genre, Actor


@pytest.mark.django_db
def test_main():
    users = main()
    assert list(users.values_list("name", "surname")) == [
        ("Jaden", "Smith"),
        ("Will", "Smith"),
    ]


@pytest.mark.django_db
def test_genres():
    main()
    assert list(Genre.objects.values_list("name")) == [
        ("Western",),
        ("Drama",),
    ]


@pytest.mark.django_db
def test_actors():
    main()
    assert list(Actor.objects.values_list("name", "surname")) == [
        ("George", "Clooney"),
        ("Keanu", "Reeves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
    ]
