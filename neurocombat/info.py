__version__ = '0.1.0a'

NAME = 'neuroCombat'
MAINTAINER = 'Nicholas Cullen'
EMAIL = ''
VERSION = __version__
LICENSE = 'MIT'
DESCRIPTION = ('A toolbox for correcting batch effects in neuroimaging (or '
               'microarray) data using the ComBat algorithm.')
LONG_DESCRIPTION = ('')
URL = 'http://github.com/ncullen93'
DOWNLOAD_URL = ('https://github.com/ncullen93/{name}/archive/{ver}.tar.gz'
                .format(name=NAME, ver=__version__))

INSTALL_REQUIRES = [
    'numpy',
    'pandas'
]

TESTS_REQUIRE = [
]

EXTRAS_REQUIRE = {
}

PACKAGE_DATA = {
}
