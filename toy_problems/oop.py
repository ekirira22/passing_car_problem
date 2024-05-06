class Scoreboard:
    def __init__(self, participants = []) -> None:
        self.participants = participants  
        self.food_points = {"chickenwings": 5, "hamburgers": 3, "hotdogs": 2}
    
    def find_winners(self):
        scores = []
        """
          Find the total cost by looping through and timesing by the food_points
        """
        for participant in self.participants:
            name = participant.get("name")
            chicken = participant.get("chickenwings", 0) * self.food_points["chickenwings"]
            hamburger = participant.get("hamburgers", 0) * self.food_points["hamburgers"]
            hotdog = participant.get("hotdogs", 0) * self.food_points["hotdogs"]

            sum = chicken + hamburger + hotdog
            scores.append((name, sum))
            
        # sort scores
        scores.sort(key = lambda x: (-x[1], x[0]))
        return scores
