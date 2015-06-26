#Design Specs for Full-Text-Indexing:

##Abstract:
Full-Text-Indexing is a process of scanning an ASCII file, tokenzation, filtering words, indexing to the database. What a seemingly relatively simple and straight-forward processmay soon hits its bottleneck if we do not put extra care on the design dealing with the efficiency, the challenges frolic in when the input size of an ASCII file is huge (>1 GB).  
This is to document down a potential solution to improve the efficiency of full-text-indexing program, particularly in the FILTER process, as per rapid prototyping of this program, as it consumes ~87% of the process runtime of the entire execution of the program.

##What's not covered in this spec:
- Database optimization based on read/write ratio.
- Integration with Panton Node structure.

##Strategy:
It's easier to lock down the problem when we break the entire process down into modular pieces. 

1. Time it to obtain average run-time of each module.
2. Design in a way that modules could run in parallels. (we need to resolve the communications between modules)
3. Optimization in terms of space vs. time complexity of each module.
4. Utilization of CPU processing.   

##Modules:
1. File-Reading
2. Tokenization
3. Filter (puntuations & reserved words & indexed words)
4. Indexing (store words & link it to file)
















##References:
[1] Russ Cox, "Regular Expression Matching Can Be Simple And Fast", https://swtch.com/~rsc/regexp/regexp1.html, 2007

