from enum import Enum

# simulation settings
POP_SIZE = 5672       # population of south africa
SIM_TIME_STEPS = 50    # length of simulation (years)
DISCOUNT = 0.03
ALPHA = 0.05


class HealthState(Enum):
    """ health states of patients """
    WELL = 0
    ACTIVE_TB = 1
    CURED = 2
    INCOMPLETE = 3


STANDARD_OF_CARE_MATRIX = [
    [0.99468, 0.00532, 0, 0],
    [0, 0, 0.707, 0.293],
    [0, 0, 1.0, 0],
    [0, 0, 0, 1.0]
]

CASH_INCENTIVE_MATRIX = [
    [0.99468, 0.00532, 0, 0],
    [0, 0, 0.812, 0.188],
    [0, 0, 1.0, 0],
    [0, 0, 0, 1.0]
]

HOME_VISITS_MATRIX = [
    [0.99468, 0.00532, 0, 0],
    [0, 0, 0.827, 0.173],
    [0, 0, 1.0, 0],
    [0, 0, 0, 1.0]
]
# Costs
ANNUAL_COST_MATRIX = [
    0,
    294,
    0,
    0,
]

# Potential Treatment Costs
STANDARD_OF_CARE = 0
CASH_INCENTIVES = 90
HOME_VISIT_COSTS = 117
