from abc import ABC, abstractmethod
from datetime import datetime

class MensagemBase(ABC):
    def __init__(self, texto: str):
        self._texto = texto
        self._data_envio = datetime.now()

    @abstractmethod
    def exibir(self):
        pass