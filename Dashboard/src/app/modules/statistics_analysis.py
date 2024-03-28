from scipy.stats import ttest_ind, mannwhitneyu, anderson
import pandas as pd


def normality_check(data_frame=None):
    """_summary_

    Args:
        data_frame (pandas dataframe): A handsanitizer  or control dataframe which we want to check
                                     which distribution it follows.
    Return:
    stat_model_name (string) : Returns a statistical model name based on p_value of the Anderson Darling normality
                               test
    """
    print(data_frame)
    treated, control = get_treated_control_df(data_frame)
    res_treated = anderson(treated['Treated'])
    res_control = anderson(control['Control'])
    if (res_treated.statistic and res_control.statistic) > 0.05:
        stat_model_name = 'Mann-Whitney U'
        return stat_model_name

    if (res_treated.statistic and res_control.statistic) < 0.05:
        stat_model_name = 'Two-sample t-test'
        return stat_model_name


def stat_analysis(stat_model_name=None, data_frame=None):
    '''

    This function takes the name of the statistical model, the dataframe
    and returns the p_value and t statistical value or U statistical value depends on the stat model name.

    Parameter:
    Input:
    stat_model_name: The name of a stat model. It is a string
    Data_frame: Data frame contains the sample data for treated which means
                used hand sanitizer on that finger  and control of the finger pad experiments.
    Returns: It returns the p_value and t statistical value / u statistical value depends on the
             name on the stat model. Both of them are float

    '''
    treated, control = get_treated_control_df(data_frame)

    if stat_model_name == 'Two-sample t-test':
        t_statistical_value, p_value = ttest_ind(
            treated['Treated'], control['Control'])
        return t_statistical_value, p_value
    elif stat_model_name == 'Mann-Whitney U':
        u_statistical_value, p_value = mannwhitneyu(
            treated['Treated'], control['Control'])
        return u_statistical_value, p_value


def get_treated_control_df(data_frame):
    """_summary_

    Args:
        data_frame (pandas dataframe): It takes the dataframe and process this to divide it into treated and control

    Returns:
        treated:This is the dataframe for the participants who used hand sanitizer
        control: This is the dataframe for the participants for control
    """

    treated = data_frame[data_frame['Sample_type'] == 'Treated'].iloc[:, :6].T
    treated.rename(columns={0: 'Treated'}, inplace=True)

    control = data_frame[data_frame['Sample_type'] == 'Control'].iloc[:, :6].T
    control.rename(columns={1: 'Control'}, inplace=True)

    return treated, control
