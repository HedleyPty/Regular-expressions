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

--- type:NomalExercise lang:r xp:50 skills:1 key:452b676422
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

# load the movies database from http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv using the build in read.csv function to the movies dataframe: movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)

# Use head(movies$Title) to observe the first 6 observations in the title variable from the movie dataframe

# Use head(movies$Title, 15) to observe the first 15 observations in the title variable from the movie dataframe

# When you have reflected about the structure of the data please run TRUE


```

*** =solution
```{r}
# load the movies database from http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv using the build in read.csv function to the movies dataframe: movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)
movies <- read.csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv", stringsAsFactors=F)

# Use head(movies$Title) to observe the first 6 observations in the title variable from the movie dataframe
head(movies$Title)

# Use head(movies$Title, 15) to observe the first 15 observations in the title variable from the movie dataframe
head(movies$Title, 15)

# When you have reflected about the structure of the data please run TRUE
TRUE

```

*** =sct
```{r}
test_object("movies")
test_function("head", args = "object",
              not_called_msg = "You didn't call `str()`!",
              incorrect_msg = "You didn't call `str(object = ...)` with the correct argument, `object`.")
test_function("str", args = c("object", 15),
              not_called_msg = "You didn't call `str()`!",
              incorrect_msg = "You didn't call `str(object = ...)` with the correct argument, `object`.")


# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# testwhat R package. Documentation can also be found at github.com/datacamp/testwhat/wiki

# Test whether the function str is called with the correct argument, object
# If it is not called, print something informative
# If it is called, but called incorrectly, print something else
test_function("str", args = "object",
              not_called_msg = "You didn't call `str()`!",
              incorrect_msg = "You didn't call `str(object = ...)` with the correct argument, `object`.")

# Test the object, good_movies
# Notice that we didn't define any feedback here, this will cause automatically 
# generated feedback to be given to the student in case of an incorrect submission
#test_object("good_movies")

# Test whether the student correctly used plot()
# Again, we use the automatically generated feedback here
# test_function("plot", args = "x")
# test_function("plot", args = "y")
# test_function("plot", args = "col")

# Alternativeley, you can use test_function() like this
# test_function("plot", args = c("x", "y", "col"))

# It's always smart to include the following line of code at the end of your SCTs
# It will check whether executing the student's code resulted in an error, 
# and if so, will cause the exercise to fail
test_error()

# Final message the student will see upon completing the exercise
success_msg("Good work!")
```

--- type:NormalExercise lang:r xp:100 skills:1 key:7ea2125df4
## More movies

In the previous exercise, you saw a dataset about movies. In this exercise, we'll have a look at yet another dataset about movies!

A dataset with a selection of movies, `movie_selection`, is available in the workspace.

*** =instructions
- Check out the structure of `movie_selection`.
- Select movies with a rating of 5 or higher. Assign the result to `good_movies`.
- Use `plot()` to  plot `good_movies$Run` on the x-axis, `good_movies$Rating` on the y-axis and set `col` to `good_movies$Genre`.

*** =hint
- Use `str()` for the first instruction.
- For the second instruction, you should use `...[movie_selection$Rating >= 5, ]`.
- For the plot, use `plot(x = ..., y = ..., col = ...)`. 

*** =pre_exercise_code
```{r}
# Pre-load a package in the workspace
library(MindOnStats)

# You can prepare the data before the student starts:
data(Movies)
movie_selection <- Movies[Movies$Genre %in% c("action", "animated", "comedy"),c("Genre", "Rating", "Run")]

# You can also clean up data so that it's not available in the student's workspace anymore:
rm(Movies)
```

*** =sample_code
```{r}
# movie_selection is available in your workspace

# Check out the structure of movie_selection


# Select movies that have a rating of 5 or higher: good_movies


# Plot Run (i.e. run time) on the x axis, Rating on the y axis, and set the color using Genre

```

*** =solution
```{r}
# movie_selection is available in your workspace

# Check out the structure of movie_selection
str(movie_selection)

# Select movies that have a rating of 5 or higher: good_movies
good_movies <- movie_selection[movie_selection$Rating >= 5, ]

# Plot Run (i.e. run time) on the x axis, Rating on the y axis, and set the color using Genre
plot(good_movies$Run, good_movies$Rating, col = good_movies$Genre)
```

*** =sct
```{r}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# testwhat R package. Documentation can also be found at github.com/datacamp/testwhat/wiki

# Test whether the function str is called with the correct argument, object
# If it is not called, print something informative
# If it is called, but called incorrectly, print something else
test_function("str", args = "object",
              not_called_msg = "You didn't call `str()`!",
              incorrect_msg = "You didn't call `str(object = ...)` with the correct argument, `object`.")

# Test the object, good_movies
# Notice that we didn't define any feedback here, this will cause automatically 
# generated feedback to be given to the student in case of an incorrect submission
test_object("good_movies")

# Test whether the student correctly used plot()
# Again, we use the automatically generated feedback here
test_function("plot", args = "x")
test_function("plot", args = "y")
test_function("plot", args = "col")

# Alternativeley, you can use test_function() like this
# test_function("plot", args = c("x", "y", "col"))

# It's always smart to include the following line of code at the end of your SCTs
# It will check whether executing the student's code resulted in an error, 
# and if so, will cause the exercise to fail
test_error()

# Final message the student will see upon completing the exercise
success_msg("Good work!")
```