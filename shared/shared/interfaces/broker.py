from abc import ABC, abstractmethod


class BrokerAdapter(ABC):
    
    @abstractmethod
    def place_order(self, order: dict) -> dict:
        pass
    
    @abstractmethod
    def get_status(self, order_id: str) -> dict:
        pass