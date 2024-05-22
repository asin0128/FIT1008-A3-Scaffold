from landsites import Land
from data_structures.heap import MaxHeap



class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.invaders = n_teams
        self.islands = [] #stores all islands
        self.tree = None
        self.crew = [] #invader size after attack

    def add_sites(self, sites: list[Land]) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands.extend(sites)

    def simulate_day(self, adventurer_size: int) -> list[tuple[Land | None, int]]:
        """
        Student-TODO: Best/Worst Case
        """

        result_tree = [] # -> list[tuple[Land | None, int]]: thing above
        self.tree = MaxHeap.heapify(self.islands)
        for i in range(self.invaders):
            self.crew.append(adventurer_size)
        print(self.crew)

if __name__ == '__main__':
    dt = Mode2Navigator(4)
    A = Land("A", 400, 100)
    B = Land("B", 300, 150)
    C = Land("C", 100, 5)
    D = Land("D", 350, 90)
    E = Land("E", 300, 100)

    some_list = [A,B,C,D,E]
    dt.add_sites(some_list)
    dt.simulate_day(1000)