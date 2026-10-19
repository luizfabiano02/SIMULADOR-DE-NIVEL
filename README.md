# Controle de Níveis de Água

## Descrição
Este programa simula o monitoramento dos níveis de água de um reservatório. Ele utiliza a linguagem Python e a biblioteca Colorama para exibir mensagens coloridas no terminal, de acordo com o nível de água. Atividade do curso de DSI.

## Níveis do reservatório

- **Nível 1:** Muito baixo (crítico) — Vermelho.
- **Nível 2:** Baixo — Amarelo.
- **Nível 3:** Médio — Verde.
- **Nível 4:** Alto — Ciano.
- **Nível 5:** Muito alto (alerta) — Azul.

## Tecnologias utilizadas

- Python
- Biblioteca Colorama

## Instalação

Instale a biblioteca Colorama utilizando o terminal:

```bash
python -m pip install colorama
```

## Como executar

1. Abra o terminal na pasta do arquivo.
2. Execute o comando:


## Funcionamento

O programa armazena as mensagens em uma lista, utiliza uma função para definir a cor de cada nível e percorre os cinco níveis com uma estrutura de repetição `for`. As mensagens são exibidas com suas respectivas cores, e o estilo do terminal é restaurado após cada exibição.

## Observação

Este programa é uma simulação educativa. Os níveis são definidos no próprio código e não representam medições reais de um reservatório.

