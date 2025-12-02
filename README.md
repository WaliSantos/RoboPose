## Transformação de coordenadas

1. Primeiro configurar a matriz que vai converter pixaels (u,v) em milimetros (X,Y). Foi dado a matriz de homografia H, e como temos que fazer a transição imagem -> mundo, é necessario achar a inversa dessa matriz

2. Usar um loop while para ler frame a frame. Em cada frame fazer:
    2.1) Normalização de cor: converter a imagem para float e calcular a cromatiticidade normalizada (r e g)
    2.2) Segmentação: criar uma mascara binaria onde r é alto e g é baixo
    2.3) Usar morphologyEx (Abertura/Fechamento) para remover ruídos brancos pequenos e fechar buracos no marcador.
    2.4) calculo da pose:
        2.4.1) achar o contorno do marcador
        2.4.2) calcular os momentos
        2.4.3) obter o centroide e o angulo 
    2.5) transformação: multiplicar o centroide (u,v,1) pela matriz H^-1 para obert (X,Y)