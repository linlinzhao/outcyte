This is the standalone version of [OutCyte](outcyte.com) and [paper](https://www.nature.com/articles/s41598-019-55351-z).  

This instruction assumes you are using linux and know basic Python and bash commands. For windows users, it might need adaption.  

Suppose you cloned the repo or downloaded and unzipped the software to a fold named "outcyte" 

How to: 

0. Open a terminal window

1. Change work directory to "outcyte".

2. Set up a virtual environment based on requirements.txt, Then activate the python virtual environment by running the following command:
```source ./bin/activate```

3. Now you can annotate your fasta file by typing:

```python run_outcyte.py /path/to/your/fasta/file /outcyte-sp/or/outcyte-ups/or/outcyte```

The last field of the command specifies the method you would want to use, it could be either one of "outcyte-sp", "outcyte-ups" or "outcyte". It is basically the same as the web version. 

4. The result will be stored in the subfolder "results". 
