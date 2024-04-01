# Get-just-URLs-from-dirsearch-output
When using dirsearch, I found that it saved the subdirectories found along with the status code and the size of the file found in subdirectories. This made it difficult to easily pass this output into another tool, that accepted only URLs and lists of URLs as input, such as gau. 

Dirsearch also often returned duplicate subdirectories due to the wordlist I was using being case sensitive. 

So, I made this tool to quickly and easily parse files from dirsearch. This is able to remove duplicates and grab all of the unique URLs found by a dirsearch search. 


I have a couple of bugs/limitations currently that I am working on. 
  1. Cannot sort the list. 
  2. Can't then have a sorted list and write only the top x amount of URLs to a text file. Useful for time & space efficiency.

References:
https://github.com/maurosoria/dirsearch
https://github.com/lc/gau
