**Answer to a potential coding question interview**

After attending a Microsoft coding session on campus, I ended up with an unsolved problem:

*Let consider a sequence of numerical values such as V = [100,0,70,2,1010]. The size of the sequence or list is unknown. The problem is to find the maximal difference between the values of the sequence. For the sequence V, the result is 1010 - 0 = 1010*

My understanding of the above is that we are looking for the difference between the minimum and the maximum. The ways to find that value are:

+  order the sequence and do the difference between the first element and the last element of the ordered sequence;
+  take an element as the starting point; compute the difference between the starting point and others elements; the maximal positive difference and the minimal negative difference will give the maximal difference of the sequence.

**Idea :**

I applied the way #2 in the file "maxi_difference.py". The advantage is that there is no need to order the sequence and the starting point can be any element inside the sequence.

The starting point is the first element of the sequence. The positive difference is the difference between the first element and any other element less than itself. The negative difference is the difference between the first element and any other element greater than itself.

**Tools :**
Python 3.7.3 [GCC 7.3.0] :: Anaconda(spyder)
