## User guide note
This user guide assumes some basic familiarity with R software. If you would like to run the code in this guide in your own R interface, make sure you also download the associated folder "userguide_files" which includes the different dictionary versions and necessary functions. We are working on a version of the Grievance Dictionary that does not require R knowledge!

## What is the Grievance Dictionary?

The Grievance Dictionary (GD) can be used to assess grievance-fuelled communications through language. There are 22 psychological and content categories currently measured with the Grievance Dictionary, namely:

* Planning
* Violence
* Weaponry
* Help seeking
* Hate
* Frustration
* Suicide
* Threat 
* Grievance
* Fixation
* Desperation
* Deadline
* Murder
* Relationship 
* Loneliness
* Surveillance
* Soldier
* Honour
* Impostor
* Jealousy
* God
* Paranoia


## Dictionary versions

Importantly, there are several versions of the dictionary that can be used based on the aims of your analysis. First, you need to know there are two approaches to measuring GD categories. 

### Proportional scoring (wordcount-based)
The first approach makes use of word counts, where words from the dictionary categories are searched and counted in your text(s) of interest. These counts are then divided by the total number of words in the text, resulting in a proportion score. You can then obtain the proportion for each GD category (i.e., the sum of all individual word proportions in the category) as well as the proportion scores for each individual word found in the text(s). 

### Weight-based approach
The second approach makes use of weights assigned to each word in the GD obtained through crowdsourced annotations. Each word was rated for the extent to which it fits into its overarching category (scale 0-10). For example, the word "knife" fits well into the category "weaponry" and may have a weight of 9. In the weight-based approach words from the dictionary categories are searched and the associated weight is assigned. You can then obtain the average for each GD category as well as the individual words found in the text(s).

### Word inclusion criteria
For both the word count and weight-based approaches, it is important to select a dictionary with the word inclusion criteria of your choice. The analyses in our paper were all performed with the GD which includes words that received a goodness-of-fit rating of at least 7 or higher. Alternatively, you can opt for a less stringent version including words with a rating of 5 or higher. For the weight based approach, you may also opt for a dictionary which includes all words and their associated weights. Note that the words in this dictionary will range from very low to very high goodness-of-fit weights. 

## Using the Grievance Dictionary
Applying the Grievance Dictionary relies on two main functions. The 'grievance_lookup' function can be used for any word count-based approach, and the 'grievance-weights' function for any weight-based approach. The dictionary version (e.g., average rating of 7 or higher) can be specified in each function. You can see both functions at work below.

But first, it's important to note a few things.

* The GD functions need to be supplied with a character vector of text(s) and the dictionary version of choice
* You can opt out of obtaining the individual word matches if you specify 'return_words = F'
* The GD functions stem all words in the text of interest in order to find the right matches (e.g., 'friendly' becomes 'friend')

```{r}
# Some preparations first..
# Define an example text
example_text = "This is an example of a very violent text, I will do horrible, deadly, bloody things. I will use my AK-47, and several knives and machetes for stabbing. I am very frustrated by this, but this is my final warning. I am obsessed with achieving this, so beware of my attack."

# Now, source the GD functions.
source('grievance_lookup.R')
source('grievance_weights.R')
```

### Proportional scoring: rating of 7 and higher
Now, let's apply the functions to the example text. We first use the GD version with words that received an average rating of _7 or higher_. This is the recommended version, also used in the paper. We also choose to return the individual word matches found, to give you an idea of what the GD looks for. Note this will return a list.

```{r message=FALSE, warning=FALSE}
load('qdictionary_7plus.Rdata')
results_1 = grievance_lookup(example_text, # specify the text vector
                            remove_short = T, # remove texts with less than 50 words 
                            dict = qdictionary_7plus, # specify the dictionary version
                            df_or_dfm = "dfm") # return a document-feature-matrix

# Look at the results (a list with two elements)
print(results_1, max_nfeat = 23) # gives you the scores per category and the % of words not matched
```
In the code above, we can see that there are some matches in the example text for several categories. We have no matches for the categories god, impostor, or relationship. Indeed, when you look back at the example text there is no mention of religion, impostor delusions, or love.

### Proportional scoring: rating of 5 and higher
We will get similar looking results (albeit slightly higher proportions) if we use the less stringent version of the GD, which includes words which received a score of _5 or higher_. This time we do not choose to return the individual matches, so the output is a dataframe, not a list. 

```{r message=FALSE, warning=FALSE}
load('qdictionary_5plus.Rdata')
results_2 = grievance_lookup(example_text, # specify the text vector
                            remove_short = T, # remove texts with less than 50 words 
                            dict = qdictionary_5plus, # specify the dictionary version
                            df_or_dfm = "dfm") # return a document-feature-matrix

# Look at the results (a dataframe)
print(results_2, max_nfeat = 23)
```

### Weight-based scoring
Lastly, we use the weight-based version of the GD. This looks for all 20,502 words in your text and assigns the average weight. The output of this function looks slightly different.
```{r message=FALSE, warning=FALSE}
load('weighted_dictionary.Rdata')
results_3 = grievance_weights(example_text) # specify whether you want individual matches returned

# Look at the results
results_3

```

## Usage in practice
Please refer to our paper for a breakdown of all usage posibilities of the Grievance Dictionary, as well as its limitations. In the paper, we used the GD to make statistical comparisons between different text samples (e.g., texts written by known lone-actor terrorists and non-violent individuals) but as you have seen above the GD can also be used to gain a general picture of a text (or several texts). The dictionary categories may also be used as features in machine learning prediction (please see the paper for details).

Please get in touch if you have any questions! (isabelle.vandervegt@ucl.ac.uk)