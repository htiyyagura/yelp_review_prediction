import os
import sys
import json

REVIEW_DATA_FILE = './yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'
BUSINESS_DATA_FILE = './yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json'

def load_json(fname):
  with open(fname) as f:
    for line in f:
      yield json.loads(line)

def get_reviews():
  restaurants = set()
  for business_data in load_json(BUSINESS_DATA_FILE):
    if "Restaurants" in business_data["categories"]:
      restaurants.add(business_data["business_id"])

  with open('./reviews_restaurants.json', 'w') as o:
  	for review_data in load_json(REVIEW_DATA_FILE):
  		if review_data['business_id'] in restaurants:
  			#print(review_data)
  			o.write(json.dumps(review_data))
  			o.write('\n')
  
def main():
	get_reviews()

if __name__ == '__main__':
    main()