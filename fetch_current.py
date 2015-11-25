#!/usr/bin/env python

import yaml
import urllib2
import json
from pprint import pprint

CONFIG = yaml.load(open('config.yaml'))
ACCESS_KEY = CONFIG['access_key']

def main():
	country,city = CONFIG['target']['country'].replace(' ','_'), CONFIG['target']['city'].replace(' ','_')
	raw = urllib2.urlopen('http://api.wunderground.com/api/{0}/conditions/q/{1}/{2}.json'.format(ACCESS_KEY,country,city))
	json_data = json.loads(raw.read())
	current = json_data['current_observation']
	
	current_metrics = {} 
	for key in CONFIG['metrics']: current_metrics[key] = current[key]	
		
	pprint(current_metrics)



if __name__ == '__main__':
	main()
