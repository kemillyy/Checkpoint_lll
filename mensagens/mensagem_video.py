from .mensagem_base import MensagemBase

class MensagemVideo(MensagemBase):
    def __init__(self, texto: str, arquivo: str, formato: str, duracao: int):
        super().__init__(texto)
        self._arquivo = arquivo
        self._formato = formato
        self._duracao = duracao

    def exibir(self):
        print(f"[Vídeo] '{self._texto}' ({self._arquivo}, formato {self._formato}, duração {self._duracao}s)")
