from abc import ABC, abstractmethod
from nlp_parser.schema import TradeOrder


class BaseBroker(ABC):
    
    @abstractmethod
    async def execute_order(self, order: TradeOrder) -> dict:
        """Send order to broker and return response"""
        pass

    @abstractmethod
    def get_account_info(self) -> dict:
        pass