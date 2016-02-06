'''
Get all of the lecture names from www.sis.itu.edu.tr using lecture codes using BeautifulSoup web scraper
e.g. BLG for Computer Engineering
Usage: python q3.py <Lecture Code>
'''


from bs4 import BeautifulSoup
import urllib2, sys

__author__ = 'Yigit Bekir Kaya <admin@cbilab.org>'

try:
    # If the arguments are not correct raise a value error
    if len(sys.argv) != 2:
        raise ValueError('Usage: python q3.py <Lecture Code>')

    # Format the URL
    url = 'http://www.sis.itu.edu.tr/tr/ders_programlari/LSprogramlar/prg.php?fb={0}'.format(sys.argv[1])

    # Open the URL
    response = urllib2.urlopen(url)

    # Read the whole page into html_doc
    html_doc = response.read()

    # Parse the whole page using html.parser from BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Select all of the table cells with <td> tag
    all_td = soup.select('td')

    # First lecture name is in the 36th td tag and repeats at every 14 cells until all tds
    for i in range(36, len(all_td), 14):

        # Get the td with index i and print the text of it
        print all_td[i].text

except ValueError as ve:
    print ve.message
except Exception as e:
    print 'Something went wrong {0}'.format(e.message)
