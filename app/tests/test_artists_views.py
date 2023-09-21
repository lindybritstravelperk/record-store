import pytest

from rest_framework.test import APIClient
from rest_framework import status

from artists.models import Artist, Track

client = APIClient()


def describe_artists():
    def describe_get():
        @pytest.mark.django_db
        def empty_artists():
            res = client.get("/artists/")
            assert res.data == []
            assert res.status_code == 200

        @pytest.mark.django_db
        def all_artists():
            Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.get("/artists/")
            assert res.status_code == status.HTTP_200_OK
            assert res.data == [
                {"id": 1, "first_name": "John", "last_name": "Lennon", "tracks": []}
            ]

        @pytest.mark.django_db
        def query_by_artist_name():
            Artist.objects.create(first_name="John", last_name="Lennon")
            Artist.objects.create(first_name="Paul", last_name="McCartney")
            res = client.get("/artists/?name=John")
            assert res.status_code == status.HTTP_200_OK
            assert res.data == [
                {"id": 1, "first_name": "John", "last_name": "Lennon", "tracks": []}
            ]

    def describe_post():
        @pytest.mark.django_db
        def without_tracks_in_payload():
            res = client.post(
                "/artists/",
                {"first_name": "John", "last_name": "Lennon", "tracks": []},
                format="json",
            )
            assert res.status_code == status.HTTP_201_CREATED
            assert res.data == {
                "id": 1,
                "first_name": "John",
                "last_name": "Lennon",
                "tracks": [],
            }

        @pytest.mark.django_db
        def with_tracks_in_payload():
            res = client.post(
                "/artists/",
                {
                    "first_name": "John",
                    "last_name": "Lennon",
                    "tracks": [{"title": "let it be"}],
                },
                format="json",
            )
            assert res.status_code == status.HTTP_201_CREATED
            assert res.data == {
                "id": 1,
                "first_name": "John",
                "last_name": "Lennon",
                "tracks": [{"title": "let it be"}],
            }


def describe_artist_detail():
    def describe_get():
        @pytest.mark.django_db
        def test_artist_detail():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.get(f"/artists/{artist.id}")
            assert res.status_code == status.HTTP_200_OK
            assert res.data == {
                "id": 1,
                "first_name": "John",
                "last_name": "Lennon",
                "tracks": [],
            }

    def describe_put():
        @pytest.mark.django_db
        def test_all_fields_change():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.put(
                f"/artists/{artist.id}",
                {
                    "first_name": "Foo",
                    "last_name": "Fighters",
                    "tracks": [{"title": "Pretender"}],
                },
                format="json",
            )
            assert res.status_code == status.HTTP_200_OK
            assert res.data == {
                "id": 1,
                "first_name": "Foo",
                "last_name": "Fighters",
                "tracks": [{"title": "Pretender"}],
            }

    def describe_patch():
        @pytest.mark.django_db
        def test_first_name_change():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.patch(
                f"/artists/{artist.id}", {"first_name": "Foo"}, format="json"
            )
            assert res.status_code == status.HTTP_200_OK
            assert res.data == {
                "id": 1,
                "first_name": "Foo",
                "last_name": "Lennon",
                "tracks": [],
            }

        @pytest.mark.django_db
        def test_last_name_change():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.patch(
                f"/artists/{artist.id}", {"last_name": "Foo"}, format="json"
            )
            assert res.status_code == status.HTTP_200_OK
            assert res.data == {
                "id": 1,
                "first_name": "John",
                "last_name": "Foo",
                "tracks": [],
            }

        @pytest.mark.django_db
        def test_with_tracks_in_payload():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.patch(
                f"/artists/{artist.id}",
                {"tracks": [{"title": "let it be"}]},
                format="json",
            )
            assert res.status_code == status.HTTP_200_OK
            assert res.data == {
                "id": 1,
                "first_name": "John",
                "last_name": "Lennon",
                "tracks": [{"title": "let it be"}],
            }

        @pytest.mark.django_db
        def test_without_tracks_in_payload():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")

            Track.objects.create(artist=artist, **{"title": "let it be"})
            res = client.patch(f"/artists/{artist.id}", {"tracks": []}, format="json")
            assert res.status_code == status.HTTP_200_OK
            assert res.data == {
                "id": 1,
                "first_name": "John",
                "last_name": "Lennon",
                "tracks": [],
            }

    def describe_delete():
        @pytest.mark.django_db
        def test_delete_artist():
            artist = Artist.objects.create(first_name="John", last_name="Lennon")
            res = client.delete(f"/artists/{artist.id}")
            assert res.status_code == status.HTTP_204_NO_CONTENT
            assert res.data == None
