# DiagnosePy — Sistema Especialista para Diagnóstico de Erros de Programação

Sistema especialista desenvolvido em Python que recebe o tipo de erro apresentado
por um programa e, a partir de uma base de conhecimento com regras explícitas,
retorna a possível causa do erro e uma orientação para correção.

## Disciplina

**Programação de Sistemas Especialistas**
Professor: Vinicius
Universidade Veiga de Almeida (UVA)

## Grupo

- Davi Santos Silva (1250113510)
- Gabriel Barbosa Souza De Oliveira (1250123662)
- Lohan Matheus Gonçalves Teodoro (1250124891)
- Lucas Brandão Rosas (1250124788)
- Gabriel Thiago Corrêa da Silva (1250108004)

## Sobre o projeto

O sistema simula o fluxo clássico de um sistema especialista:
Delete Entrada do usuário → Motor de inferência → Base de regras → Diagnóstico → Orientação


O usuário informa o tipo de erro apresentado (ex.: `NameError`, `IndexError`,
`ZeroDivisionError`) e o motor de inferência consulta a base de conhecimento
para retornar a causa provável e a orientação de correção.

## Base de conhecimento (regras)

| Erro | Possível causa | Orientação |
|---|---|---|
| SyntaxError | Estrutura do código incorreta | Verificar sintaxe, pontuação e ':' |
| NameError | Variável ou função não definida | Conferir nome e se foi criada antes do uso |
| TypeError | Tipo de dado incompatível | Verificar mistura de tipos incompatíveis |
| ValueError | Valor inválido para a operação | Conferir o valor passado à função |
| IndexError | Índice fora dos limites da lista | Verificar tamanho da lista e posição acessada |
| KeyError | Chave inexistente no dicionário | Confirmar se a chave existe antes de acessá-la |
| ZeroDivisionError | Divisão por zero | Verificar se o divisor pode ser zero |
| IndentationError | Problema na indentação | Revisar espaços/tabs do bloco |
| ImportError | Módulo não encontrado ou import incorreto | Conferir nome do módulo e instalação |
| Erro de Lógica | Condição, laço ou variável incorreta | Revisar condições, laços e valores |

## Como executar

```bash
python main.py
```

O programa exibirá um menu para escolha do tipo de erro e retornará o
diagnóstico com a causa provável e a orientação de correção.

## Protótipo de telas

Protótipo navegável com as 6 telas do fluxo (Início → Seleção do erro →
Motor de inferência → Diagnóstico final → Decisão → Encerramento):

- Figma: [https://check-young-08606117.figma.site/]

