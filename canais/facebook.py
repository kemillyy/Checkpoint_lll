from .canal_base import CanalBase

class CanalFacebook(CanalBase):
    def enviar_mensagem(self, mensagem):
        print(f"[Facebook] Enviando para usuário {self._identificador}:")
        mensagem.exibir()