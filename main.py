from src.data_loader import read_resumes, read_jds
from src.processor import screening_pipeline
from src.schema import ResumeScreener
from openai import OpenAI
from pathlib import Path
from src.config_reader import (resume_path,
                               jd_path,
                               output_path,
                               project_name,
                               run_id,
                               model,
                               system_prompt,
                               samples)

try:
    print('Pipeline begins....')
    output_folder=Path(output_path) / f"{project_name}_{run_id}"
    llm_folder=output_folder/ "llm_response"

    output_folder.mkdir(parents=True, exist_ok=True)
    llm_folder.mkdir(parents=True, exist_ok=True)

    print('Folders created successfully......')

    client= OpenAI()

    res_df=read_resumes(resume_path)
    jd_df=read_jds(jd_path)

    if samples:
        res_df=res_df.iloc[:samples]

    job_des=jd_df.iloc[0].job_description_details

    screening_pipeline(client=client,
                        res_df=res_df,
                        system_prompt=system_prompt,
                        screening_class=ResumeScreener,
                        model=model,
                        job_des=job_des,
                        output_path=output_folder,
                        llm_result_path=llm_folder)

except Exception as e:
    print(e)

