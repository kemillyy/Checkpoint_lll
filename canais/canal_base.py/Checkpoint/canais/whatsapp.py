from .canal_base import CanalBase

class CanalWhatsApp(CanalBase):
    def enviar_mensagem(self, mensagem):
        print(f"[WhatsApp] Enviando para número {self._identificador}:")
        mensagem.exibir()
