TabelaCaracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
TabelaAcentosA = ['Á','À','Ã','Â']
TabelaAcentosE = ['É','È','Ê']
TabelaAcentosI = ['Í','Ì','Î']
TabelaAcentosO = ['Ó','Ò','Õ','Ô']
TabelaAcentosU = ['Ú','Ù','Û']

def simplificar(texto):
  caracteresSimplificados = []
  texto = texto.upper()
  for caractere in texto:
    for acento in TabelaAcentosA:
      if caractere == acento:
        caractere = 'A'
    for acento in TabelaAcentosE:
      if caractere == acento:
        caractere = 'E'
    for acento in TabelaAcentosI:
      if caractere == acento:
        caractere = 'I'
    for acento in TabelaAcentosO:
      if caractere == acento:
        caractere = 'O'
    for acento in TabelaAcentosU:
      if caractere == acento:
        caractere = 'U'
    if caractere == 'Ç':
      caractere = 'C'

    caracteresSimplificados.append(caractere)
  return caracteresSimplificados

def transcriptar(texto):
  caracteres = simplificar(texto)
  posicaoCaractere = 0
  textoTranscriptado = ''
  for caractere in caracteres:
    if caractere == ' ' or caractere == '.' or caractere == ',' or caractere == '?' or caractere == '!' or caractere == '"' or caractere == '-' or caractere == "'":
        textoTranscriptado = textoTranscriptado + str(caractere)
    else:
      posicaoCaractere = TabelaCaracteres.index(caractere)
      if posicaoCaractere < 13:
        posicaoCaractere = posicaoCaractere + 13
        textoTranscriptado = textoTranscriptado + str(TabelaCaracteres[posicaoCaractere])
      else:
        posicaoCaractere = posicaoCaractere - 13
        textoTranscriptado = textoTranscriptado + str(TabelaCaracteres[posicaoCaractere])
  return textoTranscriptado

def main():
  entrada = True
  print("Digite o texto a ser transcriptado abaixo, caso queira terminar escreva '-1'")
  while entrada != "-1":
    entrada = input("\n\ntexto: ")
    if entrada != "-1":
      saida = transcriptar(entrada)
      print("Transcrição: ",saida)
  input("Aperte qualquer coisa para terminar")

if __name__ == "__main__":
  main()
