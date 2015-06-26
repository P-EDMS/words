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
2. Design in a way that modules could run in parallels.   

##Modules:
1. File-Reading
2. 


