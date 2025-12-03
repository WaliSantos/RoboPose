### **Projeto RoboPose**

#### **Objetivo**
Rastrear um robô móvel através de um marcador vermelho, estimar sua posição real no chão (em milímetros) e sua orientação, e gerar gráficos da trajetória.

---

### **parte 1: Configuração e Matemática (Setup)** **ok**
1.  **Definir a Matriz de Homografia ($H$):**
    * Copiar a matriz $H$ fornecida no PDF `modelo_camera.pdf`.
2.  **Calcular a Matriz Inversa ($H^{-1}$):**
    * A matriz original mapeia do Mundo $\to$ Imagem.
    * Nós queremos o inverso: **Imagem $(u,v) \to$ Mundo $(X,Y)$**. Portanto, usamos `np.linalg.inv(H)`.
3.  **Criar Função de Transformação (`pixel_para_mundo`):**
    * Entrada: Coordenadas do pixel $(u, v)$.
    * Passo A: Converter para coordenadas homogêneas: vetor coluna $[u, v, 1]^T$.
    * Passo B: Multiplicar pela matriz inversa: $P_{mundo} = H^{-1} \cdot P_{img}$.
    * **Passo C (Correção Importante):** Realizar a **Normalização Homogênea**. O resultado será $[X', Y', W']$. As coordenadas reais são $X = X'/W'$ e $Y = Y'/W'$.

---

### **parte 2: O Pipeline de Processamento**
fazer processamento do video
---
### **parte 3: gerar os resultados**
fazer os graficos e etc