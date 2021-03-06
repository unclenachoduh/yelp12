# Yelp Dataset Challenge Round 12 Entry

A TF\*IDF extractive summarization system for Yelp reviews.

Read the [full report](report.md).

## Description

This system summarizes the reviews for a business that can be found in the Yelp Dataset.

For each busisness, five summaries are generated: one fore each star rating. The summaries are generated from the collection of reviews of a star rating by weighting words found in reviews of that star rating heavier and weighting words found in reviews of other star ratings for the same business.

## Running the System

Make sure you meet [system requirements](#Dependencies).

Because Yelp Dataset Challenge participants must keep the dataset confidential, the structure of this repo is not ideal.

Currently, the systems operates from outside of the main folder, `yelp12`. The unzipped dataset folder should be in `yelp12`'s parent folder.

In this parent folder, use the command:  
`python3 yelp12/src/main.py <business_id>`  
to generate summaries.

`<business_id>` is the unique identifier for a business found in the dataset.

Many businesses can be summarized at once with the command:  
`python3 yelp12/src/main.py -b <business_file>`  
where `<business_file.` is a file containing the IDs of several businesses on separate lines. [recommended_businesses.txt](recommended_businesses.txt) contains some IDs that are recommended based on the similar number of reviews per star rating.

## Evaluating Summaries

Because curated summaries are not available, faithful evaluation of generated summaries relies on manual analysis of the reviews used to generate a summary.

However, this system includes a simple coverage analysis script that demonstrates the possible significant terms that are covered by the summary.

This analysis compiles up to n-grams up to 3 of all reviews used to generate a summary and of the summary itself. These n-grams comprise only sequences that do not contain common stop words or punctuation. The score is simply the percent of these rudimentary terms that are present in the summary.

In addition to the score for the generated summary, a set of 10 random summaries are generated from the source reviews and the score is calculated for these summaries as well for comparision with the system.

## System Performance

Performance was assessed manually for one business and with the coverage script for 40 businesses.

### Manual Revision

**ID:** VUtazCTIc0aoOrQprP_s-Q

**Number of Reviews**

| 1 Star | 2 Star | 3 Star | 4 Star | 5 Star |
| - | - | - | - | - |
| 124 | 108 | 108 | 147 | 123 |

**Results**

*description needed*

**Coverage Analysis Comparison**

| | 1 Star | 2 Star | 3 Star | 4 Star | 5 Star | Avg. |
| - | - | - | - | - | - | - |
| Generated | 2.85% | 4.93% | 4.80% | 2.52% | 4.44% | 3.91% |
| Random | 2.82% | 3.48% | 3.43% | 3.20% | 3.13% | 3.22% |


### Results from Coverage Analysis Script

Results for the 40 businesses assessed with the coverage analysis script.

#### Batch of 30 Businesses

Businesses with 50-99 reviews per star

**System Wins:** 92 / 150

**Average Coverage**

| Generated | Random |
| - | - |
| 5.96% | 5.33% |

#### Batch of 10 Businesses

Businesses with 100-150, 100-200, or 150-250 reviews per star

**System Wins:** 35 / 50

**Average Scores:**

| Generated | Random |
| - | - |
| 3.31% | 2.86% |

## TF\*IDF

The weighting metric used is a modified [TF\*IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

**TF** stands for **Term Frequency**, meaning the number of times a term appears in a text. **IDF** stands for **Inverse Document Frequency**, meaning 1 divided by the number of documents the term appears in.

My system uses a (TF\*DF) \* (ITF\*IDF) weighting metric, where TF\*DF is the term frequency and document frequency in reviews with the star rating being summaried, and ITF\*IDF is the inverse of each in reviews of all other star ratings.

This weighting rewards terms that unique to the reviews of the star rating being summarized and should help identify the reason a Yelp reviewers give certain star ratings.

## Dependencies

Python 3  
[NLTK](https://www.nltk.org/) (This system relies heavily on NLTK's tokenization packages.)

This system was built on Ubuntu 18.4.1.

## TODO

* [ ] Move Analytics data to repo
  * [ ] Use analytics for write up

* [ ] Analyze contents of reviews
  * [ ] VUtazCTIc0aoOrQprP_s-Q 100-149
  * [ ] Tally topics covered in reviews
  * [ ] Order topics by tally count
  * [ ] Identify the number of high-ranking topics covered in summary per star
  * [ ] Maybe create a scoring method 
  	* 1st = 10 pts, 2nd = 9 pts, etc
  	* 1 / place ( 1st = 1/1, 2nd = 1/2, ect.)

* [ ] Compile final report and document the code

* [ ] Clean up repo
* [ ] Move tools to another repo

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
* [x] Minimum Reviews for 1 and 5 or 2 and 4
* [x] Review Length
* [x] Words per review
* [ ] Make a plot of words per review
* [ ] Set summary length to some length beyond avg

Also:

* [ ] Find business types
* [ ] Maybe use businesses from different types during iterations

### Summarize Reviews

* [x] Use TFIDF methods
* [x] Key Tokens (Topic)
* [x] Representative Review
* [x] Representative Sentence
* [x] Extractive Summary
  * Possibly use useful, funny, or cool in weighting metric
* [x] weight sentences by the percent of their review they represent
* [x] Generate one summary with RNN method
  * [ ] Improve this method

* [ ] Apply these methods on the Star rating and Business level
