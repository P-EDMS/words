#Design Specs for Full-Text-Indexing:

##Abstract:
Full-Text-Indexing is a process of scanning an ASCII file, tokenzation, filtering words, indexing to the database. What a seemingly relatively simple and straight-forward processmay soon hits its bottleneck if we do not put extra care on the design dealing with the efficiency, the challenges frolic in when the input size of an ASCII file is huge (>1 GB).  
This is to document down a potential solution to improve the efficiency of full-text-indexing program, particularly in the FILTER process, as per rapid prototyping of this program, as it consumes ~87% of the process runtime of the entire execution of the program.

##What's not covered in this spec:
- Database optimization based on read/write ratio.
- Integration with Panton Node structure.
- Non-ASCII file.

##Strategy:
It's easier to lock down the problem when we decompose a complex process into simple modular tasks. 

1. Time it & benchmark to obtain average run-time of each module.
2. Design in a way that modules could run in parallels. (we need to resolve the communications between modules)
3. Optimization in terms of space vs. time complexity of each module.
4. Utilization of CPU processing.   

##Modules:
1. File-Reading
2. Sanitization(punctuation marks)
3. Filter (reserved words & indexed words)
4. Indexing (store words & link it to file)

##File-Reading  

This is the starting process of full-text-indexing. File reading is a process of opening a file and read its content out to application memory for manipulation. There are many file-reading techniques,  each of it will be discussed in details at later section.

###Analysis
An assessment of the performance of several methods:

**Method 1: Naive reading**

    File.Read()



**Method 2:** 

-File.ReadLine()
 

##Tokenization:

Tokenization is to recognize & extract words out of a stream of characters (string). The definition of `word` is a single distinct meaningful element which collectively forms a sentence, that is often seperated by space or punctuation marks.

In computer representation:
- space = {\n, \t, \r} 
- punctuation marks = {!, @, #, $, %, ... , : }   



###Psedocode:

An assessment of the performance of several methods:







###Analysis:

This section is to note down the possible complexity of this module in terms of time and space. Notably for tokenization module, the focus is rather on time complexity.

- O(n). Linear-time algorithm. 

To get words out of a sentence, we have to scan each and every character in that stream of characters, and it could be done in single pass.





















   






##Future improvements:
1. Key-phrase indexing, indexing with context, for an example:

Obesity -> overweight  	


2. Improve performance. How do we boost up the performance by using:
- multi-threading. Not with Python, especially it has GIL.
- multi-process (CPU cores).
- caching



##References:
[1] Russ Cox, "Regular Expression Matching Can Be Simple And Fast", https://swtch.com/~rsc/regexp/regexp1.html, 2007.

[2] Ugo Scaiella, "Improving regex preformance on JVM", http://blog.spaziodati.eu/en/2014/11/07/improving-regex-performance-on-java-virtual-machine-jvm/, 2014.

[3] Stackoverflow, "Speed up a single task using multi-processing or threading", http://goo.gl/DXcybN, 2013.

[4] Michael Cvet, "Parallel MapReduce in Python in Ten Minutes", https://mikecvet.wordpress.com/2010/07/02/parallel-mapreduce-in-python/, 2010

[5] Alyona (Olena) Medelyan, "Key Phrase Indexing With Controlled Vocabularies", youtube.

[6] Alyona Medelyan, "Semantically Enhanced Automatic Keyphrase Indexing", 2006

[7] https://www.simple-talk.com/sql/learn-sql-server/understanding-full-text-indexing-in-sql-server/

[8] http://stackoverflow.com/questions/3055477/how-slow-is-pythons-string-concatenation-vs-str-join

[9]  "Efficient String Concatenation in Python", https://waymoot.org/home/python_string/	
