###--------------------------------------------------#####
# Projeto de Visão Computacional - RoboPose.
# Autor: Walisson Santos e Ruan Oliveira.
# Visão Computacional - UFBA - 2025.
# Estimação de pose de um robô Móvel utilizando técnicas de visão computacional.
###--------------------------------------------------#####

from pipeline import RoboPosePipeline

def main():
    pipeline = RoboPosePipeline("arquivos/video1.mp4")
    pipeline.run()

main()