# 01-intro
## Main part
- [Original Jupyter notebook from the lecture](duration-prediction.ipynb)
- [Homework tasks](homework.md)
- [My homework solutions (basic DictVEctorizer+Linear model)](homework-solution.ipynb)

## Extra materials
### Experiment: lookup table instead of DictVEctorizer+Linear
When we treat locations simply as categories, and use DictVectorizer (which is effectively one hot encoder), to encode them, we basically ignore all the location semantics: what is close, what is distant, - we just drop all this possibly available information. And it seemed to me that when they use a linear model on a data like this, we basically memorize the mean duration values for each combination of two categories. Not exactly, but very close to that. And I wanted to demonstrate that if I use just a very simple lookup table instead, I could get very similar results using the same number of dimensions for encoding. 

So, I created a basic lookup table for 515 most frequent combinations of pickup and drop off locations. I memorized the mean durations for them. I used one more category to store the overall mean as a fallback. And no big surprise, the final results are very close to what we got in the basic solution. 

See [Notebook](lookup-table-baseline.ipynb)

### Experiment: OHE with a twist

We encode both pickup location and drop off location using the same one-hot encoding. So in total, we get 261 labels instead of 515. And accordingly, 261 dimensions. And we plug them into a linear model by labeling Pickup locations with $+1$ and Dropoff locations with $-1$. In this case, we implicitly assume that the duration riding from A to C is about the same the sum of riding from A to B and from B to C. Which is not exactly the case but this could be a good approximation.

Results: we get RMSE on train 8.82 and RMSE on validation 9.06, which is very close to the basic solution. But, we have reduced the dimensionality of the feature matrix by half.

See [Notebook](homework-solution-with-twist.ipynb)