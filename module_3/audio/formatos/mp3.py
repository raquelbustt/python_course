def converter(arquivo):
    """
    meuvideo.mp4 ==> meuvideo.mp3
    """

    novo_arquivo = arquivo.split(".")[0] + '.mp3'

    print(f"Arquivo {arquivo} convertido para {novo_arquivo}")