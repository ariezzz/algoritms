#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

from collections import Counter
from operator import itemgetter


class MyNode:

    def __init__(self, left=None, right=None):

        self.left = left

        self.right = right

    def walk(self, code, value):

        self.left.walk(code, value + ['0'])

        self.right.walk(code, value + ['1'])


class MyLeaf:

    def __init__(self, char):

        self.char = char

    def walk(self, code, val):

        code[self.char] = val


class Huffman:

    def __init__(self, data):

        self.data = data

        self.code = dict()

        self.node = self._node

    @property
    def _tree(self):

        counter = list()

        for key, value in Counter(self.data).items():

            counter.append([MyLeaf(key), value])

            # counter.append([key, value])

        return counter

    @property
    def _node(self):

        leaves = self._tree

        while len(leaves) >= 2:

            left = leaves.pop()

            right = leaves.pop()

            leaf_count = left[1] + right[1]

            leaves.append(
                [MyNode(left=left[0], right=right[0]), leaf_count])

            leaves.sort(key=itemgetter(1), reverse=True)

        return leaves.pop()[0]

    def main(self):

        self.node.walk(self.code, [])

    def __repr__(self):

        string = ''

        for i in self.data:

            string += ''.join(self.code[i]) + ' '

        return f'Строка {self.data}\n Сжата в {string}\n\
таблица {self.code}'

# a = Huffman('абра кадабра швабра')


a = Huffman('beep boop beer!')

a.main()

print(a)
