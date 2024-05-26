from landsites import Land
from data_structures.heap import MaxHeap
from data_structures.referential_array import ArrayR
from typing import List, Tuple, Union



class Mode2Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    """

    def __init__(self, n_teams: int) -> None:
        self.num_teams = n_teams
        self.sites = []

    def add_sites(self, sites: List[Land]) -> None:
        if not self.sites:
            self.sites = sites
        else:
            self.sites.extend(sites)

    def compute_score(self, site: Land, adventurers: int) -> Tuple[float, float, int]:
        if site.guardians == 0:
            reward = site.gold
        else:
            reward = min((adventurers * site.gold) / site.guardians, site.gold)
        remaining_adventurers = adventurers - site.guardians if adventurers >= site.guardians else 0
        score = 2.5 * remaining_adventurers + reward
        return score, reward, remaining_adventurers

    def construct_score_data_structure(self, adventurers: int) -> MaxHeap:
        score_heap = MaxHeap(len(self.sites))
        for site in self.sites:
            score, reward, remaining_adventurers = self.compute_score(site, adventurers)
            score_heap.add((score, site, reward, remaining_adventurers))
        return score_heap

    def simulate_day(self, adventurer_size: int) -> List[Tuple[Union[Land, None], int]]:
        return_list = []
        score_heap = self.construct_score_data_structure(adventurer_size)

        for _ in range(self.num_teams):
            if len(score_heap) == 0:
                return_list.append((None, 0))
                continue

            score, site, reward, remaining_adventurers = score_heap.get_max()
            if site.get_gold() > 0:
                sent = min(site.get_guardians(), adventurer_size)
                site.set_gold(site.get_gold() - reward)
                site.set_guardians(max(site.get_guardians() - adventurer_size, 0))
                return_list.append((site, sent))
            else:
                return_list.append((None, 0))

            # Update the heap with the modified site
            self.update_heap(score_heap, adventurer_size)

        return return_list

    def update_heap(self, score_heap: MaxHeap, adventurer_size: int) -> None:
        updated_heap = MaxHeap(len(self.sites))
        for i in range(1, len(score_heap.the_array)):
            if score_heap.the_array[i] is not None:
                _, site, _, _ = score_heap.the_array[i]
                if site.get_gold() > 0:
                    score, reward, remaining_adventurers = self.compute_score(site, adventurer_size)
                    updated_heap.add((score, site, reward, remaining_adventurers))
        score_heap.the_array = updated_heap.the_array
        score_heap.length = updated_heap.length



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