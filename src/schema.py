from pydantic import BaseModel, Field
from typing import Literal, List

class ResumeScreener(BaseModel):
    candidate_name:str=Field(description="Mention the name of the candidate given in the resume text")
    candidate_summary:str=Field(description='Mention the profile summary or description of candidate given in the resume text.')
    total_experience:float=Field(description="""Mention the total years of experience of the candidate. If the candidate is a fresher or does not have any experience then mention 0.
                                 Always mention the experience in years. If the experience is given in months then calculate it in years.""")
    relevant_experience:float=Field(description="""Mention the relevant years of experience of the candidate as per the job description. If the candidate is a fresher or does not have any experience then mention 0.
                                 Always mention the experience in years. If the experience is given in months then calculate it in years.""")
    matching_skills:List[str]=Field(description="Mention the list of matching skills of the candidate as per the job description.")
    missing_skills:List[str]=Field(description="Mention the list of the missing skills in the resume as per the job description.")
    highest_education:str=Field(description="Mention the highest education of the candidate")
    relevant_education:Literal["Yes","No"]=Field(description="Does the candidate have the relevenat education as per the job description?")
    recommendation:Literal["Highly Recommended", "Weakly Recommended", "No Recommendation"]=Field(description="Give the recommendation after analysing overall details given in the resume as per the hob description")
    reasoning:str=Field(description='Give a detailed reasoning and explanation of your answers by adding a snippet from the resume text')