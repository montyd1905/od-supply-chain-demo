import pytest

from models import (
    quantitative_factor,
    categorical_factor,
    sum_qf,
    sum_cf,
    haversine_distance,
)
from quality import quality_score

lagos_lat, lagos_long = 6.5244, 3.3792
abuja_lat, abuja_long = 9.0765, 7.3986


def test_quantitative_factor():
    assert quantitative_factor(3, 5) == 0.6826061944859853


def test_categorical_factor():
    assert categorical_factor("red", "blue") == 0
    assert categorical_factor("red", "red") == 1


def test_sum_qf():
    assert sum_qf([3, 1, 5], [5, 1, 3]) == 0.6826061944859853 + 1 + 0.6826061944859853


def test_sum_cf():
    assert sum_cf(["red", "blue", "green"], ["red", "yellow", "green"]) == 1 + 0 + 1


def test_haversine_distance():
    assert (
        haversine_distance(lagos_lat, lagos_long, abuja_lat, abuja_long)
        == 525.8979535468812
    )


def test_quality_score():

    user_location = lagos_lat, lagos_long
    provider_location = abuja_lat, abuja_long

    user_price_preference = 30
    user_provider_rating_preference = 4.8
    user_crust_preference = "regular"
    user_item_type = "pizza:mozzarella"

    user_search_parameters = (
        [user_price_preference, user_provider_rating_preference],
        [user_crust_preference, user_item_type],
    )

    provider_1_price = 32.50
    provider_1_rating = 4.6
    provider_1_crust = "thick"
    provider_1_item_type = "pizza:mozzarella"

    provider_2_price = 31.20
    provider_2_rating = 4.7
    provider_2_crust = "regular"
    provider_2_item_type = "pizza:mozzarella"

    provider_1_parameters = (
        [provider_1_price, provider_1_rating],
        [provider_1_crust, provider_1_item_type],
    )

    provider_2_parameters = (
        [provider_2_price, provider_2_rating],
        [provider_2_crust, provider_2_item_type],
    )

    qs_provider_1 = quality_score(
        user_location,
        provider_location,
        user_search_parameters,
        provider_1_parameters,
    )

    qs_provider_2 = quality_score(
        user_location,
        provider_location,
        user_search_parameters,
        provider_2_parameters,
    )

    assert qs_provider_1 == 0.0001378627126888822
    assert qs_provider_2 == 0.0002836274187406838
    assert qs_provider_2 > qs_provider_1
