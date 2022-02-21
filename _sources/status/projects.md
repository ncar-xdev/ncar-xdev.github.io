# Short-Term Projects

We are currently working on [xWRF](https://github.com/ncar-xdev/xwrf), a prototype of an
Pangeo-friendly analysis plug-in for Xarray.  This prototypical effort is exploring how
functionality that currently exists in the
[wrf-python](https://wrf-python.readthedocs.io/en/latest/) package can be implemented in
a way that is compatible with the Pangeo stack.

We are also in the process of completing *Project Funnel*, which developed a caching and
workflow automation framework for climate and weather analysis based on
[Prefect](https://www.prefect.io/).  As part of this project, we developed the
[xpersist](https://xpersist.readthedocs.io/en/latest/) package for caching steps in
the workflow that return Xarray objects.

## Selecting Future Projects

Our current mechanism for selecting short-term projects for Xdev’s effort is
internal.  We have assessed the pain points that the community has based on Q/
A through either our Zulip platform or through our weekly Office Hours and
based on direct interactions with scientists.  A record of questions asked in
the Xdev Office Hours is made, and Zulip records are held indefinitely.  We
collaborate with individuals who reach out to us individually.

Moving forward, however, we believe that we need to adopt a more equitable
approach to assessing the most important activities for Xdev and what
activities will have the greatest impact.  With that in mind, it is my belief
that we should begin conducting surveys of the community to ask them
specifically for their pain points and their thoughts on what we should be
working on.  As more of the community adopts Pangeo technology and Python, we
expect that a formal project proposal process can be created, whereby
individuals or groups with a desire for software engineering experience in the
Python realm can reach out for help on specific problems.  In this capacity,
Xdev could select proposals that can be generalized to impact a broader range
of users than just the proposing scientists.  Through this process, we believe
that Xdev can have a strong impact on changing best practices and the
development of scientific software.
