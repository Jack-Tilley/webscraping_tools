# tablescraper.py
# Jack Tilley
# February 2019
# This program scrapes the table inputted and outputs the table as a 2D list

from bs4 import BeautifulSoup

class TableScrape:
    def __init__(self, soupscope, ignore_rows=[], ignore_columns=[], separated_header=True,
                 header_row_container="thead", header_row_tag="tr", table_row_container="tbody",
                 table_row_tag="tr", header_info_tag="th", table_info_tag="td"):

        self.soupscope = soupscope  # takes soup argument
        self.ignore_rows = ignore_rows  # takes soup argument which will be ignored
        self.ignore_columns = ignore_columns  # takes column index arguments which will be ignored
        self.separated_header = separated_header  # True if table header and table body are separate
        self.header_row_container = header_row_container  # tag value of location where header exists in soup
        self.header_row_tag = header_row_tag   # tag value of row where header info exists
        self.table_row_container = table_row_container  # tag value of location where table exists in soup
        self.table_row_tag = table_row_tag  # tag value of where table row info exists
        self.header_info_tag = header_info_tag # tag value of info stored inside header_row_tag
        self.table_info_tag = table_info_tag  # tag value of info stored inside table_row_tag

    # gets row info based on row tag
    def get_row_info(self, row, tag_to_find):
        row_list = []
        row_data = row.find_all(tag_to_find)
        for column in range(len(row_data)):
            if column not in self.ignore_columns:
                row_list.append(row_data[column].text)
        return row_list

    # gets table values depending on parameters given
    def scrape(self):
        table = []

        rows = self.soupscope.find(self.table_row_container).find_all(self.table_row_tag)
        if self.separated_header:
            header_row = self.soupscope.find(self.header_row_container).find(self.header_row_tag)
        else:
            header_row = self.soupscope.find(self.table_row_container).find(self.table_row_tag)
            rows = rows[1:]

        full_header = self.get_row_info(header_row, self.header_info_tag)
        table.append(full_header)

        for row in rows:
            if row not in self.ignore_rows:
                row_data = self.get_row_info(row, self.table_info_tag)
                table.append(row_data)
        return table
