from .mensagem_base import MensagemBase

class MensagemTexto(MensagemBase):
    def exibir(self):
        print(f"[Texto] '{self._texto}' (enviado em {self._data_envio})")