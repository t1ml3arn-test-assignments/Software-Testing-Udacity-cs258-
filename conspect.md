## Lesson 1

The goal of testing not just in finding bugs, but in funding bugs as early as possible.

### Testing in general

We take some input data, pass it to SUT(software under test) and examine results. If the results is not acceptable then we found a bug.

Where bugs can be found:

1. In the *software under test* (SUT)
2. In the *test* itself
3. In the *software specification*
4. In the *operating system*
5. In the *hardware*

>Passed tests do not mean that there are no bugs in SUT !

### Input data

First, it is not possible to test all the inputs (*input domain* - all the possible inputs). Therefore, second, it is hard to choose good inputs. 

### Assertions

Assertion is check that a property is `True`. Assertions are not errors/exceptions, they are not meant for handling, but rather they indicate that execution went wrong. Assertions should be used to check if something wrong in the logic of a programm instead of checking wrong user's input.

### Specificaton

Software operates under some specs. What should return `sqrt(9)` ? 3 or -3 ? In general - either or both answers are correct. But in actual code it should be strictly defined what is being returned from `sqrt()` - positive or negative. 

### Fault injection

We need to test how our soft responds on low-level OS/API errors, but we often cannot force those api calls to generate wrong behavior easily. What we should instead? The answer is - **fault injection** technique. So we build our test case in such a manner when we can generate some errors which we are interesting in.

```py
def faulty_open(path, mode):
	if math.rand() < 0.2:
		return SOME_ERROR
	else:
		return normal_open(path, mode)
```

As you see above, sometimes `faulty_open` generates an error. Later in some stress tests we can examine how SUT works when that errors happen. I general, such faults should not be forced to occur often.

### Types of testing

- White-box testing

	In this scenario we can see source code of SUT, or more general - we can examine the details of the system.

- Black-box testing

	It is not possible to get details about the system internals in this scenario. Tests based on specification or only on assumptions how the system works.

- Unit testing

	In this scenario - *separate modules* (or units) is being tested independently. Units use wide range of data from input domain and also use mock objects which simulate the behavior of the larger software to which this unit belongs.

- Integrations testing

	This tests the modules (which has already been unit tested) in *combinations* with each other, i.e. *interfaces* between modules.

- System testing

	The purpose of this kind - find if a system does what it should do as a *whole*. At this level we more concerned how the system will be used, how it works with important inputs (or use cases)

- Differential testing

	Here we compare the results of two different implementations. It might be completely different software or one of the system under test might be just an old version of the same software.

- Stress testing

	The system is tested beyond(or near) its normal usage limits. Examples:

	- huge number of requests to the *webserver*
	- creation of large files or allocation of large memory block for *operationg system*

	Stress testing is needed for reliability.

- Random testing

	The tests generate random input data and observe how the system responds for such input. The input can be just random bytes or some specialy constructed data structures.

**Some hints to hold in mind when do testing**

- do not want code to succeed, want it to fail
- do not ignore weird things

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

If we depend on 3d party code (OS I/O) it is better to test with specification in mind, rather than use automatic metrics (like branch coverage). *fault injection* might help to test software behavior, to simulate I/O errors etc.

### What does it mean if code is not covered

1. **Infeasible code** - the code that cannot be executed.
	It is not always a bad thing, e.g. code is good and can reach *Infeasible* part **only** if we made a mistake somewhere. It is possible to tell coverage tool to ignore infeasible code.
2. Code not worth covering
	Such code is simple but can be *very* hard to trigger. If we need to test this - it is better to use *fault injection* technique.
3. Inadequate test suite
	Either test code should be improved to achive more coverage, or it can be left at is is since we don't need to get 100% coverage.
	
### Automated whitebox testing

There are tools that allows automaticaly generate test inputs to get good *path coverage*.
	
## Lesson 5 - Random testing

It is a way to build test cases based on random input. *Random data generator* produces input (and tests) for code, the tests is being executed, then results passes to *oracle*. The oracle decides if tests ok and logs its results.

### Input validity

General problem for random testing - generating valid inputs. It is needed to keep in mind specification. Instead of pure random input, better to contain random data in some sort of predefined range. E.g. for web browser testing, just random data can be used, but the tests must also use random html generator to test parsing/rendering/js exection, in order to achive *great coverage*.

### Problems with random testing

There is possible that among all generated random inputs most of them cover only small part of code. I.e. most of the inputs are invalid and will be rejected by software on the early stage. There is possible also, that invalid inputs are not being rejected by the sotware and crash test suit. So there should be input validation, but it is not always possible.

### Structures input

Again, this is related to good and valid inputs. So, to test some API in random maner, we want not just random calls to its functions, but rather correct structured calls. Some function should be call only after another one (some action depends on other actions). Otherwise, we get useless (or even invalid) inputs, which we don't want. For example, in file system testing, *writing* or *readind* a file can be done only if the file has been *opened*. So some sequence of API's calls should be maintened.

### Generating random inputs

RIG basicaly consists of random-number generator and specification. E.g. credit card number generator takes some random input (card prefix) and generates other digits with Luhn' algo (specification). This kind of testing is calling **Generative random testing**. There is another way of random testing which is calling **Mutation-based random testing**. In this technique, a random mutations is applied to non-random generated input data. 

Kind of mutations which can be applied:

1. Random bits twisting. 
	Some random part of input data can be modified, e.g. writing random bytes at random addresses of pdf file.
2. Field modification.
	This involves specifications. Mutation applied not randomly, but to specifiec fields of structured data.
	E.g. mutations applied to fields of HTTP request

### Oracles

Oracle decides if a random test passes or not. It is the most important part of random testing.

Possible types of oracles:

1. **Weak oracles**
	Such oracles are most useful in practice, but they offer generic properties to test
	- application crash detection
	- application timeout detection
	- language rule violation (e.g. access an array element out of array bounds)
2. **Medium oracles**
	- assertion checks that put into programms by programmer. These checks are more application specifiec than checks in weak oracles
3. **Strong oracles**
	- alternative implementation of the same specification
		- small code, written for the concrete tests
		- different version of software under test, i.e. previous version or even more old;
		- completely different software that implements the same spec
	- function inverse pairs
		Pseudocode example `D -> foo() -> D* -> foo_inv() -> D`. We have a function and its invers so some input passed in `foo()` then result of it is passed to `inv()` and this result must be the same as the initial one. E.g. `write/read` for files, `push/pop` for arrays, `ecrypt/decrypt`. However it is not always possible to get good results from that. It will be harder to use such oracles for media encoding/decoding like JPEG.
	- null test transformation
		We take input and transform it in such a way, that it should not affect the results. E.g. `return a + b` can be transformed into `return -(-a) + (-(-b))`