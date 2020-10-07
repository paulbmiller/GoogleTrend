"""
Module to get google trends using pytrends.
"""

import pandas as pd
from pytrends.request import TrendReq
from pytrends import dailydata


def by_region(kw_list, draw=True, drop_0=True, **kwargs):
    """
    Fetches the DataFrame of the Google Trend for a list of keywords. By
    default, it will drop 0 values and will draw the plot.

    Parameters
    ----------
    kw_list : list
        List of keywords to search.
    draw : bool, optional
        Draw the bar plot for the keywords or not. The default is True.
    drop_0 : bool, optional
        Drop empty rows. The default is True.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the keywords as columns and the country as index.

    """
    pytrend = TrendReq()
    
    pytrend.build_payload(kw_list=kw_list, **kwargs)
    
    df = pytrend.interest_by_region()
    
    if drop_0:
        df = df.loc[(df!=0).any(axis=1)]
    if draw:
        df.plot(kind='bar')
    return df


def over_time(kw_list, draw=True, **kwargs):
    """
    Fetches the DataFrame of the Google Trend for a list of keywords. By
    default, it will draw the plot.

    Parameters
    ----------
    kw_list : list
        List of keywords to search.
    draw : bool, optional
        Draw the bar plot for the keywords or not. The default is True.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the keywords as columns and the country as index.

    """
    pytrend = TrendReq()
    
    pytrend.build_payload(kw_list=kw_list, **kwargs)
    
    df = pytrend.interest_over_time()
    
    df = df.drop('isPartial', axis=1)
    
    if draw:
        df.plot()
    
    return df



