import math


def calculate_reliability(failure_rate, operational_time):
    reliability = math.exp(-1 * failure_rate * operational_time)
    return reliability


def calculate_the_highest_failure_rate(reliability, hours):
    natural_log = -1 * math.log(reliability)
    result = natural_log / hours
    return result


def calculate_failure_rate(mtbf):
    failure_rate = 1 / mtbf
    return failure_rate


def print_reliability_function(reliability):
    print(f'The reliability function: R(t) = e^(-({reliability} * t))')


def calculate_reliability_for_two_series_connected_components(reliability_d, reliability_e):
    result = reliability_d * reliability_e
    return result


def calculate_reliability_for_three_parallel_connected_components(reliability_a, reliability_b, reliability_c):
    result = 1 - (1 - reliability_a) * (1 - reliability_b) * (1 - reliability_c)
    return result


def calculate_total_system_reliability(reliability_for_parallel_connected_components,
                                       reliability_for_series_connected_components):
    result = reliability_for_parallel_connected_components * reliability_for_series_connected_components
    return result


