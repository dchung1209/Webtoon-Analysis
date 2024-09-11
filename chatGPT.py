import openai

class HashtagGenerator():
    def __init__(self, target, desc):
        self.target = target
        self.title = self.target['Title']
        self.genre = self.target['Genre']
        self.url = self.target['URL']
        self.desc = desc

    def guess_genre(self):
        few_shot_prompt = f"Here are some comics and their hashtags."
        
        role_prompt = "You are a social media influencer specializing in web comics."

        instruction
        prompt = f"Generate 5 catchy and genre-appropriate hashtags for a comic titled"
        completion = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a social media content generator. Generate hashtags based on the given context",
            },
            {
                "role": "user",
                "content": prompt,
            },
            ],
        )   
  
        return completion.choices[0].message.content


