import sys
from importlib.metadata import Distribution, DistributionFinder
from pathlib import Path


class UninstalledDistributionFinder(DistributionFinder):
    """Find lazr.uri's metadata despite it not being installed."""

    @staticmethod
    def find_spec(fullname, path=None, target=None):
        return None

    @staticmethod
    def find_module(fullname, path):
        return None

    @staticmethod
    def invalidate_caches():
        pass

    @staticmethod
    def find_distributions(context=DistributionFinder.Context()):
        if context.name == "lazr.uri":
            return [Distribution.at(Path(__file__).parent / "lazr" / "uri")]


sys.meta_path.append(UninstalledDistributionFinder)
