from landsites import Land
from data_structures.bst import BinarySearchTree, BSTPostOrderIterator
from data_structures.heap import MaxHeap
from algorithms import mergesort
from typing import List, Tuple

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = BinarySearchTree()
        sites = mergesort(sites, key = lambda x: x.get_gold()/x.get_guardians())
        self.adventurers = adventurers

        for land in sites:
            self.sites[(land.get_gold() / land.get_guardians())] = land
        self.size = len(sites)
        self.remaining = self.adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        result = []

        for i in BSTPostOrderIterator(self.sites.root):
            island = island.item
            if self.remaining >= island.get_guardians():
                self.remaining -= island.get_guardians()
                result.append((island, island.get_guardians()))
            else:
                result.append((island, self.remaining))
                self.remaining = self.adventurers
                break

        self.remaining = self.adventurers
        return result

    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()
