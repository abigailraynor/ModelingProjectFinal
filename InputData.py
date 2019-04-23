from enum import Enum

# simulation settings
POP_SIZE = 500      # population of south africa
SIM_TIME_STEPS = 200    # length of simulation (years)
DISCOUNT = 0.03
ALPHA = 0.05


class HealthState(Enum):
    """ health states of patients """
    ACTIVE_UNDIAGNOSED = 0
    ACTIVE_TB = 1
    CURED = 2
    INCOMPLETE = 3


STANDARD_OF_CARE_MATRIX = [
    [0.33, 0.67, 0, 0], # ACTIVE_UNDIAGNOSED
    [0, 0, 0.707, 0.293], #ACTIVE TB
    [0, 0, 1.0, 0], #CURED
    [0, 0, 0, 1.0] #INCOMPLETE
]

CASH_INCENTIVE_MATRIX = [
    [0.33, 0.67, 0, 0],  # ACTIVE_UNDIAGNOSED
    [0, 0, 0.812, 0.188],
    [0, 0, 1.0, 0],
    [0, 0, 0, 1.0]
]

HOME_VISITS_MATRIX = [
    [0.33, 0.67, 0, 0],  # ACTIVE_UNDIAGNOSED
    [0, 0, 0.827, 0.173],
    [0, 0, 1.0, 0],
    [0, 0, 0, 1.0]
]

COUNSELING_MATRIX = [
    [0.33, 0.67, 0, 0],  # ACTIVE_UNDIAGNOSED
    [0, 0, 0.72, 0.18],
    [0, 0, 1.0, 0],
    [0, 0, 0, 1.0]
]

# Costs
ANNUAL_COST_MATRIX = [
    0,
    588,
    0,
    0,
]

# Potential Treatment Costs
STANDARD_OF_CARE = 0
CASH_INCENTIVES = 180
HOME_VISIT_COST = 234
COUNSELING_COST = 61

