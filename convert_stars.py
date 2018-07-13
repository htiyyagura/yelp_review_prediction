import os
import sys
import json

REVIEW_RESTAURANTS_FILE = './reviews_restaurants.json'

def load_json(fname):
  with open(fname) as f:
    for line in f:
      yield json.loads(line)

def convert_stars():
  with open('./reviews_restaurants_sentiment.json', 'w') as o:
    for review_data in load_json(REVIEW_RESTAURANTS_FILE):
      #print("1", review_data)
      #print("2", review_data['stars'])
      if review_data['stars'] == 5:
        #print("in if", review_data['stars'])
        counter = 5
      elif review_data['stars'] == 4:
        #print("in elif", review_data['stars'])
        counter = 5
      else:
        #print("in else", review_data['stars'])
        counter = 1
      print("counter", counter)
      review_data['stars'] = counter
      o.write(json.dumps(review_data))
      o.write('\n')

def main():
	convert_stars()

if __name__ == '__main__':
    main()