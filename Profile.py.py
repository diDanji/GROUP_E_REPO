class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hello, My name is {self.name}.And i love {self.favorite_language} and my hobby is {self.hobby}.")

    def show_stack(self):
        print(f"My tech stack includes: {', '.join(self.tech_stack)}.")

    def github_link(self):
        return f"https://github.com/Asia-Marvin-4"

my_profile = Profile(
    name="Asia ",
    favorite_language="HTML",
    hobby="Travelling,Vactions,Abseiling",
    tech_stack=["Python", "HTLML", "Javascript, php"],
    github_username="your_github_username",
    fun_fact="I can't swim"
)

my_profile.introduce()
my_profile.show_stack()
print(f"Check out my GitHub profile: {my_profile.github_link()}")