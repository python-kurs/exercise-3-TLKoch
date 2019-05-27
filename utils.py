# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script


# possible function for task 3, see an all_in_one solution below in the all_in_one Function 
def countocc(x):
    """
    Calculate the occurence of each item in a text file.
    
    Parameters
    ----------
    x : text file
        
    Returns
    -------
    item and the corresponding number of occurence of this item in the text file
    
    """
    
    items = list(set(x))
    for value in items: 
        print(value, x.count(value))
        
        
           
# possible function for task 4, see an all_in_one solution below in the all_in_one Function 
def directorycheck(output):
    """
    Checks, if a directory exists. If it does not exist, it creates this directory.
    
    Parameters
    ----------
    output : directory
        
    Returns
    -------
    Prints a statement whether the given directory already existed or whether it had to be created
    
    """
    temp = output.exists()
    if temp == True:
        print("Your results will be saved into the directory \"{}\" ".format(output))
    else:    
        output.mkdir()
        print("Unfortunately your directory \"{}\" did not exist, so it was created. Your results will be saved in there".format(output))
    
            
        
# Function for creating a csv file in a directory for the item and its counts        
def all_in_one(x, output):
    """
    Calculate the occurence of each item in a text file. Checks, if a output directory exists. If it does not exist, it creates this directory and finally saves 
    the results there in a csv file
    
    Parameters
    ----------
    x : text file
    output: an output directory, where to save the results
        
    Returns
    -------
    A csv file with each item from a textfile and the corresponding number of occurence of this item in the text file
    
    """
    import pandas as pd
    # Create dataframe for counting the occurences for each item in a text file 
    items = list(set(x))
    countings = []
    for value in items: 
        countings.append(x.count(value))
    countingsdf = pd.DataFrame({'model': items, 'countings': countings})
    
    # Checking output directory
    temp = output.exists()
    if temp == True:
        print("Your results are saved into the directory \"{}\" ".format(output))
    else:    
        output.mkdir()
        print("Unfortunately your directory \"{}\" did not exist, so it was created. Your results are saved in there".format(output))
        
        
    # savind the results into a csv file
    output_name = output / "results_counting_occurences.csv"      
    countingsdf.to_csv (output_name, header = True)

      
                
