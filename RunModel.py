import InputData as D
import ParameterClasses as P
import Support as Support
import MarkovModelClasses as Cls

# selected therapy
therapy = P.Therapies.NONE

# create a cohort
myCohort = Cls.Cohort(id=1,
                      pop_size=D.POP_SIZE,
                      parameters=P.ParametersFixed(therapy=therapy))

# simulate the cohort over the specified time steps
myCohort.simulate(n_time_steps=D.SIM_TIME_STEPS)


# print the outcomes of this simulated cohort
Support.print_outcomes(sim_outcomes=myCohort.cohortOutcomes,
                       therapy_name=therapy)

# selected therapy
therapy = P.Therapies.CASH_INCENTIVES

# create a cohort
myCohort = Cls.Cohort(id=1,
                      pop_size=D.POP_SIZE,
                      parameters=P.ParametersFixed(therapy=therapy))

# simulate the cohort over the specified time steps
myCohort.simulate(n_time_steps=D.SIM_TIME_STEPS)


# print the outcomes of this simulated cohort
Support.print_outcomes(sim_outcomes=myCohort.cohortOutcomes,
                       therapy_name=therapy)


# print comparative outcomes
Support.print_comparative_outcomes(sim_outcomes_none=cohort_none.cohortOutcomes,
                                   sim_outcomes_treat=cohort_treat.cohortOutcomes)

# report the CEA results
Support.report_CEA_CBA(sim_outcomes_none=cohort_none.cohortOutcomes,
                       sim_outcomes_treat=cohort_treat.cohortOutcomes)