# Class for getting static graph data for testing the algorithms.
class DataLoader:

    @staticmethod
    def get_island_graph():
        return [
            {"from": "Hawaii", "to": "Tahiti", "travel_time": 15},
            {"from": "Tahiti", "to": "Hawaii", "travel_time": 15},
            {"from": "Tahiti", "to": "Rapanui", "travel_time": 20},
            {"from": "Rapanui", "to": "Tahiti", "travel_time": 20},
            {"from": "Hawaii", "to": "Aotearoa", "travel_time": 30},
            {"from": "Aotearoa", "to": "Hawaii", "travel_time": 30},
            {"from": "Tahiti", "to": "Aotearoa", "travel_time": 25},
            {"from": "Tahiti", "to": "Samoa", "travel_time": 10},
            {"from": "Samoa", "to": "Tahiti", "travel_time": 10},
            {"from": "Samoa", "to": "Rapanui", "travel_time": 15},
            {"from": "Rapanui", "to": "Samoa", "travel_time": 15},
            {"from": "Samoa", "to": "Aotearoa", "travel_time": 25},
            {"from": "Aotearoa", "to": "Samoa", "travel_time": 25},
        ]
