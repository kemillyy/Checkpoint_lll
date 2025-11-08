from .canal_base import CanalBase

class CanalInstagram(CanalBase):
    def enviar_mensagem(self, mensagem):
        print(f"[Instagram] Enviando para usuário {self._identificador}:")
        mensagem.exibir()