from setuptools import setup, find_packages


requires = [
    'pyramid',
    'waitress',
    'pyramid_debugtoolbar',
    ]

setup(name='longstocking',
      version='0.0',
      description='longstocking',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      namespace_packages = ['ilogue'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="ilogue.longstocking",
      entry_points = """\
      [paste.app_factory]
      main = ilogue.longstocking:main
      """,
      )

