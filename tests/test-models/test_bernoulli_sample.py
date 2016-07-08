from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from edward.models import Bernoulli
from edward.util import get_dims

sess = tf.Session()


def _test(shape, p, size):
    x = Bernoulli(shape, p)
    val_est = tuple(get_dims(x.sample(size=size)))
    val_true = (size, ) + shape
    assert val_est == val_true


def test_scalar():
    _test((), 0.5, 1)
    _test((), np.array(0.5), 1)
    _test((), tf.constant(0.5), 1)


def test_1d():
    _test((1, ), np.array([0.5]), 1)
    _test((1, ), np.array([0.5]), 5)
    _test((2, ), np.array([0.2, 0.8]), 1)
    _test((2, ), np.array([0.2, 0.8]), 10)
    _test((1, ), tf.constant([0.5]), 1)
    _test((1, ), tf.constant([0.5]), 5)
    _test((2, ), tf.constant([0.2, 0.8]), 1)
    _test((2, ), tf.constant([0.2, 0.8]), 10)


#def test_2d():
#    _test((1, 1), np.array([[0.5]]), 1)
#    _test((1, 1), np.array([[0.5]]), 5)
#    _test((1, 2), np.array([[0.2, 0.8]]), 1)
#    _test((1, 2), np.array([[0.2, 0.8]]), 10)
#    _test((2, 2), np.array([[0.2, 0.8], [0.7, 0.6]]), 1)
#    _test((2, 2), np.array([[0.2, 0.8], [0.7, 0.6]]), 10)
