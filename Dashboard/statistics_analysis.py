from scipy.stats import ttest_ind, mannwhitneyu
# import data_process as dp

def stat_analysis(stat_model_name, data_frame):
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
    print('Hello from stat analysis', stat_model_name)
    treated = data_frame[data_frame['Sample_type'] == 'Treated'].iloc[:, :6].T
    treated.rename(columns = {0: 'Treated'},inplace = True)
    
    control = data_frame[data_frame['Sample_type'] == 'Control'].iloc[:, :6].T
    control.rename(columns = {1: 'Control'},inplace = True)
    print(treated,control)
    if stat_model_name == 'Two-sample t-test':

        t_statistical_value, p_value = ttest_ind(treated['Treated'], control['Control'])
        print(t_statistical_value, p_value)
        return t_statistical_value, p_value
    elif stat_model_name == 'Mann-Whitney U':
        u_statistical_value, p_value = mannwhitneyu(treated['Treated'], control['Control'])
        print(u_statistical_value, p_value)
        return u_statistical_value, p_value
        
# df = dp.return_dataframe('Sagrotan')
# print(stat_analysis('Two-sample t-test', df))
# print(stat_analysis('Two-sample t-test', df))