from random import sample
import pandas as pd


def create_dataframe(path, widths, columns):
    """Create the dataframe of raw data

    Args:
        path (string): path to the txt file of raw data
        widths (list): column widths
        columns (list): column names
        
    path = './raw_data/Falen.txt'
    df = pd.read_fwf(path, widths=[29,4,7,8,7,11,9,6])
    df.columns = ['datetime', 'lane', 'speed', 'length', 'class', 'gap', 'wrong_dir', 'display']
    """
    path = './raw_data/Falen.txt'
    df = pd.read_fwf(path, widths=widths)
    df.columns = columns
    return df

def create_speed_list(df, areaname):
    """generates the arrays containing speeds in a time interval t.

    Args:
        df (DataFrame): DataFrame retrieved from create_dataframe() function
        areaname (string): name of the location

    Returns:
        list of list: list containing speed lists.
    """
    df['datetime'] = pd.to_datetime(df['datetime'])
    index = list(df.groupby(pd.Grouper(key='datetime', freq='60min')).groups.values())
    k=0
    lst = []
    speed_list = []
    for i in range(0, len(index)):
        for speed in range(k, index[i]):
            lst.append(df['speed'][speed])
        k = index[i]
        speed_list.append(lst)
        lst = []
        
    for i in speed_list:
        if len(i) <= 5:
            speed_list.remove(i)
    # data = pd.DataFrame(df.groupby(pd.Grouper(key='datetime', freq='60min')).count()['speed'])
    # data.columns = ['number of cars']
    # data['speed_list'] = speed_list
    # data['area'] = areaname
    # data = data[data['number of cars'] > 5]
    
    return speed_list

# sample = create_speed_list(df, areaname)