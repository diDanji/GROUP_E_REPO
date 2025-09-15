class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")

    def show_stack(self):
        print("My tech stack:")
        for tool in self.tech_stack:
            print(f"- {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}/"

    def share_fun_fact(self):
        print(f"Fun fact: {self.fun_fact}")

my_profile = Profile(
    name="Kikomeko Ibrahim",
    favorite_language="Python",
    hobby="Reading",
    tech_stack=["Python", "Vs", "Git"],
    github_username="kikomeko617",
    fun_fact="I gave up my seat to a blind person on the bus. That's how I lost my job as a bus driver."
)

my_profile.introduce()
my_profile.show_stack()
my_profile.share_fun_fact()  
print("GitHub Profile:", my_profile.github_link())