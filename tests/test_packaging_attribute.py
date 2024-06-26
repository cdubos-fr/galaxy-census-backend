import pytest

from .utils import is_canonical_version


class TestPackagingAttribute:
    @pytest.mark.unit
    def test_version_respect_pep440(self):
        from galaxy_census_backend import __version__

        assert isinstance(__version__, str)
        assert is_canonical_version(__version__)

    @pytest.mark.unit
    def test_package_description(self):
        from galaxy_census_backend import __doc__

        assert isinstance(__doc__, str)
        assert len(__doc__) > 0
