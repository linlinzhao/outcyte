### What is this?
This is the standalone version of [OutCyte](outcyte.com) and here is the [paper](https://www.nature.com/articles/s41598-019-55351-z).  

### Dependencies

- Python 3.7
- Core package dependency: PyTorch 1.0.1 (can be replaced with Numpy implementations), XGBoost 0.9
- The instructions assumes you are using linux and know basic Python and bash commands. For windows users, it might need adaptation.  
- We consider that you cloned the repo or downloaded it and unzipped the software to a folder named "outcyte" 

### How

1. Change work directory to "outcyte".

2. Set up a virtual environment with conda :
  `conda create -n outcyte --file requirements.txt`, then activate the python virtual environment by running the following command:
```conda activate outcyte```

3. Now you can annotate your fasta file by typing:

```python run_outcyte.py /path/to/your/fasta/file <outcyte-model>  <output_dir> ```

where "outcyte-model" specifies the method you would want to use, so it could be either one of "outcyte-sp", "outcyte-ups" or "outcyte". It is basically the same as the web version. 

4. The results will be stored in the subfolder you define as  < output_dir >. 
