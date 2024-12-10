# Demyst_coding_round

# To run the Docker file, we need to clone the respository to our local machine and exucute the folloing few lines of code in command promt or terminal one by one.

1) git clone https://github.com/atharvapandit81/Demyst_coding_round.git

2) cd Demyst_coding_round

3) docker build -t demyst-coding-round .

4) docker run --rm -v $(pwd)/spec.json:/app/spec.json -v $(pwd)/input.txt:/app/input.txt -v $(pwd)/output.csv:/app/output.csv demyst-coding-round
