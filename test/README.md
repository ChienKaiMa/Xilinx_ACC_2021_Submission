# PCAP generator
## Required packages
- `scapy`
- `pandas`

## Usage
```shell
>> python pcap_gen.py -h
# prints the help message
>> python pcap_gen.py -o data_gen.pcap r --csv ./data/data.csv
# generate data_gen.pcap from a given csv file
>> python pcap_gen.py g --req_arb --output_csv data_gen.csv
# generates a random data and output the csv file of generated data
```
## Note
1. The generated data has information of 18 exchange pair which its exchange rate range from 0.0001 to 10000 randomly.
2. The `pcap_gen.py` takes `./data/cme_input_arb.pcap` as a template of pcap generation, hence this file is required during the generation process.
