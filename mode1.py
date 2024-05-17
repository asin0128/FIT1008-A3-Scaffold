from landsites import Land
from data_structures.heap import MaxHeap
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
        self.sites = sites
        self.adventurers = adventurers

    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        max_heap = MaxHeap(len(self.sites))  # Initialize the max heap with the number of land sites
        
        # Insert lands into the max heap based on the gold-to-guardians ratio
        for land in self.sites:
            if land.guardians > 0:
                ratio = land.gold / land.guardians
            else:
                ratio = float('inf')  # If no guardians, prioritize this land
            max_heap.insert((ratio, land))

        selected_sites = []
        remaining_adventurers = self.adventurers

        # Extract from max heap and allocate adventurers
        while remaining_adventurers > 0 and not max_heap.is_empty():
            ratio, land = max_heap.extract_max()
            if land.guardians == 0:
                selected_sites.append((land, 0))
                continue

            needed_adventurers = min(land.guardians, remaining_adventurers)
            selected_sites.append((land, needed_adventurers))
            remaining_adventurers -= needed_adventurers

        return selected_sites

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
