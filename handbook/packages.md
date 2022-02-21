# Xdev Packages

As a result of our work, it is common for Xdev to create stand-alone packages for
general use.  Some of these packages can be found on the
[Package Metrics](../status/packages) page.  So that we can better maintain
these packages, we employ as much automation as possible.  Thus, any new package
is expected to employ the following services to ensure enough automation that we
can continue to minimally maintain our past work.  The following services are
commonly deployed on all of our packages.

## Automatic Versioning

To make versioning of our packages easy and consistent, **all GitHub packages
should enable something like [`setuptools-scm`](https://github.com/pypa/setuptools_scm/)**
to make versioning of the software consistent with git tag names.

## Package Services

Below are some of the services that we expect you to use to aid in our
package publication and maintenance.

### PyPI

All of our installable packages are expected to be published on
[PyPI](https://pypi.org).  **The GitHub PyPI Publish Action
[`pypa/gh-action-pypi-publish`](https://github.com/marketplace/actions/pypi-publish)
should be deployed on all GitHub repositories** to ensure that every GitHub release
triggers the publication of a new version of the software on PyPI.

### Conda-Forge

While PyPI publication is required, **we also highly recommend publishing the same
package on Conda Forge.**  You can use the
[`grayskull`](https://github.com/marcelotrevisani/grayskull) package to easily
create a new Conda Forge recipe for you.  Once the first conda-forge *feedstock*
has been created and accepted on Conda Forge, it will automatically publish
new versions of the package on Conda Forge when new versions have been published
on PyPI.

### Read the Docs

We routinely use the [Read the Docs](https://readthedocs.org) service to publish
our package documentation.  **All packages should publish documentation that is
complete and useful,** and we recommend RTD for that purpose.

## Package Ownership

In addition to the package repository on GitHub, it is important that **all members
of the Xdev Team have administrative ownership of each package service account.**
That is, ownership of the Read the Docs project for a given package should be
shared by all members of the team, not be a sole individual.
