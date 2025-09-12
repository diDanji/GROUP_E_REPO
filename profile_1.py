class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"Hi, I’m {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}.")

    def show_stack(self):
        print("Tech Stack:")
        for tool in self.tech_stack:
            print(f"- {tool}")

    def github_link(self):
        return f"https://github.com/{self.github_username}"

# Example usage:
if __name__ == "__main__":
    my_profile = Profile(
        name="Mwebaza Tony",
        favorite_language="Python",
        hobby="construction",
        tech_stack=["Python", "Javascript", "Git", "VS Code"],
        github_username="anthonymweb",
        fun_fact="I once coded for 25 hours straight!"
    )

    my_profile.introduce()
    my_profile.show_stack()
    print("GitHub Profile:", my_profile.github_link())
    print("Fun Fact:", my_profile.fun_fact)