import pytest
from src.core.domain.value_objects.ratings import Ratings


@pytest.mark.parametrize(
    "value, scale, result",
    [
        (93, 100, 9.3),
        (78, 100, 7.8),
        (33, 100, 3.3),
        (8.2, 10, 8.2),
        (5, 10, 5.0),
        (4.8, 5, 9.6),
        (3.3, 5, 6.6),
        (2.75, 5, 5.5),
    ]
)
def test_normalize_ratings(value, scale, result):
    value_rating = Ratings.normalize(value, scale)
    assert value_rating == result


@pytest.mark.parametrize(
    "value, scale, exception",
    [
        (8, 5, ValueError),
        (78, 10, ValueError),
    ]
)
def test_ratings_errors(value, scale, exception):
    with pytest.raises(
        exception,
        match=f'The rating must be between 0 and {scale}'
    ):
        Ratings.normalize(value, scale)
