# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = ["test_normal_de", "test_uniform_de"]

from ... import proposals
from .test_proposal import _test_normal, _test_uniform


def test_normal_de(**kwargs):
    _test_normal(proposals.DEProposal(1e-2), **kwargs)


def test_uniform_de(**kwargs):
    _test_uniform(proposals.DEProposal(1e-2), **kwargs)
