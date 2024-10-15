from project.player import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, p: Player) -> str:
        if p.guild == "Unaffiliated":
            self.players.append(p)
            p.guild = self.name
            return f"Welcome player {p.name} to the guild {self.name}"
        elif p.guild == self.name:
            return f"Player {p.name} is already in the guild."
        else:
            return f"Player {p.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        for p in self.players:
            if p.name == player_name:
                self.players.remove(p)
                p.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}"
        for p in self.players:
            result += f"\n{p.player_info()}"
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
