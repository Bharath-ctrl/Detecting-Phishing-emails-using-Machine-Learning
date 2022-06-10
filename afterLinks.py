import sqlite3
import re
import pandas as pd

from string import punctuation

connection=sqlite3.connect("Project.db",check_same_thread=False)
listofTabs = connection.execute("select name from sqlite_master where type='table' AND name='user'").fetchall()
cur=connection.cursor()

from html.parser import HTMLParser
class Parser(HTMLParser):
  # method to append the start tag to the list start_tags.
  def handle_starttag(self, tag, attrs):
    global start_tags
    start_tags.append(tag)
    # method to append the end tag to the list end_tags.
  def handle_endtag(self, tag):
    global end_tags
    end_tags.append(tag)
  # method to append the data between the tags to the list all_data.
  def handle_data(self, data):
    global all_data
    all_data.append(data)
  # method to append the comment to the list comments.
  def handle_comment(self, data):
    global comments
    comments.append(data)
start_tags = []
end_tags = []
all_data = []
comments = []
# Creating an instance of our class.
parser = Parser()
abc=cur.execute("SELECT dbhtmlbody FROM user as qw").fetchall()
ocs=len(abc)
for row in range(ocs):
    #ocs[row[0]]=int(row[0])
    print(abc[row])
    # parser.feed(str(abc[row]))
    # # print("start tags:", start_tags)
    # # print("end tags:", end_tags)
    # print("data:", all_data)
    # def print_text(sample, clean):
    #     print(f"Before: {sample}")
    #     print(f"After: {clean}")

    # df=pd.DataFrame(all_data)
    # def preprocess_text(text):
    #     text = text.lower()  # Lowercase text
    #     text = re.sub(f"[{re.escape(punctuation)}]", "", text)  # Remove punctuation
    #     text = " ".join(text.split())  # Remove extra spaces, tabs, and new lines
    #     return text

    # #df[all_data].map(preprocess_text)
    # sample_text=df[all_data].map(preprocess_text)
    # clean_text = sample_text.lower()
    # print_text(sample_text, clean_text)
    # urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', clean_text)
    # print(urls)
