import os
import httpx
try:
    from openai import OpenAI
except:
    pass

PROXY = os.environ['http_proxy']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

def get_gpt_completion(prompt,
                       system=None,
                       temperature=0, 
                       max_tokens=1024,
                       model="gpt-4o", 
                       api_key=None, 
                       base_url=None, 
                       count_tokens=False,
                       **kwargs):

    messages = []
    if system is not None:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})    
        
    if api_key is None:
        client = OpenAI(
            api_key=OPENAI_API_KEY,
            http_client=httpx.Client(
                proxies=PROXY
            )
        )
    else:
        client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
    
    if kwargs.get('stream') is True:
        completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        **kwargs
        )
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
    else:
        attempts = 0
        max_attempts = 10
        while attempts < max_attempts: 
            try:
                try:
                    completion = client.chat.completions.create(
                    model=model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    **kwargs
                    )
                    total_tokens = completion.usage.total_tokens
                    prompt_tokens = completion.usage.prompt_tokens
                    completion_tokens = completion.usage.completion_tokens
                    if count_tokens:
                        return completion.choices[0].message.content, [prompt_tokens, completion_tokens, total_tokens]
                    else:
                        return completion.choices[0].message.content
                except:
                    completion = client.completions.create(
                    model=model,
                    prompt=prompt,
                    temperature=temperature,
                    **kwargs
                    )
                    total_tokens = completion.usage.total_tokens
                    prompt_tokens = completion.usage.prompt_tokens
                    completion_tokens = completion.usage.completion_tokens
                
                    if count_tokens:
                        return completion.choices[0].text, [prompt_tokens, completion_tokens, total_tokens]
                    else:
                        return completion.choices[0].text
            except:
                attempts += 1
                if attempts < max_attempts:
                    print("Trying again...")
                else:
                    print("Max attempts reached. Exiting.")