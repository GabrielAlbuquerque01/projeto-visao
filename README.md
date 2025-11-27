# Reprodução dos Experimento do Artigo "Words or Vision: Do Vision-Language Models Have Blind Faith in Text?"

Este repositório contém o código, dados e notebooks utilizados para
investigar o fenômeno conhecido como "blind faith in text" em modelos de
visão-linguagem. O projeto replica e adapta experimentos
inspirados pelo artigo "Words or Vision: Do Vision--Language Models Have
Blind Faith in Text?" (Deng et al., CVPR 2025).

## Objetivo do Projeto

Avaliar se modelos de visão-linguagem confiam mais no texto presente nas
imagens do que nas informações visuais, reproduzindo e expandindo
experimentos do artigo selecionado.

## Estrutura do Repositório

    project/
    │
    ├── data/                       # Bases de dados geradas e arquivos auxiliares
    ├── images/                     # Imagens do VQAv2 utilizadas nos experimentos*
    ├── images_tuning/              # Imagens do VQAv2 utilizadas nos para tunar os modelos open-source*
    ├── jsons/                      # JSONs contendo informações das anotações e das perguntas do VQAv2*
    │
    ├── constants.py                # Constantes globais do projeto
    ├── utils.py                    # Funções auxiliares, como de limpeza das respostas dos modelos
    ├── requirements.txt            # Listagem das dependências necessárias para rodar o projeto
    │
    ├── evaluation.ipynb            # Avaliação dos resultados produzidos pelos modelos
    ├── lite_open_models.ipynb      # Experimentos com modelos open-source mais leves
    ├── property_models.ipynb       # Experimentos com modelos open-source mais leves
    ├── sanity_check.ipynb          # Verificação do impacto das descrições geradas para o problema
    ├── treatment_and_text_generation.ipynb  # Geração das descrições corretas, corrompidas e irrelevantes 

*Como as imagens e os .jsons utilizados nestes experimentos eram muito grandes, eles podem ser acessados através deste link:
https://drive.google.com/drive/folders/1Zwx3S_u_REeGAXZWVOQOzp2M2QPkDhdb?usp=drive_link

## Principais Dependências

-   Python 3.10+
-   PyTorch
-   Transformers (HuggingFace)
-   APIs de modelos utilizados
-   Pandas
-   Pillow

## Fluxo Principal

1. **Preparação dos Dados**
   - Extrair de `images.zip`, `images_tuning.zip` e `jsons.zip` presente no link fornecido os dados necessários e adicionar nas respectivas pastas (images, images_tuning, jsons).

2. **Geração das Descrições e Respostas**
   - Executar `treatment_and_text_generation.ipynb`.
   - Este notebook utiliza o GPT-4o para gerar as descrições corretas, corruptas e irrelevantes necessárias.

3. **Verificação das Saídas**
   - Executar `sanity_check.ipynb`.
   - Este notebook avalia a qualidade das descrições geradas pelo GPT-4o.

4. **Experimentos nos modelos**
   - `property_models.ipynb`: geração dos outputs para as diferentes combinações de amostras nos modelos proprietários (neste caso, o GPT-4o mini).
   - `lite_open_models.ipynb`: geração dos outputs para as diferentes combinações de amostras nos modelos abertos (neste caso, o Qwen2-VL-2B).

4. **Avaliação dos Modelos**
   - Executar `evaluation.ipynb`.
   - Este notebook calcula métricas como acurácia por condição, Text Preference Ratio (TPR) e gera gráficos equivalentes aos do artigo.


## Contato

Qualquer dúvidas ou sugestões podem ser encaminhadas para o seguinte endereço eletrônico: gca@ecomp.poli.br
