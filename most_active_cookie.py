#!/usr/bin/env python
import sys

def main(filename, date):
    cookie_counts = {}
    with open(filename) as csv_file:
        max_count = 0
        line_cnt = 0
        max_cookies_list = []
        for line in csv_file:
            if line_cnt == 0:   #Skips first line which contains column headers
                line_cnt += 1
                continue
            row = line.split(',')
            date_time = row[1]
            if date_time[:len(date)] == date:
                curr_cookie_count = cookie_counts.get(row[0], 0) + 1    #Increments the counter value of the cookie by 1
                if curr_cookie_count == max_count:
                    max_cookies_list.append(row[0])
                if curr_cookie_count > max_count:
                    max_count = curr_cookie_count
                    max_cookies_list = [row[0]]
                cookie_counts[row[0]] = curr_cookie_count
        return max_cookies_list

if __name__ == "__main__":
    filename = sys.argv[1]
    date = sys.argv[3]
    max_cookies_list = main(filename, date)
    for cookies in max_cookies_list:
        print(cookies, flush = True)

    


