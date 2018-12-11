# yelp12

My entry for the Yelp Dataset Challenge Round 12

## Current

* Reevaluate necessary analytics
* Select and isolate experiement data
  * 1 business with 100-150 reviews per star
  * 2 businesses with 150-250 reviews per star
  * 8 businesses with 100-200 reviews per star
  * 30 with 50-99 and 97 with 50-150

## Milestones

### Access Data

* [x] Access the data as a quickly traversable json.
* [x] Stream review JSON due to length (5,000,000+ lines)

### Sort Data by Metropolitan Area

* [x] Plot all data on a global map by latitude and longitude
* [x] Set opacity to 5 or 10% to view strong clusters
* [x] Select region barriers by max lat and long from 10 strongest clusters

### Select Training Data

Assess shape of data:

* [x] Number of Businesses
* [ ] Number of Businesses / urban area
* [x] Max number of reviews
* [x] Avg number of reviews
* [x] Max and Avg reviews per star
* [x] Find Businesses with similar number of reviews per stars
  * [ ] May not have similar number of reviews per star
* [x] Business with minimum number of review per star
* [ ] Minimum Reviews for 1 and 5 or 2 and 4
* [ ] Review Length
* [ ] Words per review
* [ ] Make a plot of words per review
* [ ] Set summary length to some length beyond avg

Also:

* [ ] Find business types
* [ ] Maybe use businesses from different types during iterations

### Summarize Reviews

* [ ] Use TFIDF methods
* [ ] Key Tokens (Topic)
* [ ] Representative Review
* [ ] Extractive Summary
  * Possibly use useful, funny, or cool in weighting metric
* [ ] Generate one summary with RNN method

* [ ] Apply these methods on the Star rating and Business level