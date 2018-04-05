# Trabalho Final da Disciplina de Grafos
### O trabalho consiste de buscar a solução do sudoku proposto utilizando algum algortimo para coloração de grafos
##### Utilizamos o algoritmo _DSatur_ com _Backtracking_
------------
**Professor(a):**
> Gabriela de Melo Pontes

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
	1. A escrita do arquivo deve seguir o seguinte padrão:
		- cada '-' corresponde a uma celula vazia do sudoku
		- um numero corresponde a uma celula preenchida com aquele numero
		- o arquivo deve conter 9 linha
		- cada linha deve conter 9 caracteres ( '-' ou numero )
