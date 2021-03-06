"""Easily create cross-platform desktop applications with PyQt

See:
https://github.com/mherrmann/fbs
"""

from glob import glob
from os.path import relpath, join, isdir

from setuptools import setup, find_packages

def _get_package_data(pkg_dir, data_subdir):
    glob_parts = pkg_dir.split('/') + [data_subdir, '**', '*']
    glob_pattern = join(*glob_parts)
    return [
        relpath(file_path, pkg_dir)
        for file_path in glob(glob_pattern, recursive=True)
        # Exclude directories to avoid errors when installing via pip on Ubuntu:
        if not isdir(file_path)
    ]

description = 'Easily create cross-platform desktop applications with PyQt'
setup(
    name='fbs',
    version='0.1.0-SNAPSHOT',
    description=description,
    long_description=
        description + '\n\nHome page: https://github.com/mherrmann/fbs',
    author='Michael Herrmann',
    author_email='michael+removethisifyouarehuman@herrmann.io',
    url='https://github.com/mherrmann/fbs',
    packages=find_packages(),
    package_data={
        'fbs': _get_package_data('fbs', 'default_settings'),
        'fbs.installer.mac': _get_package_data(
            'fbs/installer/mac', 'yoursway-create-dmg'
        ),
        'fbs.installer.windows': ['Setup.nsi']
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
    
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    
        'Operating System :: OS Independent',
    
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='GPLv3 or later',
    keywords='PyQt',
    platforms=['MacOS', 'Windows', 'Debian']
)