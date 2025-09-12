class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}. Fun fact: {self.fun_fact}")

    def show_stack(self):
        print("My tech stack:")
        for tool in self.tech_stack:
            print(f"- {tool}")

    def github_link(self):
        return f"https://github.com/diDanji/"

# Create your profile
my_profile = Profile(
    name="dilli tony",
    favorite_language="Python",
    hobby="Listening to hiphop & RnB",
    tech_stack=["Python", "Django", "Git"],
    github_username="tonny dilli",
    fun_fact="I can solve a Rubik's cube in under a minute!"
)

# Call the methods
my_profile.introduce()
my_profile.show_stack()
print("GitHub Profile:", my_profile.github_link())