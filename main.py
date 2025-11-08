from canais.whatsapp import CanalWhatsApp
from canais.telegram import CanalTelegram
from canais.facebook import CanalFacebook
from canais.instagram import CanalInstagram

from mensagens.mensagem_texto import MensagemTexto
from mensagens.mensagem_video import MensagemVideo
from mensagens.mensagem_foto import MensagemFoto
from mensagens.mensagem_arquivo import MensagemArquivo

def main():
    # Canais
    whatsapp = CanalWhatsApp("+5511999999999")
    telegram = CanalTelegram("@usuario_tg")
    facebook = CanalFacebook("usuario_fb")
    instagram = CanalInstagram("usuario_ig")

    # Mensagens
    texto = MensagemTexto("Olá, esta é uma mensagem de texto!")
    video = MensagemVideo("Confira o vídeo!", "video.mp4", "mp4", 120)
    foto = MensagemFoto("Veja esta foto!", "foto.jpg", "jpg")
    arquivo = MensagemArquivo("Baixe o arquivo!", "documento.pdf", "pdf")

    # Envio
    whatsapp.enviar_mensagem(texto)
    telegram.enviar_mensagem(video)
    facebook.enviar_mensagem(foto)
    instagram.enviar_mensagem(arquivo)

if __name__ == "__main__":
    main()
