# RandomPolynomials
Fix a positive integer n and an interval I = [a, b] in the real line. Pick coefficients of an n degree polynomial uniformly at random from I. What is the distribution over such random polynomials? 

It can be proved that the roots will tend to converge around the unit circle! This python script displays this wonderful fact. Simply run the script "rootsunity.py" and it will produce a plot similar to RootsUnity.png. 

The current interval is [-1, 1] but this can be easily changed by altering the code as shown:

```python
 np.random.uniform(-1, 1, deg)
```
A heurisic proof of this fact can be found [here.](http://mathoverflow.net/questions/182412/why-do-roots-of-polynomials-tend-to-have-absolute-value-close-to-1)

