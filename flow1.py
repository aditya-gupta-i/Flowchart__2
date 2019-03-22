from graphviz import Digraph
from graphviz import render
#make sure you have graphviz installed

g = Digraph('G', filename='DNAseq_Pipeline.dot',format='png')

g.attr('node', shape='hexagon')
g.attr('edge', style='dashed')

g.attr(rankdir='TB', size='8,5')
g.attr('edge',minlen='2')
g.attr('node',fixedsize='true', width='1.3',height='1.3')


#The steps
g.node('A',label='picard_\nsam_to\n_fastq',style='filled', color = 'lightgrey')
g.node('B',label='trimmo-\nmatic',style='filled', color = 'lightgrey')
g.node('C',label='merge_\ntrimmomatic_\nstats',style='filled', color = 'lightgrey')
g.node('D',label='bwa_mem_\npicard_\nsort_sam',style='filled', color = 'lightgrey')
g.node('E',label='picard_\nmerge_sam\n_files',style='filled', color = 'grey55')


#Inputs
g.attr('node',fixedsize='true', width='0.5',height='0.5')
g.node('F',label='~~\n~~',xlabel='.bam',shape='note')
g.node('G',label='~~\n~~',xlabel='.fastq',shape='note')
g.node('H',label='~~\n~~',xlabel='.bam',shape='note')


#inputs
g.edge('F', 'A') #input to step 1
g.edge('G', 'B') #input to step 2
g.edge('H', 'E') #input to step 5


# Edges for steps 1-5
g.edge('A', 'B')
g.edge('B', 'C')
g.edge('C', 'D')
g.edge('D', 'E')

g.attr('node',fixedsize='false') #undoing the fixed size command
g.body.append('label = <<u>DNAseq Pipeline</u>>;') #label of entire digraph
g.body.append('{rank = same; A; B; C; D; E;}; {rank = same; F;G;H;};') #To style it


#code below this is just for rendering the explaination of the various symbols used in the above code :
# (it is a bit unreadable because of python indentation)
# This code can be added anywhere, just change the A and C they are connected to. (Find that code at the last append)


#cluster_1 (The symbols explained)
g.body.append('subgraph cluster_1 {')
g.body.append('label = <<u>Symbols</u>>;')
g.body.append('edge[style=invis];')
g.body.append('a0[shape = plaintext, label = "step per\n readset"];   a1[shape = plaintext, label = "step on multiple \nreadsets/samples"];  a2[shape = plaintext, label = "input file"];')
g.body.append('b0 -> b1 -> b2;')
g.body.append('b0[shape = hexagon,style=filled,color = lightgrey,label=""];  b1[shape = hexagon,style=filled, color = gray55,label=""];   b2[shape = note,label="~~\n~~"];')
g.body.append('b0->a0[style = invis];	 b1->a1[style = invis];   b2->a2[style = invis];')
g.body.append('{rank = same;a0;b0};        {rank = same;a1;b1};        {rank = same;a2;b2};     }')

#cluster_2 (The arrows explained)
g.body.append('subgraph cluster_2{')
g.body.append('label = <<u>Arrows</u>>;')
g.body.append('edge[style = invis];')
g.body.append('a3[shape = plaintext, label = "input/output"]; 		a4[shape = plaintext, label = "alternate\n input path"]; 		a5[shape = plaintext, label = "step \ndependency"];')
g.body.append('b3 ->b4 ->b5;')
g.body.append('b3[style = invis];        b4[style = invis];        b5[style = invis];')
g.body.append('b3->a3[style = solid]; 		b4->a4[style = dotted];		b5->a5[style = dashed];')
g.body.append('{rank = same;a3;b3};        {rank = same;a4;b4};        {rank = same;a5;b5};}')

#The connection to upper body
#Replace A to change position of cluster_1 that explains the symbols
#Replace C to change position of cluster_2 that explains the arrows
g.body.append('edge[style=invis];   A->b0;  C->b3;  ')


#uncomment this to see the dot source code
#print(g.source)

#To publish changes into the png
g.view()

#uncomment this if you want to open it automatically
#g.render(view=True)
