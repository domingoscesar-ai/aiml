# Documentação da Correção - Kernel Crash em Jupyter Notebooks

## Problema Identificado

O notebook `ComputerVision/lesson001.ipynb` causava **crash do kernel** ao executar a célula que tentava exibir uma imagem usando OpenCV.

### Causa Raiz

A função `cv.imshow()` do OpenCV tenta abrir uma **janela gráfica do sistema**, o que é incompatível com o ambiente de execução dos Jupyter Notebooks. Isso resulta em crash do kernel e erro de execução.

```python
# ❌ CÓDIGO PROBLEMÁTICO
img = cv.imread('data/img/img01.png')
cv.imshow('window', img)  # Causa crash no Jupyter!
```

## Solução Implementada

### 1. Adicionar matplotlib aos imports
```python
import cv2 as cv
import matplotlib.pyplot as plt  # ✅ Novo
```

### 2. Substituir cv.imshow() por matplotlib
```python
# ✅ CÓDIGO CORRIGIDO
img = cv.imread('data/img/img01.png')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Converter BGR → RGB
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
```

## Detalhes Técnicos

| Aspecto | Problema | Solução |
|--------|----------|--------|
| **Função** | `cv.imshow()` abre janela do SO | `plt.imshow()` renderiza inline |
| **Compatibilidade** | ❌ Incompatível com Jupyter | ✅ Nativo em Notebooks |
| **Cores** | OpenCV usa BGR | Converter para RGB com `cv.cvtColor()` |
| **Renderização** | Tenta usar display do servidor | Renderiza como PNG embarcado |

## Arquivos Modificados

- **[ComputerVision/lesson001.ipynb](ComputerVision/lesson001.ipynb)**
  - Cell 1: Adicionado import de matplotlib
  - Cell 2: Substituído cv.imshow() por plt.imshow()

## Status de Validação

✅ Células testadas com sucesso:
- Célula 1 (imports) - Executou sem erros
- Célula 2 (exibição de imagem) - Exibiu imagem corretamente
- Célula 3 (YOLO) - Sem mudanças, continua funcionando
- Célula 4 (pip install) - Sem mudanças, continua funcionando

## Recomendação para Futuros Notebooks

Sempre que precisar exibir imagens em Jupyter, use:

```python
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('caminho/imagem.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.tight_layout()
plt.show()
```

## Referências

- [OpenCV Documentation](https://docs.opencv.org/master/d7/dbd/group__imgproc__shape.html)
- [Matplotlib in Jupyter](https://matplotlib.org/stable/users/interactive_guide.html)
- [Jupyter Best Practices](https://jupyter.readthedocs.io/en/latest/)
