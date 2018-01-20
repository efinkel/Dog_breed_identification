import os
import pandas as pd
import warnings
def organize_groups(df, breed, fformat = 'jpg'):
    """ 
    convenience function to create folder for each group and move appropriate files.
    df should have 'id' column containing file names of data files and 'breed'
    column labeling which group each file belongs to 
    """
    try:
        os.mkdir(breed)
    except:
        print('directory already created')
             
    ids = df.loc[df['breed'] == breed, 'id']
    cwd = os.getcwd()
    
    for filename in ids:
        curr_path = cwd+'/'+filename+'.'+fformat
        future_path = cwd+'/'+breed+'/'+filename+'.'+fformat
        
        if os.path.isfile(future_path):
            continue
        else:
            os.rename(curr_path, future_path)