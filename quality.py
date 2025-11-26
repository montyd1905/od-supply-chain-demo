from typing import Tuple, List, Union
from models import haversine_distance, sum_qf, sum_cf
from math import log10

LocationType = Tuple[float, float]
QuantitativePropertiesType = List[Union[float, int]]
CategoricalPropertiesType = List[str]

timeliness_weight = 0.5  # increase this if timeliness is more important than accuracy
accuracy_weight = 1 - timeliness_weight


def quality_score(
    user_location: LocationType,
    provider_location: LocationType,
    user_search_parameters: Tuple[
        QuantitativePropertiesType, CategoricalPropertiesType
    ],
    dynamic_provider_parameters: Tuple[
        QuantitativePropertiesType, CategoricalPropertiesType
    ],
) -> float:
    """
    Calculate the quality score for a given POS provider relative to a user's search request

    :param user_location: lat, long coordinate pair for the user
    :param provider_location: lat, long coordinate pair for the provider
    :param user_search_parameters: collection of quantitative and categorical user search parameters
    :param dynamic_provider_parameters: collection of corresponding quantitative and categorical POS provider values
    :return: a float representing the match quality of the POS provider relative to the user's order.
             The higher this value, the better the match
    """

    distance = haversine_distance(*user_location, *provider_location)

    user_quantitative_params, user_categorical_params = user_search_parameters
    (
        provider_quantitative_params,
        provider_categorical_params,
    ) = dynamic_provider_parameters

    _sum_qf = sum_qf(user_quantitative_params, provider_quantitative_params)
    _sum_cf = sum_cf(user_categorical_params, provider_categorical_params)

    sum_product = _sum_qf * _sum_cf
    weight_product = timeliness_weight * accuracy_weight

    weight_adjusted_product = sum_product**weight_product
    normalized_weight_adjusted_product = log10(weight_adjusted_product)

    qs = normalized_weight_adjusted_product / distance

    return qs
