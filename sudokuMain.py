from Graph import *

if __name__ == "__main__":
    input_name = "input.txt"
    output_name = "output.txt"
    input_file = open(input_name,"r")
    cells = ""
    for line in input_file:
        cells = cells + ((line.replace(" ","").replace("\n","").replace("-","N")))
    cells = list(cells)
    graph = Graph(cells)
    graph.solve(output_name)
    graph.writeFile(output_name)
