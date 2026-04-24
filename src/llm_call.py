from .exceptions import LLMCallFailed_Error

def make_api_call(client, system_prompt, screening_class, model, text, job_des):
    try:
        response=client.chat.completions.parse(
            model=model,

            messages=[{'role':'system', 
                       'content':system_prompt},
                      {'role':'user',
                       'content':f'''Screen the following resume as per the given job description.
                       Follow the given schema to format the output.
                       RESUME TEXT: {text}
                    JOB DESCRIPTION: {job_des}'''}],

            response_format=screening_class
        )

        cleaned_result=response.choices[0].message.parsed.model_dump()
        return cleaned_result
    
    except Exception as e:
        raise LLMCallFailed_Error('LLM call has failed')