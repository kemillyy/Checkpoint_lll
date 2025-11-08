from .mensagem_base import MensagemBase

class MensagemFoto(MensagemBase):
    def __init__(self, texto: str, arquivo: str, formato: str):
        super().__init__(texto)
        self._arquivo = arquivo
        self._formato = formato

    def exibir(self):
        print(f"[Foto] '{self._texto}' ({self._arquivo}, formato {self._formato})")
