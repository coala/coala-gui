#!/usr/bin/env python2

import sys
import os
import signal
import time
import dogtail
from dogtail.utils import run
from dogtail.config import config
from dogtail.procedural import focus, click
import unittest


class WindowTest(unittest.TestCase):
    def setUp(self):
        config.logDebugToStdOut = True
        config.logDebugToFile = False
        # Next line may take some time to run - about 40 sec.
        self.pid = run('./coala-gui')
        self.app = dogtail.tree.root.application('coala-gui')

    def test_focus_app(self):
        focus.application.node = None
        focus.application('coala-gui')
        self.assertEquals(focus.application.node, self.app)

    def tearDown(self):
        os.kill(self.pid, signal.SIGKILL)
        # Sleep just enough to let the app actually die.
        # AT-SPI doesn't like being given things too fast.
        print("Tearing down ...")
        time.sleep(0.5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
