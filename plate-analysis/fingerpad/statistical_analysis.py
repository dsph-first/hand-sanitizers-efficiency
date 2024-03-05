#!/usr/bin/python3

'''
This file contains statistical analysis tools that are obtained from Emile Apol.
Only the necessary tools that are needed for data analysis of the data from the datasets
that are described in the main script.
'''

def DS_Q_Q_Plot(y, est = 'robust', title = 'Q-Q plot', **kwargs):
    """
    *
    Function DS_Q_Q_Plot(y, est = 'robust', **kwargs)
    
       This function makes a normal quantile-quantile plot (Q-Q-plot), also known
       as a probability plot, to visually check whether data follow a normal distribution.
    
    Requires:            numpy, scipy.stats.iqr, scipy.stats.norm, matplotlib.pyplot
    
    Arguments:
      y                  data array
      est                Estimation method for normal parameters mu and sigma:
                         either 'robust' (default), or 'ML' (Maximum Likelihood),
                         or 'preset' (given values)
      N.B. If est='preset' than the *optional* parameters mu, sigma must be provided:
      mu                 preset value of mu
      sigma              preset value of sigma
      title              Title for the graph (default: 'Q-Q plot')
      
    Returns:
      Estimated mu, sigma, n, and expected number of datapoints outside CI in Q-Q-plot.
      Q-Q-plot
      
    Author:            M.E.F. Apol
    Date:              2020-01-06, revision 2022-08-30, 2023-12-19
    """
    
    import numpy as np
    from scipy.stats import iqr # iqr is the Interquartile Range function
    import matplotlib.pyplot as plt
    from scipy.stats import norm
    
    # First, get the optional arguments mu and sigma:
    mu_0 = kwargs.get('mu', None)
    sigma_0 = kwargs.get('sigma', None)
    
    n = len(y)
    
    # Calculate order statistic:
    y_os = np.sort(y)
  
    # Estimates of mu and sigma:
    # ML estimates:
    mu_ML = np.mean(y)
    sigma2_ML = np.var(y)
    sigma_ML = np.std(y) # biased estimate
    s2 = np.var(y, ddof=1)
    s = np.std(y, ddof=1) # unbiased estimate
    # Robust estimates:
    mu_R = np.median(y)
    sigma_R = iqr(y)/1.349

    # Assign values of mu and sigma for z-transform:
    if est == 'ML':
        mu, sigma = mu_ML, s
    elif est == 'robust':
        mu, sigma = mu_R, sigma_R
    elif est == 'preset':
        mu, sigma = mu_0, sigma_0
    else:
        print('Wrong estimation method chosen!')
        return()
        
    
    # Expected number of deviations (95% confidence level):
    n_dev = np.round(0.05*n)

         
    # Perform z-transform: sample quantiles z.i
    z_i = (y_os - mu)/sigma

    # Calculate cumulative probabilities p.i:
    i = np.array(range(n)) + 1
    p_i = (i - 0.5)/n

    # Calculate theoretical quantiles z.(i):
    z_th = norm.ppf(p_i, 0, 1)

    # Calculate SE or theoretical quantiles:
    SE_z_th = (1/norm.pdf(z_th, 0, 1)) * np.sqrt((p_i * (1 - p_i)) / n)

    # Calculate 95% CI of diagonal line:
    CI_upper = z_th + 1.96 * SE_z_th
    CI_lower = z_th - 1.96 * SE_z_th

    # Make Q-Q plot:
    plt.plot(z_th, z_i, 'o', color='k', label='experimental data')
    plt.plot(z_th, z_th, '--', color='r', label='normal line')
    plt.plot(z_th, CI_upper, '--', color='b', label='95% CI')
    plt.plot(z_th, CI_lower, '--', color='b')
    plt.xlabel('Theoretical quantiles, $z_{(i)}$')
    plt.ylabel('Sample quantiles, $z_i$')
    plt.title(title + ' (' + est + ')')
    plt.legend(loc='best')
    plt.show()
    pass;

