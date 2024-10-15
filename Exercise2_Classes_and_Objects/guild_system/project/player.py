class Player:
    def __init__(self, name: str, hp: int, mp: int) -> None:
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: list[tuple] = []
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        for skill in self.skills:
            if skill_name == skill[0]:
                return "Skill already added"
        else:
            self.skills.append((skill_name, mana_cost))
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"
        if self.skills:
            for skill in self.skills:
                result += f"\n==={skill[0]} - {skill[1]}\n"
        return result
