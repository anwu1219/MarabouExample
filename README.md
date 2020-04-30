usage: benchmark_maker.py [-h] [-e EPSILON] -o ORIGINAL_LABEL -t TARGET_LABEL
                          [-f FILENAME] [-d DUMP_DIRECTORY]
                          [-n NUMBER_OF_PROPERTIES] [-s SEED]

optional arguments:
  -h, --help            show this help message and exit
  -e EPSILON, --epsilon EPSILON
                        Epislon value
  -o ORIGINAL_LABEL, --original-label ORIGINAL_LABEL
                        Correct label
  -t TARGET_LABEL, --target-label TARGET_LABEL
                        Targeted label
  -f FILENAME, --filename FILENAME
                        The prefix of the generated property files
  -d DUMP_DIRECTORY, --dump-directory DUMP_DIRECTORY
                        The directory to dump the property file
  -n NUMBER_OF_PROPERTIES, --number-of-properties NUMBER_OF_PROPERTIES
                        Number of properties to dump
  -s SEED, --seed SEED  random seed for getting training point

Example:

mkdir property

python3 benchmark_maker.py -o 1 -t 2 -e 0.02 -d ./property -n 10

This will dump 10 target attack queries about 10 different training points
in the ./property directory.
The original label of each training point is 0 and the target label is 2.
The input region is an epsilon ball around the training point.
