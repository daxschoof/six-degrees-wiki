'''
    Implement BFS using wikipedia urls and the links in the wiki page.
    Store url, title, links in the page, and the parent link in the list.
'''

from typing import final
from page import Page
import sys


def main():
    # Testing Purposes
    try:
        startingNode = Page(
            sys.argv[1], 0)
        startingNode.populateLinks()
        endNode = Page(sys.argv[2], 0)
    except:
        print("Error!")

    result = BFS(startingNode, endNode.url)
    if result:
        print("\t"+result)
    else:
        print(
            f"\t{startingNode.getName()} has no links to {endNode.getName()}. Please try again!")


def BFS(initialNode, destUrl):
    queue = [initialNode]
    visited = []

    while len(queue) > 0:
        s = queue.pop(0)
        visited.append(s.url)

        if s.url == destUrl:
            final_str = s.getName()
            itr = s.parent

            while itr:
                final_str = itr.getName() + '--->' + final_str
                itr = itr.parent

            return final_str

        s.populateLinks()

        if s.depth <= 6:
            for link in s.links:
                if link not in visited:
                    node = Page(link, s.depth + 1)
                    node.parent = s
                    queue.append(node)

    return None


if __name__ == '__main__':
    main()
