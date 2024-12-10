# Demyst_coding_round

# 1st Problem

# To run the Docker file, we need to clone the respository to our local machine and exucute the folloing few lines of code in command promt or terminal one by one.

1) git clone https://github.com/atharvapandit81/Demyst_coding_round.git

2) cd Demyst_coding_round

3) docker build -t demyst-coding-round .

4) docker run --rm -v $(pwd)/spec.json:/app/spec.json -v $(pwd)/input.txt:/app/input.txt -v $(pwd)/output.csv:/app/output.csv demyst-coding-round

# 2nd Problem

# For the second problem just run the first data_processing.py file and it will generate the dummy file and the same code will also encode the file. 
# For handling the large csv files I have written the code in data_processing_using_pyspark.py, running that will generate the necessary files.
