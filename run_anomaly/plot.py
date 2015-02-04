#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2015, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""
Plotting anomaly scores.
(Copied from grok-projects/tools/db_utils.py)
"""

import os
import subprocess
import sys

from plotly import plotly

from gef.utils.plotting import plotResults



def plotFile(fileName, chartTitle=None):
  """
  Plot the given results file using plot.ly and return the URL of the graph
  """
  plotlyUser = os.environ['PLOTLY_USER_NAME']
  plotlyAPIKey = os.environ['PLOTLY_API_KEY']
  py = plotly(username_or_email=plotlyUser, key=plotlyAPIKey, verbose = False)

  # Plotly now opens urls by default. Turn this off.
  py.ioff()

  thresholds = [.99, .999, .9999, .99999]
  plotURL = plotResults(py,
              fileName,
              thresholds,
              includeThresholds = True,
              includeLikelihoods = True,
              includeAnomalyScore = True,
              includeLabels = False,
              jeffPlots = False,
              largePlots = False,
              verbosity=0,
              chartTitle=chartTitle)


  if sys.platform == 'darwin':
    cmd = "open " + plotURL
    subprocess.call(cmd, shell=True)
  return plotURL



if __name__ == "__main__":
  fileName = sys.argv[1]
  url = plotFile(fileName, chartTitle=fileName)
  print "URL is %s" % (url)
