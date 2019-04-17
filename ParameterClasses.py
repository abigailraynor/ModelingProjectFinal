from enum import Enum
import InputData as Data


class HealthStates(Enum):
    """ health states of patients with primary tuberculosis infections """
    WELL = 0
    ACTIVE_TB = 1
    CURED = 2
    INCOMPLETE = 3


class Therapies(Enum):
    COUNSELING = 3
    CASH_INCENTIVES = 1
    HOME_VISITS = 2
    NONE = 0


class ParametersFixed:
    def __init__(self, therapy):

        # selected therapy
        self.therapy = therapy

        # initial health state
        self.initialHealthState = HealthStates.WELL

        # annual treatment cost
        if self.therapy == Therapies.NONE:
            self.annualTreatmentCost = Data.STANDARD_OF_CARE
        else:
            self.annualTreatmentCost = Data.CASH_INCENTIVES

        # transition probability matrix of the selected therapy
        self.probMatrix = []

        # calculate transition probabilities between stroke states
        if self.therapy == Therapies.NONE:
            # calculate transition probability matrix for the stroke therapy
            self.probMatrix = get_prob_matrix_standard()

        else:
            # calculate transition probability matrix for the cash incentive intervention
            self.probMatrix = get_prob_matrix_cash()

        # annual state costs and utilities
        self.annualTotalCosts = Data.ANNUAL_COST_MATRIX

        # discount rate
        self.discountRate = Data.DISCOUNT


def get_prob_matrix_standard():

    return Data.STANDARD_OF_CARE_MATRIX


def get_prob_matrix_cash():

    return Data.CASH_INCENTIVE_MATRIX


def get_prob_matrix_home():

    return Data.HOME_VISITS_MATRIX
