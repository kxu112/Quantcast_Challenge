#!/usr/bin/env python3
import argparse

def parse_cli():    # Parses command line for filename and target date
    parser = argparse.ArgumentParser(description='Reads csv file to identify most common cookie')
    parser.add_argument('file_name', type = str, help = 'Name of csv file')
    parser.add_argument('-d', '--date', required = True, help = 'Target date')
    args = parser.parse_args()
    return args

def match_date(date_time_str, target_date): # Checks if date of cookie matches target date
    return date_time_str[:len(target_date)] == target_date

def update_count(cookie_name, cookie_counts):   # Updates the count in the cookie dictionary
    curr_cookie_count = cookie_counts.get(cookie_name, 0) + 1
    cookie_counts[cookie_name] = curr_cookie_count
    return curr_cookie_count

def parse_csv(filename, target_date):   # Parses the csv file
    cookie_dict = {}
    with open(filename) as csv_file:
        matched_date = False
        max_count = 0   # Stores largest number of times a cookie has appeared
        line_cnt = 0
        max_cookies_list = []   # Stores all cookies that have appeared the most
        for line in csv_file:
            if line_cnt == 0:   #Skips first line which contains column headers
                line_cnt += 1
                continue
            row = line.split(',')
            cookie_name = row[0]
            date_time = row[1]
            if match_date(date_time, target_date):
                matched_date == True
                cookie_count = update_count(cookie_name, cookie_dict)
                if cookie_count == max_count:
                    max_cookies_list.append(row[0]) # Add cookie to list if appeared highest number of times
                if cookie_count > max_count:    # Update max_count if cookie has appeared more than all others
                    max_count = cookie_count
                    max_cookies_list = [row[0]]
            else:
                if matched_date:    # If we have already come across a match, then there cannot be any more dates that match afterwards
                    return max_cookies_list
    return max_cookies_list # Returns all cookies that have appeared the highest amount of times


def main():
    args = parse_cli()
    filename = args.file_name
    date = args.date
    max_cookies_list = parse_csv(filename, date)
    for cookies in max_cookies_list:
        print(cookies, flush = True)

if __name__ == '__main__':
    main()