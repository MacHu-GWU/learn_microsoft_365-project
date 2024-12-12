# -*- coding: utf-8 -*-

from learn_microsoft_365 import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_microsoft_365.tests import run_cov_test

    run_cov_test(__file__, "learn_microsoft_365.api", preview=False)
