class DataLoader:
    """Fake data for testing the graph flow algorithms.
    """

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
            {"from": "Aotearoa", "to": "Tahiti", "travel_time": 25},
            {"from": "Tahiti", "to": "Samoa", "travel_time": 10},
            {"from": "Samoa", "to": "Tahiti", "travel_time": 10},
            {"from": "Samoa", "to": "Rapa Nui", "travel_time": 15},
            {"from": "Rapa Nui", "to": "Samoa", "travel_time": 15},
            {"from": "Samoa", "to": "Aotearoa", "travel_time": 25},
            {"from": "Aotearoa", "to": "Samoa", "travel_time": 25},
            {"from": "Hawaii", "to": "Samoa", "travel_time": 20},
            {"from": "Samoa", "to": "Hawaii", "travel_time": 20},
            {"from": "Niihau", "to": "Hawaii", "travel_time": 5},
            {"from": "Hawaii", "to": "Niihau", "travel_time": 5},
            {"from": "South America", "to": "Tahiti", "travel_time": 40},
            {"from": "Tahiti", "to": "South America", "travel_time": 40},
            {"from": "South-East Asia", "to": "Rapa Nui", "travel_time": 45},
            {"from": "Rapa Nui", "to": "South-East Asia", "travel_time": 45},
        ]

    @staticmethod
    def get_island_populations():
        return {
            "Hawaii": 1500000,
            "Tahiti": 350000,
            "Rapa Nui": 8000,
            "Aotearoa": 5100000,
            "Samoa": 250000,
            "Niihau": 250,
            "South America": 4000000,
            "South-East Asia": 3000000
        }

    @staticmethod
    def get_resources():
        return {
            "kahelelani_shell_leis": {
                "produced_at": "Niihau",
                "quantity": 1000,
                "canoe_capacity": 100
            },
            "uala": {
                "produced_at": "South America",
                "quantity": 2000,
                "canoe_capacity": 50
            },
            "kalo": {
                "produced_at": "South-East Asia",
                "quantity": 1500,
                "canoe_capacity": 75
            }
        }
