# Python Profiling

## cProfile: A deterministic profiler

- Built-in to python
- Traces every function call in a program
- By default measures process CPU
- You probably don't want to use it?

Every function call gets wrapped

Tells you how many times every function was called
How much cpu a particular function used

```python
start = process_time()
try:
  f()
finally:
  elapsed = process_time() = start
```

### Problems

#### 1 - Function wrapping

Function wrapping causes the parts of the code that have more functions to get more overhead

#### 2 - Too much information

Too much information: Profile every single function, lots of noise

#### 3- Offline measure of performance

- Your program may be slow when in real world
- But cProfile has enough overhead you probably don't want to run it in production
- Only suitable for running on your laptop

#### 4- Measure slowness on function level

Sometimes the argument of a function determine the speed, e.g. database query, more data to process, etc.

```pyton
slowFunction(100) # is fast

slowFunction(0) # is slow
```

And cProfile only tells you that the average of slowFunction is slow, but figuring out what particular input causes to make it slow is hard.

### Benefits

- Non-CPU: all time spent waiting for non cpu events
- Number of voluntary context switches(systems calls that take a long time)
- Memory allocations
- Any counter that goes up

## Pyinstrument

A statistical profiling tool

It doesn't track every function call, instead records the stack every 1ms

Much lower overhead than tracing profilers

It uses real world time instead of cpu time which includes network time, io, etc.

It hides library calls by default allowing you to focus on your app code.

## py-spy

Super fast sampling profiler written in Rust that runs in a different process

Looks like it has too much noise compared to pyinstrument

## Eliot

Allows you to inspect the time, input and output of functions that you suspect are taking too long.

Its like having a magnifiying glass once you find a slow function :)

TODO: Write more detailed description https://eliot.readthedocs.io/en/stable/

## Rule of thumb

Always add logging
Use pyisntrument as default profiler
Use cProfile if you need a custom profiler

## All profilers

https://github.com/itamarst/eliot
https://github.com/joerick/pyinstrument
https://github.com/benfred/py-spy

## Sources

[Beyond cProfile: performance optimization with sampling profilers and logging](https://www.youtube.com/watch?v=fOzVTPOWfQs)

[slides](https://pythonspeed.com/pygotham19/slides)

## TODO

https://medium.com/@antoniomdk1/hpc-with-python-part-1-profiling-1dda4d172cdf

https://medium.com/pinterest-engineering/api-profiling-at-pinterest-6fa9333b4961

- Slides has some extra useful links

https://docs.python.org/3/library/debug.html

https://docs.python.org/3/library/profile.html