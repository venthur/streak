#!/usr/bin/env python3

import argparse
import datetime
import random
import subprocess


TIMES = [datetime.time(h, m, s)
         for h in range(0, 24)
         for m in range(0, 60)
         for s in range(0, 60)]


def date(s):
    year, month, day = s.split('-')
    return datetime.date(int(year), int(month), int(day))


def main():
    args = parse_args()

    for i in daterange(args.start, args.end):
        times = []
        for j in range(args.max):
            if random.random() < args.proba:
                times.append(random.choice(TIMES))
        times = sorted(times)
        for t in times:
            # our timestamp
            ts = datetime.datetime.combine(i, t)
            commit(ts)


def commit(timestamp):
    cmd = f"GIT_AUTHOR_DATE='{timestamp}' GIT_COMMITTER_DATE='{timestamp}' git commit --allow-empty -m '{timestamp}'"
    subprocess.run(cmd, shell=True)


def daterange(start, end):
    for i in range((end - start).days):
        yield start + datetime.timedelta(i)


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
            '--start',
            type=date,
            default='1980-05-09',
            help="Beginning of the commits (Format: YYYY-MM-DD)",
    )

    parser.add_argument(
            '--end',
            type=date,
            default='2080-05-09',
            help="End of the commits (Format: YYYY-MM-DD)",
    )

    parser.add_argument(
            '--max',
            type=int,
            default=3,
            help="Maximum number of commits per day."
    )

    parser.add_argument(
            '--proba',
            type=float,
            default=5/7,
            help="Probability for a commit to happen."
    )

    return parser.parse_args()


if __name__ == '__main__':
    main()
