'''
    Implement BFS using wikipedia urls and the links in the wiki page.
    Store url, title, links in the page, and the parent link in the list.
'''

from page import Page


def main():
    page_list = []

    # Testing Purposes
    hello = Page(
        "https://en.wikipedia.org/wiki/Gunilla_Carlsson")
    hello.populateLinks()
    hello.getName()
    for i in hello.links:
        print(i)


if __name__ == '__main__':
    main()
