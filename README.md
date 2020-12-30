# Streak

Create github or gitlab streaks with this simple script.


## Install

```bash
$ pip install python-streak
```


## Usage

After installing streak, simply create an new git repository and run streak:

```bash
$ git init
$ streak
```

Now push this repository to github or gitlab et voià!

By default streak will create 3 commits per day with a probability of ~71% per
commit for 100 years, starting from 1980-05-09. These parameters can be tuned
with:

* `--start START`: Beginning of the commits (Format: YYYY-MM-DD)
* `--end END`: End of the commits (Format: YYYY-MM-DD)
* `--max MAX`: Maximum number of commits per day.
* `--proba PROBA`: Probability for a commit to happen.
