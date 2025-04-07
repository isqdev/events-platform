from abc import ABC, abstractmethod
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos

class InscritosRepositoryInterface(ABC):
    def insert(self, subscriber_infos: dict) -> None: pass
            
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: pass