def DS_AndersonDarling_test_normal(y, alpha=0.05):
    """
    *
    Function DS_AndersonDarling_test_normal(y, alpha)
    
       This function tests whether the data y follow a normal distribution (Null Hypothesis Significance Test).
    
    Requires:            scipy.stats.anderson
    
    References:          * Th. Anderson & D. Darling (1952) - "Asymptotic Theory of 
                         Certain "Goodness of Fit" Criteria Based on Stochastic Processes".
                         Ann. Math. Statist. 23, 193-212. DOI: 10.1214/aoms/1177729437
                         * R.B. D'Agostino (1986). "Tests for the Normal Distribution"
                         In: R.B. D'Augostino & M.A. Stephens - "Goodness-of-fit
                         techniques", Marcel Dekker.
    
    Arguments:
      y                  data array
      alpha              significance level of the critical value (default: alpha = 0.05)
      
    Usage:               DS_AndersonDarling_test_normal(y, alpha=alpha)
      
      
    Returns:             AD, AD_star, p_value [ + print interpretable output to stdout ]
    where
      AD                 (Large-sample) Anderson-Darling statistic
      AD_star            Small-sample Anderson-Darling statistic
      p_value            p-value of AD-test
      
    Author:            M.E.F. Apol
    Date:              2023-12-05
    """
    
    from scipy.stats import anderson
    import numpy as np
    
    AD = anderson(y, dist='norm').statistic
    n = len(y)
    AD_star = AD*(1 + 0.75/n + 2.25/n**2)
    
    # p-values based on D'Augostino & Stephens (1986):
    if(AD_star <= 0.2): # Eq. (1)
        p_value = 1 - np.exp(-13.436 + 101.14*AD_star - 223.73*AD_star**2)
    elif((AD_star > 0.2) & (AD_star <= 0.34)): # Eq. (2)
        p_value = 1 - np.exp(-8.318 + 42.796*AD_star - 59.938*AD_star**2)
    elif((AD_star > 0.34) & (AD_star < 0.6)): # Eq. (3)
        p_value = np.exp(0.9177 - 4.279*AD_star - 1.38*AD_star**2)
    elif(AD_star >= 0.6): # Eq. (4)
        p_value = np.exp(1.2937 - 5.709*AD_star + 0.0186*AD_star**2)
        
    # Critical AD* values, based on D'Augostino & Stephens (1986):
    # Inverting these relations, we get
    # Invert (1) if alpha > 0.884
    # Invert (2) if 0.50 < alpha < 0.884
    # Invert (3) if 0.1182 < alpha < 0.50
    # Invert (4) if alpha < 0.1182
    
    if(alpha >= 0.884): # Eq. (1a)
        AD_crit = (-101.14+np.sqrt(101.14**2-4*-223.73*(-13.436-np.log(1-alpha))))/(2* -223.73)
    elif((alpha < 0.884) & (alpha >= 0.50)): # Eq. (2a)
        AD_crit = (-42.796+np.sqrt(42.796**2-4* -59.938*(-8.318-np.log(1-alpha))))/(2* -59.938)
    elif((alpha < 0.50) & (alpha >= 0.1182)): # Eq. (3a)
        AD_crit = (4.279-np.sqrt(4.279**2-4* -1.38*(0.9177-np.log(alpha))))/(2* -1.38)
    elif(alpha < 0.1182): # Eq. (4a)
        AD_crit = (5.709-np.sqrt(5.709**2-4*0.0186*(1.2937-np.log(alpha))))/(2*0.0186)
    
    # Additional statistics:
    y_av = np.mean(y)
    s = np.std(y, ddof=1)
    
    if p_value < 0.05:
        print(f'The dataset is not normally distributed! p= {p_value}')
    else:
        print(f'The data is normally distributed! p={p_value}');

def ind_t_test(y1, y2):
    import scipy
    if scipy.stats.ttest_ind(y1,y2)[1] < 0.05:
        print(f'There is a significant difference between control and hand-sanitizers H0 rejected, p={scipy.stats.ttest_ind(y1,y2)[1]}')
    else:
        print(f"There is not a significant different between control and hand-sanitizers H0 is true p={scipy.stats.ttest_ind(y1,y2)[1]}")

def mann_withney(y1, y2):
    import scipy
    if scipy.stats.mannwhitneyu(y1, y2)[1] < 0.05:
        print(f'There is a significant difference between control and hand-sanitizers H0 rejected, p={scipy.stats.mannwhitneyu(y1,y2)[1]}')
    else:
        print(f"There is not a significant different between control and hand-sanitizers H0 is true p={scipy.stats.mannwhitneyu(y1,y2)[1]}")
