# git bisect

A very very simple example of how to track down a bug using git bisect

## Setup

```
pip install virutalenv
virutalenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run tests and see that it's broken

```
nosetests
```

or run tests on any file change

```
sniffer
```

## Using git bisect

```
# Start git bisect
git bisect start

# Mark current commit a bad
git bisect bad

# Go back to a commit we know was working and mark as good
git checkout 6a6b8bec14e88d5cf760effade04b55fb95055db
git bisect good
>> Bisecting: 0 revisions left to test after this (roughly 1 step)
>> [fd9747757bf21f617abc508d8e9f6c15fdb6343d] Add further test cases

# Notice how git automatically checks out another commit
# This commit is between the good and bad commits

# Continue to mark selected commits as good or bad
# until git find the "first bad commit"!

git bisect bad
>> Bisecting: 0 revisions left to test after this (roughly 0 steps)
>> [ee41c4fe88f8571a3771ca2ba713f0093431899c] Adds futher test cases and implements solution

git bisect good
fd9747757bf21f617abc508d8e9f6c15fdb6343d is the first bad commit
commit fd9747757bf21f617abc508d8e9f6c15fdb6343d
Author: Tom Marks <thomas.marks@gmail.com>
Date:   Sun Aug 13 10:00:24 2017 -0400

    Add further test cases

# We found the bad commit, lets end the git bisect process
git bisect reset
```

We know know the commit with sha-1 hash `fd9747757bf21f617abc508d8e9f6c15fdb6343d` introduced the bug.


# Futher examples

The following [You Tube Video](https://www.youtube.com/watch?v=P3ZR_s3NFvM) shows how git bisect can be used to track down bugs during web development.
