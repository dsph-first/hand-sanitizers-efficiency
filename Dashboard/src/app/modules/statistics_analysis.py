from scipy.stats import ttest_ind, mannwhitneyu


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

    print('Hello from stat analysis', len(stat_model_name))
    # let's add some requirements on the input data
    # if data_frame == None or 'Empty' in stat_model_name or stat_model_name == None:
    #     print('XXXXXXX')
    #     return None, None

    treated = data_frame[data_frame['sample_type'] == 'Treated'].iloc[:, :6].T
    print('treated: ', treated)
    treated.rename(columns={0: 'Treated'}, inplace=True)

    control = data_frame[data_frame['sample_type'] == 'Control'].iloc[:, :6].T
    control.rename(columns={1: 'Control'}, inplace=True)
    print("CONTROL: ", control)
    print("=================================================")
    print(treated['Treated'], control['Control'])
    print("=================================================")
    if stat_model_name == 'Two-sample t-test':
        t_statistical_value, p_value = ttest_ind(
            treated['Treated'], control['Control'])
        print(t_statistical_value, p_value)
        return t_statistical_value, p_value
    elif stat_model_name == 'Mann-Whitney U':
        u_statistical_value, p_value = mannwhitneyu(
            treated['Treated'], control['Control'])
        print(u_statistical_value, p_value)
        return u_statistical_value, p_value

# df = dp.return_dataframe('Sagrotan')
# print(stat_analysis('Two-sample t-test', df))
# print(stat_analysis('Two-sample t-test', df))
