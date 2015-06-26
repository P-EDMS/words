#Design Specs for Full-Text-Indexing:

##Abstract:
Full-Text-Indexing is a process of scanning an ASCII file, tokenzation, filtering words, indexing to the database. What a seemingly relatively simple and straight-forward processmay soon hits its bottleneck if we do not put extra care on the design dealing with the efficiency, the challenges frolic in when the input size of an ASCII file is huge (>1 GB).  
This is to document down the proposed solution to improve the efficiency of full-text-indexing program, particularly in the FILTER process.

##Strategy:


