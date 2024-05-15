from landsites import Land


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
        # Sort lands by gold-to-guardians ratio in descending order
        sorted_lands = sorted(self.sites, key=lambda land: (land.gold / land.guardians), reverse=True)

        selected_sites = []
        remaining_adventurers = self.adventurers

        # Allocate adventurers to each land
        for land in sorted_lands:
            if remaining_adventurers <= 0:
                break
            
            if land.guardians == 0:
                # If there are no guardians, we can collect all gold without sending adventurers
                selected_sites.append((land, 0))
                continue

            # Calculate the maximum adventurers needed to match guardians
            needed_adventurers = min(land.guardians, remaining_adventurers)

            # Calculate the reward for sending the adventurers
            reward = min((needed_adventurers * land.gold) / land.guardians, land.gold)

            # Add to selected sites
            selected_sites.append((land, needed_adventurers))

            # Reduce the remaining adventurers
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
