mm2in
=====

Utility for breaking down a metric distance into its imperial equivalent.

```
./mm2in.py --help
Usage: mm2in.py <number of millimeters> *or* <options>

Options:
  -h, --help      show this help message and exit
  -m MM, --mm=MM  millimeters
  -c CM, --cm=CM  centimeters
  -M M, --m=M     meters

```

Examples
--------

1. Only one option -- assumed to be millimeters

 ```
 ./mm2in.py 2400
 7' 10" 7/16
 ```

2. Using multiple metric units (32 meters, 10 centimeters and 9 millimeters)

 ```
 ./mm2in.py -M 32 -c 10 -m 9
 105' 4" 1/8
 ```
 
3. Breakdown goes from miles all the way to 1/16 of an inch

 ```
 ./mm2in.py -M 32000    # -- 32K meters
 19 miles 4666' 10" 1/2 
 
 ./mm2in.py -m 2        # -- 2 millimeters
 1/16
 
 ./mm2in.py -m 20
 3/4
 
 ./mm2in.py -m 120
 4" 11/16
 ```
