import pandas as pd
import re
log_file = 'logfile.log'
csv_file = 'logs.csv'

def parse_log_line(line):

    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>.*?)\] "(?P<request_method>\w+) (?P<request>.*?) HTTP/(?P<http_version>\d\.\d)" (?P<status>\d+) (?P<size>\d+) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None

with open(log_file, 'r') as f:
    logs = [parse_log_line(line) for line in f if parse_log_line(line) is not None]

headers = ['IP Address', 'Timestamp', 'Request Method', 'Request', 'HTTP Version', 'Status Code', 'Size', 'Referrer', 'User Agent']


df = pd.DataFrame(logs, columns=headers)
df.to_csv(csv_file, index=False)
print(df)
print(df.iloc[:, 1])

unique_error_codes_count = df['Status Code'].value_counts()

print(unique_error_codes_count) #to print unique status code with number of logs with that status code


