---
title       : Why should we use regular expressions?
description : In this chapter I will motivate you to use Regular expressions!
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:ab57cc6e24
##Regular expressions and text

Regulars expressions allow us to analyse flat text. But which text? Text we refer to is everywhere, in the code, in webpages, in text data files... it is *almost* everywhere. Well, there are some files that we cannot use regular expressions or *regex*. These are *binary* and *compiled* files. Office documents are *binary* files. 
**Which of the following files does not have flat text, and cannot be analyzed with Regular expressions?**

*** =instructions
- Python code file (.py)
- A web page (.html)
- A word document (.docx)
- A style file (.css)
*** =hint
Have a look at heading of this exercise and observe that it refers to a specific file in this list?
*** =sct
```{r}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# testwhat R package

msg_bad <- "That is not correct! you can use regular expression with this type of file as it is stated in the heading of this question"
msg_success <- "Exactly! Word document files are Office files and they are cannot be analyzed with Regex."

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(correct = 3, feedback_msgs = c(msg_bad,  msg_bad, msg_success, msg_bad)) 
```

--- type:NormalExercise lang:r xp:50 skills:1 key:452b676422
##Text and string/character variables

In the previous exercise we learned that regular expression can be used in *string* or so called in R *character* variables. However; we need to see the structucture of this character to understand how to select the best strategy for using *regex*

*** =instructions
- load the movies database from http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv using the build in read.csv function to the movies dataframe
- Observe the first 6 observations of the title variable looks like using the function head
- Observe the first 15 observations of the title variable looks like using the function head
- After reflecting of the structure of the TRUE after the line


*** =hint
- Please run the code shown in the item
- Please run the code shown in the item
- Please run the code shown in the item
- Please run the code shown in the item


*** =sample_code
```{r}

# Uncomment the line below
# movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)

# Observe the first 6 observations in the title variable from the movie dataframe, uncomment the line below
#head(movies$title)

# Observe the first 15 observations in the title variable from the movie dataframe, uncomment the line below
#head(movies$title)

# When you have reflected about the structure of the data please run TRUE


```

*** =solution
```{r}
# Uncomment the line below
movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)

# Observe the first 6 observations in the title variable from the movie dataframe, uncomment the line below
head(movies$title)

# Observe the first 15 observations in the title variable from the movie dataframe, uncomment the line below
head(movies$title)

# When you have reflected about the structure of the data please run TRUE

```

*** =sct
```{r}
test_object("movies")
test_function("head", args = "object",
              not_called_msg = "You didn't call `head()`!",
              incorrect_msg = "You didn't call `head(object = ...)` with the correct argument, `object`.")
test_function("head", args = c("object", 15),
              not_called_msg = "You didn't call `head()`!",
              incorrect_msg = "You didn't call `head(object = ...)` with the correct argument, `object`.")


# It's always smart to include the following line of code at the end of your SCTs
# It will check whether executing the student's code resulted in an error, 
# and if so, will cause the exercise to fail
test_error()

# Final message the student will see upon completing the exercise
success_msg("Good work!")
```
--- type:MultipleChoiceExercise lang:r xp:50 skills:1 key:0d507f6f0e
##Regular expressions jargon!

Regulars expressions have 2 main components. The *literals* and the *metacharacters*. The literals are any *number*, *alphabetic* or **some** *signs* that have no other meaning than themselves. *1* means *1*, *a* means *a*, *,* means *,*. The *spaces*, *tabulation*, *line breaks* all of them are *literals*. The metacharacters have a special meaning, and we discuss them later. They are always: *.^$?+()[]{}*

**Which of the following regex contains at least a metacharacter?**

*** =instructions
- Hello, my name is Peter Parker!
- What is your name?
- I don't have time for your foolishness: 
- Be my guest!
*** =hint
Have a look at heading of this exercise and observe that it refers to a specific file in this list?
*** =sct
```{r}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# testwhat R package

msg_bad <- "there is no metacharacter in this regex"
msg_success <- "Exactly! the question mark ? is a metacharacter"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(correct = 2, feedback_msgs = c(msg_bad, msg_success, msg_bad,msg_bad)) 
```
