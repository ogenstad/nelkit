"""Tests to validate yaml features."""
from nelkit.exceptions import FileNotFound, ParsingError
from nelkit.parsing.yaml.loader import YamlLoader
import os
import pytest
s = os.sep


def test_YamlLoader():
    """Test to see that the YamlLoader returns a dict."""
    yl = YamlLoader(filename='tests%sparsing%syaml%sdata%sbase.yml' % (s, s, s, s))
    assert isinstance(yl.data, dict)


def test_load_missing_file():
    """Test to verify that an exception is raised when trying to load a non-existing file."""
    with pytest.raises(FileNotFound) as excinfo:
        YamlLoader(filename='tests%sparsing%syaml%sdata%sfile_that_does_not_exist.yml' % (s, s, s, s))
    assert 'Unable to read: tests%sparsing%syaml%sdata%sfile_that_does_not_exist.yml' % (
        s, s, s, s) == str(excinfo.value)


def test_load_invalid_file():
    """Test to verify that an exception is raised when the yaml file is invalid."""
    with pytest.raises(ParsingError) as excinfo:
        YamlLoader(filename='tests%sparsing%syaml%sdata%sinvalid_yaml.yml' % (s, s, s, s))
    assert 'tests%sparsing%syaml%sdata%sinvalid_yaml.yml is not a valid yaml file' % (
        s, s, s, s) == str(excinfo.value)
