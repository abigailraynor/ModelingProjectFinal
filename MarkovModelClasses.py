import SimPy.RandomVariantGenerators as RVGs
from InputData import HealthState
import ParameterClasses as P
import SimPy.SamplePathClasses as PathCls
import SimPy.EconEvalClasses as Econ
import SimPy.StatisticalClasses as Stat


class Patient:
    def __init__(self, id, parameters):

        self.id = id
        self.rng = RVGs.RNG(seed=id)
        self.params = parameters
        self.stateMonitor = PatientStateMonitor(parameters=parameters)

    def simulate(self, n_time_steps):

        t = 0

        # while self.stateMonitor.get_if_alive() and t < n_time_steps:
        while t < n_time_steps:

            # find the transition probabilities to future states
            trans_probs = self.params.probMatrix[self.stateMonitor.currentState.value]

            # create an empirical distribution
            empirical_dist = RVGs.Empirical(probabilities=trans_probs)

            # sample from the empirical distribution to get a new state
            new_state_index = empirical_dist.sample(rng=self.rng)

            # update health state
            self.stateMonitor.update(time_step=t, new_state=P.HealthStates(new_state_index))

            # increment time
            t += 1


class PatientStateMonitor:
    def __init__(self, parameters):

        self.currentState = parameters.initialHealthState   # assuming everyone starts in "Well"
        self.survivalTime = None
        self.nCured = 0
        self.costUtilityMonitor = PatientCostUtilityMonitor(parameters=parameters)

    def update(self, time_step, new_state):
        """
        update the current health state to the new health state
        :param time_step: current time step
        :param new_state: new state
        """
        # IF THE PATIENT IS INCOMPLETE, DO NOTHING
        # if self.currentState == P.HealthStates.INCOMPLETE:
        #     return

        # IF THE PATIENT IS CURED, COUNT AS A CURED CASE
        if self.currentState == P.HealthStates.CURED:
            self.nCured += 1

        # update cost and utility
        self.costUtilityMonitor.update(k=time_step,
                                       current_state=self.currentState,
                                       next_state=new_state)

        # update current health state
        self.currentState = new_state

    # def get_if_alive(self):
    #     """ returns true if the patient is still alive """
    #     if self.currentState == P.HealthStates.INCOMPLETE or self.currentState == P.HealthStates.CURED or \
    #             self.currentState == P.HealthStates.INCOMPLETE or self.currentState == P.HealthStates.WELL:
    #         return True
    #     else:
    #         return False


class PatientCostUtilityMonitor:

    def __init__(self, parameters):

        # model parameters for this patient
        self.params = parameters

        # total cost and utility
        self.totalDiscountedCost = 0
        # self.totalDiscountedUtility = 0

    def update(self, k, current_state, next_state):
        """ updates the discounted total cost and health utility
        :param k: simulation time step
        :param current_state: current health state
        :param next_state: next health state
        """

        # update cost
        cost = (self.params.annualTotalCosts[current_state.value] + self.params.annualTotalCosts[next_state.value])
        # # update utility
        # utility = 0.5 * (self.params.annualTotalUtility[current_state.value] +
        #                  self.params.annualTotalUtility[next_state.value])

        # add the cost of treatment
        if next_state == P.HealthStates.ACTIVE_TB:
        #     cost += 0.5 * self.params.annualTreatmentCost
        # else:
            cost += 1 * self.params.annualTreatmentCost

        # update total discounted cost and utility (corrected for the half-cycle effect)
        self.totalDiscountedCost += Econ.pv_single_payment(payment=cost,
                                                           discount_rate=self.params.discountRate,
                                                           discount_period=k + 1)

        # self.totalDiscountedUtility += Econ.pv_single_payment(payment=utility,
        #                                                       discount_rate=self.params.discountRate / 2,
        #                                                       discount_period=2 * k + 1)


class Cohort:
    def __init__(self, id, pop_size, parameters):
        self.id = id
        self.patients = []
        self.initialPopSize = pop_size
        self.cohortOutcomes = CohortOutcomes()

        for i in range(pop_size):
            patient = Patient(id=id*pop_size + i, parameters=parameters)
            self.patients.append(patient)

    def simulate(self, n_time_steps):

        for patient in self.patients:
            patient.simulate(n_time_steps)

        self.cohortOutcomes.extract_outcomes(self.patients)


class CohortOutcomes:
    def __init__(self):

        self.survivalTimes = []
        self.nTotalCured = []
        self.costs = []
        # self.utilities = []
        self.nLivingPatients = None

        self.statCost = None
        # self.statUtility = None
        # self.statSurvivalTime = None
        self.statCured = None

    def extract_outcomes(self, simulated_patients):
        for patient in simulated_patients:
            if not (patient.stateMonitor.survivalTime is None):
                self.survivalTimes.append(patient.stateMonitor.survivalTime)
            self.nTotalCured.append(patient.stateMonitor.nCured)
            self.costs.append(patient.stateMonitor.costUtilityMonitor.totalDiscountedCost)
            # self.utilities.append(patient.stateMonitor.costUtilityMonitor.totalDiscountedUtility)

        self.statCost = Stat.SummaryStat("Discounted cost", self.costs)
        self.statCured = Stat.SummaryStat("Change in number cured", self.nTotalCured)


        # # survival curve
        # self.nLivingPatients = PathCls.PrevalencePathBatchUpdate(
        #     name='# of living patients',
        #     initial_size=len(simulated_patients),
        #     times_of_changes=self.survivalTimes,
        #     increments=[-1] * len(self.survivalTimes)
        # )

