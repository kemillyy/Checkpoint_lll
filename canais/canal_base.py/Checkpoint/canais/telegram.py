class CanalTelegram(CanalBase):
    def enviar_mensagem(self, mensagem):
        print(f"[Telegram] Enviando para usuário/número {self._identificador}:")
        mensagem.exibir()