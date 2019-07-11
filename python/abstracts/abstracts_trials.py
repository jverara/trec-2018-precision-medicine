import json
from json2html import *
from IPython.display import display, HTML
import pandas

import os, sys
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
from trec_utils import utils#, running, evaluation

config = utils.load_config()

topics_all = utils.get_topics('./topics/topics2019.xml')
qrels_all = utils.get_qrels('./gold-standard/abstracts.2017.qrels')

TOPIC = 12
topic1 = topics_all[(topics_all.topic==TOPIC)]

TOPIC = 9
topic2 = topics_all[(topics_all.topic==TOPIC)]

TOPIC = 15
topic3 = topics_all[(topics_all.topic==TOPIC)]

TOPIC = 7
topic4 = topics_all[(topics_all.topic==TOPIC)]
#qrels = utils.qrels_of_topics(qrels_all, topic)
display(topic1)
display(topic2)
display(topic3)
display(topic4)