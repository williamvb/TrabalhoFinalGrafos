# Trabalho Final da Disciplina de Grafos
### O trabalho consiste de buscar a solução do sudoku proposto utilizando algum algortimo para coloração de grafos
##### Utilizamos o algoritmo _DSatur_ com _Backtracking_
------------
**Professor(a):**
> Gabriela Mendes

**Equipe:**
> William Vieira Bastos
> José Macedo de Araujo Filho

-------------
#### Algoritmos usados
- **Backtracking:** é um tipo de algoritmo que representa um refinamento da busca, onde múltiplas soluções podem ser eliminadas sem a necessidade de serem explicitamente examinadas.
- **DSatur:** é um método heurístico que apresenta um bom desempenho. Ele usa o conceito de grau de saturação de um vértice que é o número de diferentes cores para o qual ele é adjacente.

#### Concepção
- O projeto foi feito em `python3` com a IDE `ATOM` e versionamento atraves do `Github`.
- Para gerar um codigo mais genérico, optamos por obter as entradas ( *Sudoku* ) através de arquivos '.txt', assim como gerar a saida também em '.txt'.
- Foram criadas as classes:
	- **Vertice**: contendo as definições para os vertices como, conteudo, vizinhos, assim como as ações que deverão ser executadas sobre os vertices, como, calculo de saturação, mudança da saturação de seus vizinhos e possiveis cores para o vertice.
	- **Graph**: contendo as definições para o grafo, definições de linha, coluna e bloco ( *caracteristicas do Sudoku* ), o algoritmo ***DSatur*** , assim como a criação do arquivo *"output.txt"* que contem  o resultado.
- O arquivo *"sudokuMain.py"* executa a solução do puzzle, define o arquivo de entrada, *"input.txt"*, e saida, *"output.txt"*, além de fazer a leitura/conversão da entrada para as classes criadas.

#### Execução
- Para a execução do programa faz-se necessario seguir alguns passos para o arquivo de entrada:
	1. O arquivo com a entrada ( *sudoku* ) deve estar no mesmo diretorio dos demais arquivos do projeto
	1. O nome do arquivo deve ser: ***input.txt***
	1. A escrita do arquivo deve seguir o padrão abaixo onde cada '-' corresponde a uma celula do sudoku, seja ela preenchida ou vazia:

Sudoku Vazio | Sudoku Incompleto | Sudoku Concluido
--------------- | ---------------------  | -------------
- - - - - - - - - | - 2 - 5 - 1 - 9 -          | 4 2 6 5 7 1 3 9 8
- - - - - - - - - | 8 - - 2 - 3 - - 6          |8 5 7 2 9 3 1 4 6
- - - - - - - - - | - 3 - - 6 - - 7 -           |1 3 9 4 6 8 2 7 5
- - - - - - - - - | - - 1 - - - 6 - -            |9 7 1 3 8 5 6 2 4
- - - - - - - - - | 5 4 - - - - - 1 9           |5 4 3 7 2 6 8 1 9
- - - - - - - - - | - - 2 - - - 7 - -            |6 8 2 1 4 9 7 5 3
- - - - - - - - - | - 9 - - 3 - - 8 -           |7 9 4 6 3 2 5 8 1
- - - - - - - - - | 2 - - 8 - 4 - - 7          |2 6 5 8 1 4 9 3 7
- - - - - - - - - | - 1 - 9 - 7 - 6 -          |3 1 8 9 5 7 4 6 2 
