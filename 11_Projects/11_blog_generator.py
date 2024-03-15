




import openai

openai_api_key = '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'

def create_blog_post(paragraph_topic):
    response = openai.completions.create(
        engine="gpt-3.5-turbo-instruct",
        prompt='Write a paragraph about ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3
    )

    retrieve_blog_post = response.choices[0].text
    return retrieve_blog_post

print(create_blog_post('Why Being Human is worse than being a robot?'))
