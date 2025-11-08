from .mensagem_base import MensagemBase

class MensagemArquivo(MensagemBase):
    def __init__(self, texto: str, arquivo: str, formato: str):
        super().__init__(texto)
        self._arquivo = arquivo
        self._formato = formato

    def exibir(self):
        print(f"[Arquivo] '{self._texto}' ({self._arquivo}, formato {self._formato})")
