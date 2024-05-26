from landsites import Land
from data_structures.bst import BinarySearchTree, BSTPostOrderIterator
from data_structures.heap import MaxHeap
from algorithms import mergesort
from typing import List, Tuple

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per
    https://edstem.org/au/courses/14293/lessons/46720/slides/318306
    We have been given a set of islands 'sites' which hold a particular amount of gold guarded by some number of guardians. In our inventory is 
    a finite amount of adventurers using which we explore the islands and obtain the respective gold; while spending the amount of adventurers 
    as there are guardians of the island. Since the number of gold and guardians vastly differ island to island, we must find the gold-to-guardian ratio
    of each island and organise them on this ratio; highest to lowest. The most optimal way to sort the set of islands is to insert them in a MaxHeap Data Structure;
    and call get_Max to obtain the best ratio islands; and insert them in an array. The worst case Time complexity of get_max is O(logN) where N are the number of nodes
    present in the binary Heap. This is within our complexity constraint.
    """

    def __init__(self, sites: list[Land], adventurers: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.sites = sites
        self.adventurers = adventurers
        self.remaining_adventurers = adventurers
        
        # Initialize the MaxHeap
        self.max_heap = MaxHeap(len(self.sites))
        
        # Add all sites to the max heap based on their ratio
        for site in self.sites:
            self.max_heap.add((site.get_ratio(), site)) 


        



    def select_sites(self) -> list[tuple[Land, int]]:
        """
        Student-TODO: 
        Best Case Time Complexity: O(LogN) combined, This occurs when the formation of the heap structure including the 
    islands with their respective ratio takes O(1). When we call the getMax functions, this returns the root node of the MaxHeap, which is O(1)
    then the Max Heap commences sink function where the last node which is now the root node, is sequentially compared with the larger child and switch positions.
    This entire process takes O(logN), where N is the number of nodes in the MaxHeap. Altogether this takes O(logN) time complexity.
    Worst Case is O(logN), here, there might be multiple same ratios for the same island.
        """
        result = []
        remaining_adventurers = self.remaining_adventurers

        # Extract sites from the max heap and allocate adventurers
        while remaining_adventurers > 0 and len(self.max_heap) > 0:
            ratio, site = self.max_heap.get_max()  # Extract the site object
            
            if site.get_guardians() == 0:
                assigned_adventurers = remaining_adventurers  # All remaining adventurers can be sent
            else:
                assigned_adventurers = min(remaining_adventurers, site.get_guardians())
            
            result.append((site, assigned_adventurers))
            remaining_adventurers -= assigned_adventurers
        
        return result


    def select_sites_from_adventure_numbers(self, adventure_numbers: list[int]) -> list[float]:
        """
        Best Case: O(N+logN)
        Worst Case: O(N+KlogN) where L is the number of adventure sizes in the adventure_numbers list, K is the number of teams, N is the number of islands
        """
        results = []
        original_adventurers = self.adventurers  # Save the original number of adventurers

        for num_adventurers in adventure_numbers:
            self.remaining_adventurers = num_adventurers
            selected_sites = self.select_sites()
            total_gold = sum(min(site.get_gold() * adventurers / site.get_guardians(), site.get_gold())
                             for site, adventurers in selected_sites)
            results.append(total_gold)

        self.adventurers = original_adventurers  # Restore the original number of adventurers
        return results

    def update_site(self, land: Land, new_reward: float, new_guardians: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        land.set_gold(new_reward)
        land.set_guardians(new_guardians)
        # Rebuild the heap with updated site ratios
        self.max_heap = MaxHeap(len(self.sites))
        for site in self.sites:
            self.max_heap.add((site.get_ratio(), site))
