# Table of Contents
1. [Problem](README.md#problem)
2. [Run Instructions](README.md#run-instructions)
3. [Approach](README.md#approach)


# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. The immigration data trends have gained much attention recently because of the stringent provisions to the H-1B labour application process. The statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf). 

If the newspaper gets data for the year 2019 and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code. This mechanism can help the editor get **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.



## Run instructions
**Run Script**

Save the input file as `./input/h1b_input.csv` then run `./run.sh`.

**Run Unit Tests**

```
cd src
./run_test.sh 
```



## Approach

**Repo directory structure
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   ├──h1b_counting.py
      │   ├──helpers.py
      │   ├──resources
      │   |  ├──criteria.json
      │   |  └──counting_targets.json
      |   ├──unit_tests.py
      |   ├──columns.py
      |   └──run_test.sh
      |
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── your-own-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```


1.**Data Loading:** Use the Python sys Library to read data. Open CSV file and read each line into tuple list

2.**Processing:** Clean and prepare data: Remove the items which application STATUS is not 'CERTIFIED' and

3.**Sort:** Use the Python Standard Library **collections** to pick the top ten states and top ten occupations.

4.**Output:** Use Standard **I/O** Library to write list of tuples to text files.

