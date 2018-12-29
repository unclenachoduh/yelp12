# Extractive Summarization on Yelp Reviews

**Kekoa Riggin**  
University of Washington  
kekoar@uw.edu

## Abstract

_The results of creating a tf-idf-based extractive summarization system for the Yelp Dataset Challenge Round 12. Using reviews of the same star rating as a docset, summarization can identify why businesses are receiving different ratings to see what they are doing well and not so well._

## Introduction



## System

This system generates summaries of a collective set of Yelp reviews based on their star rating.

The features and methods for summarization are detailed in the following subsections.

### Extractive Summarization

The summarization engine used in this project is an extractive system. Extractive summarization uses segments that are present in the system to compile a condensed representation of the entire body and is the counterpart to abstractive summarization, which generates original summary text. *Source*.

### Modified TFIDF

In order to select segments that contribute to an informative summary, this system uses a modified version of the tf-idf weighting scale. *Quick statement about tf-idf with source*.

In this system, each word found in a review is treated as a term, or as *CLASSY PAPER* put it, an idea. These terms comprise the message of the review, and the goal of this system is to identify the central idea of the reviews. A tf-idf score is a way of evaluating the centrality of each term.

Traditional tf-idf scores, however, favor terms that have a high density in few documents. In order to find the central message of the reviews of a single star rating, this system uses a scoring metric that favors terms that appear in many documents in the target star rating but reduces the score of a term that appears often in other star ratings as well.

The weighting metric used in this system is a tf-df\*itf-idf, where tf-df is the term frequency multipled by document frequency in reviews of the target star rating and that is multiplied by itf-idf, which is the inverse term frequency multiplied by the inverse document frequency in reviews belonging to reviews with star ratings outside of the target. 

### Data

The data comes from the reviews file from the Yelp Dataset for Round 12.

The data used for summarization is extracted from the "text" value of each review.

In modeling the data, each review is considered as a document. All reviews from one business that have the same star rating comprise a docset. Thus, each business hase 5 docsets (one for each star rating), and each docset is the collection of reviews with that star rating.

Businesses used in this experiment were selected for having a similar number of reviews per star rating and a large enough number of reviews to generate extractive summaries. This system could run on any business in the dataset, but its reliability on smaller docsets may vary.

Of the businesses used, there are:

* 1 Business with 100-150 reviews per star rating
* 8 Businesses with 100-200 reviews per star rating
* 2 Businesses with 150-250 reviews per star rating
* 30 Businesses with 50-99 reviews per star rating

### Evaluation

* Stop words and punctuation (clean for meaningful "terms")

* For generated results, calculate difference in "terms" (% coverage = ~ terms)

The qualitative value of terms is not measured by term coverage. This measurement indicates that the system consistently captures a wider range of terms (or ideas) than randomly generated summaries. Additional evaluation is necessary to determine whether the terms capture the central idea of reviews.

### Performance

#### Manual

#### Coverage Analysis

## Discussion

### Notable Results

Difference in topic words and analytics in 5 star reviews: Top topic words usually stop words, avg length always shorter.

### Performance

* Manually reviewed performance.

* Beats summarizations generated at random in coverage.

* Additional qualitative analysis necessary.
* Comparing to a curated summary using ROUGE or BLEU.

## Further Study

* Qualitative Evaluation

* Abstractive summarization.

## Sources

* Extractive/Abstractive Summarization
* tfidf
* LING 573 System
* Classy Method
* ROUGE and BLEU summarization scores
* Abstractive Methods