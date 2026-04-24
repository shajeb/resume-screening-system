from .utils import save_json
from .exceptions import PipelineFailedError
from .llm_call import make_api_call
import pandas as pd
from pathlib import Path


def screening_pipeline(client, 
                       system_prompt, 
                       screening_class,
                       model, 
                       res_df,
                       job_des, 
                       output_path, 
                       llm_result_path):
    
    if res_df is None or res_df.empty:
        raise PipelineFailedError('Empty or None Data Frame')
    
    print(f'Total Resumes to be processed- {len(res_df)}\n')
    total=0
    final_json={}
    final_results=[]
    for row in res_df.itertuples():
        try:
            res_id=int(row.resume_id)
            text=row.resume_details
            print(f"The resume id- {res_id} has started")
            
            result=make_api_call(client=client,
                                 system_prompt=system_prompt,
                                 text=text,
                                 job_des=job_des,
                                 model=model,
                                 screening_class=screening_class)
            
            result_per_id={'resume_id':res_id}
            result_per_id.update(result)
            final_results.append(result_per_id)
            final_json[res_id]=result_per_id

            res_path=llm_result_path / f"{res_id}.json"
            save_json(res_path, result_per_id)
            total=total+1
            print(f"COMPLETED- {total}", end=', ')
            
        except Exception as e:
            print(f'Resume_ID- {res_id} got some error while processing!')
            print(e)

    try:
        final_df=pd.DataFrame(final_results)
    except:
        print('Issue in creating the finl data frame')
        final_df=pd.DataFrame()

    # Saving Results
    try:
        final_dict_path=output_path / 'final_result.json'
        save_json(final_dict_path, final_json)
        print('Intermediate results are saved')
        if final_df.empty or final_df is None:
            raise ValueError("Empty Results Data frame ")
        output_file_name=Path(output_path) / "resume_screening_details.xlsx"
        final_df.to_excel(output_file_name, index=False)
        print(f'Results are saved to the following path- {output_file_name}')
        print('\n====================Pipeline Completed====================')
    except:
        print('Error in saving the results to excel!')
        raise PipelineFailedError('The Pipeline aborted because of some error')