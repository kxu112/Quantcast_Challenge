#!/usr/bin/env python3
import argparse

def parse_cli():
    parser = argparse.ArgumentParser(description='Reads csv file to identify most common cookie')
    parser.add_argument('file_name', type = str, help = 'Name of csv file')
    parser.add_argument('-d', '--date', required = True, help = 'Target date')
    args = parser.parse_args()
    return args

def match_date(date_time_str, target_date):
    return date_time_str[:len(target_date)] == target_date

def update_count(cookie_name, cookie_counts):
    curr_cookie_count = cookie_counts.get(cookie_name, 0) + 1
    cookie_counts[cookie_name] = curr_cookie_count
    return curr_cookie_count

def parse_csv(filename, target_date):
    cookie_dict = {}
    with open(filename) as csv_file:
        max_count = 0
        line_cnt = 0
        max_cookies_list = []
        for line in csv_file:
            if line_cnt == 0:   #Skips first line which contains column headers
                line_cnt += 1
                continue
            row = line.split(',')
            cookie_name = row[0]
            date_time = row[1]
            if match_date(date_time, target_date):
                cookie_count = update_count(cookie_name, cookie_dict)
                if cookie_count == max_count:
                    max_cookies_list.append(row[0])
                if cookie_count > max_count:
                    max_count = cookie_count
                    max_cookies_list = [row[0]]
    return max_cookies_list


def main():
    args = parse_cli()
    filename = args.file_name
    date = args.date
    max_cookies_list = parse_csv(filename, date)
    for cookies in max_cookies_list:
        print(cookies, flush = True)

if __name__ == '__main__':
    main()