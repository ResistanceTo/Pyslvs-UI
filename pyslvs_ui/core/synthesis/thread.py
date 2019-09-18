# -*- coding: utf-8 -*-

"""Thread of synthesis process."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from abc import abstractmethod
from pyslvs_ui.core.QtModules import (
    Slot,
    QABCMeta,
    QThread,
    QWidget,
    QMutex,
)


class BaseThread(QThread, metaclass=QABCMeta):

    """Base thread of Cython functions."""

    @abstractmethod
    def __init__(self, parent: QWidget) -> None:
        super(BaseThread, self).__init__(parent)
        self.finished.connect(self.deleteLater)
        self.is_stop = False
        self.mutex = QMutex()

    @Slot()
    def stop(self) -> None:
        """Stop the algorithm."""
        self.mutex.unlock()
        self.is_stop = True
        self.mutex.lock()