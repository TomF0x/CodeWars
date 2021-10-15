# https://www.codewars.com/kata/515bb423de843ea99400000a

import math


# TODO: complete this class

class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)

    def page_item_count(self, page_index):
        if len(self.collection) < (page_index * self.items_per_page):
            return -1
        if len(self.collection) > page_index * self.items_per_page >= (
                len(self.collection) - len(self.collection) % self.items_per_page):
            return len(self.collection) % self.items_per_page
        return page_index * self.items_per_page

    def page_index(self, item_index):
        if len(self.collection) - 1 < item_index or item_index < 0:
            return -1
        return (item_index // self.items_per_page)
