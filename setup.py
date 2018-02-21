"""
SATySFi formatter for pygments
"""

from setuptools import setup

entry_points = """
[pygments.formatters]
satysfi = satysfi:SatysfiFormatter
"""

setup(
    name         = 'pygments.formatters.satysfi',
    version      = '0.1',
    description  = __doc__,
    packages     = ['satysfi'],
    entry_points = entry_points
)
