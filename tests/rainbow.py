#!/usr/bin/env python

from __future__ import print_function
from sansic import codes as sa


def main():
    colors = []
    for color in [attr for attr in dir(sa) if not callable(getattr(sa, attr)) and not attr.startswith("__")]:
        colors.append(getattr(sa, color))

    message = 'Things turn out to be less complicated when used'

    for index,char in enumerate(message):
        print('{}{}'.format(colors[index%len(colors)],char), end='')

    print(sa.ENDC)


if __name__ == '__main__':
    main()
