import yaml
import os

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

resume_path= config['paths']['resume_path']
jd_path= config['paths']['jd_path']
output_path= config['paths']['output_path']

project_name= config['project']['project_name']
run_id= config['project']['run_id']
samples=config['project']['samples']

model= config['llm']['model']
temperature= config['llm']['temperature']

system_prompt= config['prompts']['system_prompt']

if __name__=='__main__':
    print(f'resume path- {resume_path}')
    print(f'JD path- {jd_path}')
    print(f'Model- {model}')
    print(f'System Prompt- {system_prompt}')