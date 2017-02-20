"""
json_io.py

Functions related to reading/writing lists to json and json to lists
"""


import json
from datetime import datetime

def list_from_json(json_file):
    """Return a list corresponding to contents of json file"""

    with open(json_file, 'r') as fp:
        return json.load(fp)

def list_to_json(lst, path):
    """Save a list to a json file at corresponding path."""

    with open(path, 'w') as fp:
        json.dump(lst, fp, sort_keys=True, indent=4)

def merge_json_filenames(json_lst):
    """
    Return filename encapsulating date range of passed in jsons
    ex: merge_json_filnames(["path/to/jsons/2017-01-27_2017-02-04.json", "path/to/jsons/2017-02-02_2017-02-09.json"])
        returns "2017-01-27_2017-02-09.json"
    """
    # Get earliest and latest date of jsons for naming purposes of merged file.
    parse_date_from_filename = lambda fn: fn.split('/')[-1].split('.')[0].split('_')
    sorted_dates = sorted([datetime.strptime(date, "%Y-%m-%d") for fn in json_lst for date in parse_date_from_filename(fn)])
    from_date = datetime.strftime(sorted_dates[0], "%Y-%m-%d")
    to_date = datetime.strftime(sorted_dates[-1], "%Y-%m-%d")
    return "{}_{}.json".format(from_date, to_date)
