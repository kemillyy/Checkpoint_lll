from abc import ABC, abstractmethod

class CanalBase(ABC):
    def __init__(self, identificador: str):
        self._identificador = identificador  # Encapsulamento

    @abstractmethod
    def enviar_mensagem(self, mensagem):
        pass