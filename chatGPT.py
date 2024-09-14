from openai import OpenAI

class HashtagGenerator():
    def __init__(self, target, desc, api_key):
        self.target = target
        self.title = self.target['Title']
        self.genre = self.target['Genre']
        self.description = desc
        self.client = OpenAI(api_key = api_key) 

    def guess_genre(self):
        few_shot_prompt = (
            "Example 1: \n"
            "Title: The Adventures of Captain Marvel\n"
            "Genre: Superhero\n"
            "Hashtags: #Superhero #Action #Marvel #Hero #EpicJourney\n\n"
            "Example 2:\n"
            "Title: Celestial Chronicles\n"
            "Genre: Fantasy\n"
            "Hashtags: #Fantasy #Magic #Adventure #EpicQuest #Mythical\n\n"
            "Now, generate 5 catchy and genre-appropriate hashtags for this comic:\n"
        )
        
        system_prompt = "You are a social media content generator specializing in creating hashtags for web comics."
        user_prompt = f"Title: {self.title}\nDescription: {self.description}\nGenre: {self.genre}"

        response = self.client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user","content": few_shot_prompt + user_prompt}
            ],
        )

        hashtags = response.choices[0].message.content
  
        return hashtags


