# tablescraper.py
# Jack Tilley
# February 2019
# This program scrapes the table inputted and outputs the table as a 2D list

from bs4 import BeautifulSoup


class TableScrape:
    def __init__(self, soupscope, ignore_rows=[], ignore_columns=[], separated_header=True,
                 header_row_container="thead", header_row_tag="tr", table_row_container="tbody",
                 table_row_tag="tr", header_info_tag="th", table_info_tag="td", keep_all_text=False,):

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
        self.keep_all_text = keep_all_text # keeps first text if False, keeps all text separated by "|" if True

    # gets row info based on row tag
    def get_row_info(self, row, tag_to_find):
        row_list = []
        row_data = row.find_all(tag_to_find)
        for column in range(len(row_data)):
            if column not in self.ignore_columns:
                column_text_list = row_data[column].find_all(text=True)
                if self.keep_all_text:
                    column_text = "|".join(column_text_list)
                else:
                    column_text = column_text_list[0]
                row_list.append(column_text)
        return row_list

    # gets table header info
    def get_header_info(self):
        if self.separated_header:
            header_row = self.soupscope.find(self.header_row_container)
        else:
            header_row = self.soupscope.find(self.table_row_container)

        header_row = header_row.find(self.header_row_tag)
        full_header_data = self.get_row_info(header_row, self.header_info_tag)
        return full_header_data

    # gets table body info
    def get_body_info(self, rows):
        full_body_data = []
        if not self.separated_header:
            rows = rows[1:]

        for row in rows:
            if row not in self.ignore_rows:
                row_data = self.get_row_info(row, self.table_info_tag)
                full_body_data.append(row_data)
        return full_body_data

    # gets table values depending on parameters given
    def scrape(self):
        table = []
        rows = self.soupscope.find(self.table_row_container).find_all(self.table_row_tag)
        full_header = self.get_header_info()
        table.append(full_header)
        full_body = self.get_body_info(rows)
        for info_row in full_body:
            table.append(info_row)
        return table
