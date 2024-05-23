from dataclasses import dataclass
from random_gen import RandomGen

# Land sites can have names other than the list follows.
# This is just used for random generation.
LAND_NAMES = [
    "Dawn Island",
    "Shimotsuki Village",
    "Gecko Islands",
    "Baratie",
    "Conomi Islands",
    "Drum Island",
    "Water 7"
    "Ohara",
    "Thriller Bark",
    "Fish-Man Island",
    "Zou",
    "Wano Country",
    "Arabasta Kingdom",
    # 13 🌞 🏃‍♀️
    "Loguetown",
    "Cactus Island",
    "Little Garden",
    "Jaya",
    "Skypeia",
    "Long Ring Long Land",
    "Enies Lobby",
    "Sabaody Archipelago",
    "Impel Down",
    "Marineford",
    "Punk Hazard",
    "Dressrosa",
    "Whole Cake Island",
    "Ys Island",
]


@dataclass
class Land:

    name: str
    gold: float
    guardians: int
    remaining: int = 0
    total: int = 0

    @classmethod
    def random(cls):
        return Land(
            RandomGen.random_choice(LAND_NAMES),
            RandomGen.randint(0, 500),
            RandomGen.randint(0, 300),
        )

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> float:
        return self.gold

    def get_guardians(self) -> int:
        return self.guardians

    def set_gold(self, new_gold: float) -> None:
        self.gold = new_gold

    def set_guardians(self, new_guardians: int) -> None:
        self.guardians = new_guardians

    def set_remaining(self, num_adventurers: int) -> None:
        self.remaining = max(num_adventurers - self.get_guardians(), 0)
        self.total = num_adventurers        

    def calc_score(self) -> float:
        if self.get_guardians() != 0:
            if (self.total - self.remaining) < self.get_guardians():
                return 2.5 * self.remaining + min(((self.total - self.get_guardians()) * self.get_gold()) / self.get_guardians(), self.get_gold())
            else:
                return 2.5 * self.remaining + min((self.get_guardians()  * self.get_gold()) / self.get_guardians(), self.get_gold())
        else:
            return 2.5 * self.remaining + self.get_gold()

    def __gt__(self, other) -> bool:
        return self.calc_score() > other.calc_score()
    
    def __lt__(self, other) -> bool:
        return self.calc_score() < other.calc_score()
    
    def __eq__(self, other) -> bool:
        return self.calc_score() == other.calc_score()
    
    def __ne__(self, other) -> bool:
        return self.calc_score() != other.calc_score()
    
    def __ge__(self, other) -> bool:
        return self.calc_score() >= other.calc_score()
    
    def __le__(self, other) -> bool:
        return self.calc_score() <= other.calc_score()