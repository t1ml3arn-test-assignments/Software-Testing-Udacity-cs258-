## Lesson 3 - Coverage

### What is coverage

Coverage shows how much code is being tested. There are many metrics for this.

### Is coverage 100% reliable ?

No, it just a quantative metric. Having 100% coverage does not guarantee absence of errors in the code.

### What are the metrics

*How many metrics are out there:* a lot. *How many metrics do we need to care about:* a very few.

1. Statement (~ how many lines are covered)
2. Branch (~ which branches are covered)
4. Loop (to test it is needed: no loop, 1 loop, more than 1 loop)
5. MC/DC - modified conditions / decision = branch + conditions gets all possible values + every condition independently affects the result
	This metric is used in critical software. It might show that there are conditions which have no effect on the results and thus there is no understanding what is going on in the code.
6. Path coverage
```
def foo(a, b):
	if a:
		do_a()
	if b:
		do_b()
	return do_something()
```
In the example above there are 4 paths (2^2). For complex statements the number of paths will be much greater.
7. Boundary value - testing on a boundary of some value, e.g test negative and positive value.
8. Synchronization coverage - to make sure that code is locked (mutex was set, etc) in concurent access
3. ...

### When Coverage does not work

If we depend on 3d party code (OS I/O) it is better to test with specification in mind, rather than use automatic metrics (like branch coverage). *Fail injection* might help to test software behavior, to simulate I/O errors etc.

### What does it mean if code is not covered

1. **Infeasible code** - the code that cannot be executed.
	It is not always a bad thing, e.g. code is good and can reach *Infeasible* part **only** if we made a mistake somewhere. It is possible to tell coverage tool to ignore infeasible code.
2. Code not worth covering
	Such code is simple but can be *very* hard to trigger. If we need to test this - it is better to use *fail injection* technique.
3. Inadequate test suite
	Either test code should be improved to achive more coverage, or it can be left at is is since we don't need to get 100% coverage.
	
### Automated whitebox testing

There are tools that allows automaticaly generate test inputs to get good *path coverage*.
	
## Lesson 5 - Random testing

It is a way to build test cases based on random input. *Random data generator* produces input (and tests) for code, the tests is being executed, then results passes to *oracle*. The oracle decides if tests ok and logs its results.

### Input validity

General problem for random testing - generating valid inputs. It is needed to keep in mind specification. Instead of pure random input, better to contain random data in some sort of predefined range. E.g. for web browser testing, just random data can be used, but the tests must also use random html generator to test parsing/rendering/js exection, in order to achive *great coverage*.