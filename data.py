# Class for getting static graph data for testing the algorithms.
class DataLoader:

    @staticmethod
    def get_island_edges():
        return [
            {"from": "Hawaii", "to": "Tahiti", "travel_time": 15},
            {"from": "Tahiti", "to": "Hawaii", "travel_time": 15},
            {"from": "Tahiti", "to": "Rapa Nui", "travel_time": 20},
            {"from": "Rapa Nui", "to": "Tahiti", "travel_time": 20},
            {"from": "Hawaii", "to": "Aotearoa", "travel_time": 30},
            {"from": "Aotearoa", "to": "Hawaii", "travel_time": 30},
            {"from": "Tahiti", "to": "Aotearoa", "travel_time": 25},
            {"from": "Tahiti", "to": "Samoa", "travel_time": 10},
            {"from": "Samoa", "to": "Tahiti", "travel_time": 10},
            {"from": "Samoa", "to": "Rapa Nui", "travel_time": 15},
            {"from": "Rapa Nui", "to": "Samoa", "travel_time": 15},
            {"from": "Samoa", "to": "Aotearoa", "travel_time": 25},
            {"from": "Aotearoa", "to": "Samoa", "travel_time": 25},
        ]

    @staticmethod
    def get_island_populations():
        return {
            "Hawaii": 1500000,
            "Tahiti": 350000,
            "Rapa Nui": 8000,
            "Aotearoa": 5100000,
            "Samoa": 250000
        }
