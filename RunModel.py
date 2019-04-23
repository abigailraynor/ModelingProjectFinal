import InputData as D
import ParameterClasses as P
import Support as Support
import MarkovModelClasses as Cls

'PRINT ESTIMATES'
# selected STANDARD therapy
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

# selected COST INCENTIVE therapy
therapy = P.Therapies.COUNSELING

# create a cohort
myCohort = Cls.Cohort(id=1,
                      pop_size=D.POP_SIZE,
                      parameters=P.ParametersFixed(therapy=therapy))

# simulate the cohort over the specified time steps
myCohort.simulate(n_time_steps=D.SIM_TIME_STEPS)


# print the outcomes of this simulated cohort
Support.print_outcomes(sim_outcomes=myCohort.cohortOutcomes,
                       therapy_name=therapy)

" RUN COMPARATIVE OUTCOMES"

# simulating mono therapy
# create a cohort
cohort_none = Cls.Cohort(id=0,
                         pop_size=D.POP_SIZE,
                         parameters=P.ParametersFixed(therapy=P.Therapies.NONE))
# simulate the cohort
cohort_none.simulate(n_time_steps=D.SIM_TIME_STEPS)

# simulating combination therapy
# create a cohort
cohort_treat = Cls.Cohort(id=1,
                          pop_size=D.POP_SIZE,
                          parameters=P.ParametersFixed(therapy=P.Therapies.COUNSELING))
# simulate the cohort
cohort_treat.simulate(n_time_steps=D.SIM_TIME_STEPS)

# print the estimates for the mean survival time and mean time to AIDS
Support.print_outcomes(sim_outcomes=cohort_none.cohortOutcomes,
                       therapy_name=P.Therapies.NONE)
Support.print_outcomes(sim_outcomes=cohort_treat.cohortOutcomes,
                       therapy_name=P.Therapies.COUNSELING)


# print comparative outcomes
Support.print_comparative_outcomes(sim_outcomes_none=cohort_none.cohortOutcomes,
                                   sim_outcomes_treat=cohort_treat.cohortOutcomes)

' GENERATE COST EFFECTIVE ANALYSIS'
# report the CEA results
Support.report_CEA_CBA(sim_outcomes_none=cohort_none.cohortOutcomes,
                       sim_outcomes_treat=cohort_treat.cohortOutcomes)

