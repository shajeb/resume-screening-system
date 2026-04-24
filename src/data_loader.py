import pandas as pd
import os
from pathlib import Path
from .exceptions import DataLoadingError

print('Data loader is being imported')

def read_resumes(folder_path):
    try:
        details=[]
        for file in os.listdir(folder_path):
            file_path=Path(os.path.join(folder_path, file))
            file_name=file_path.stem
            
            res_id, can_name=file_name.split('_',1)
            with open(file_path, 'r') as f:
                text=f.read()

            d={'resume_id':res_id,'candidate_name':can_name, 'resume_details':text}
            details.append(d)
        df=pd.DataFrame(details)
        df.resume_id=df.resume_id.astype(int)
        df=df.sort_values(by='resume_id', ignore_index=True)
        return df
    except Exception as e:
        raise DataLoadingError('Data could not be loaded', e)
    


def read_jds(folder_path):
    try:
        details=[]
        for file in os.listdir(folder_path):
            file_path=Path(os.path.join(folder_path, file))
            file_name=file_path.stem
            
            res_id, can_name=file_name.split('_',1)
            with open(file_path, 'r') as f:
                text=f.read()

            d={'jd_id':res_id,'job_description_title':can_name, 'job_description_details':text}
            details.append(d)
        df=pd.DataFrame(details)
        df.jd_id=df.jd_id.astype(int)
        df=df.sort_values(by='jd_id', ignore_index=True)
        return df
    except Exception as e:
        raise DataLoadingError('Data could not be loaded', e)
        print(e)