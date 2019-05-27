# Exercise 3
from pathlib import Path

basedir = Path("C:/Users/Kochti/Desktop/Studium/Python/exercise-3-TLKoch/")
data_dir = basedir / "data"
output_dir = basedir / "solution"

# import functions from utils here
import utils as ut

# 1. Construct the path to the text file in the data directory using the `pathlib` module [2P]

cars_path = data_dir / "cars.txt"
print(cars_path)

# 2. Read the text file [2P]

with open(cars_path, "r") as file:
    content = file.read().splitlines()

# 3. Count the occurences of each item in the text file [2P]
 
# possible function for this tasks, see an all_in_one solution in task 5    
# ut.countocc(content)    

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]

# possible function for this tasks, see an all_in_one solution in task 5  
# ut.directorycheck(output_dir)


# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

# Actually it is easier to combine the two previous tasks with this last one to one great function, which only needs the txt-Path and an output-directory as input. 
ut.all_in_one(content, output_dir)


        
        