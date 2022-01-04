# The Experimental Development Team (Xdev)

The Experimental Development Team (Xdev) was born out of Pangeo.  Matthew Long
(CGD) and I felt that Pangeo was a movement that NCAR needed to join.  Not
only does Pangeo offer a roadmap for interactive "Big Data" analysis for
climate and weather scientists, but it demonstrates a revolutionary culture of
collaboration between scientists and software engineers spanning both academia
and industry.  Pangeo realizes the dream of open source software and open
development that so many people evangelize but so few obtain.  But to realize
this dream at NCAR, we need to do more than just _use_ Pangeo Environments.
We need to do more than just teach scientists how to use Xarray and Dask and
Jupyter, or program in Python, or even develop an NCL replacement in Python
that leverages the Pangeo stack.

_NCAR needs to change how its scientists and software engineers relate to one another, and how technology for data science and analysis at NCAR is developed openly._

Xdev was created to be the catalyst for this cultural change at NCAR, not just
by teaching Python but by working with scientists in direct collaboration on
software, and therefore teaching open development by example.

To achieve this, Xdev acts as navigators for NCAR scientists in the Pangeo
sea.  As such, Xdev helps NCAR scientists adopt a common approach to enabling
broad multidisciplinary collaboration through its education and development
efforts.  Xdev’s _education_ efforts to teach scientists at NCAR (and beyond)
Python and the Pangeo stack help build and strengthen the Pangeo community of
technology _users_.   Meanwhile, Xdev’s _development_ efforts to collaborate
with scientists on Pangeo technology development help teach open development
and open source software best practices through example.


## The Xdev Manifesto

Matt and I also recognized that Xdev needs to be something more than just
"Pangeo at NCAR."  Xdev needs to be a voice in the Pangeo community for NCAR’s
unique needs, and not just a bullhorn for Pangeo’s interests within NCAR.
Thus, it behoves us to enumerate our _technical values_ to highlight how
Xdev’s values align with Pangeo.

1. We value **interactivity** over batch processing.  While batch processing
   is still necessary for many things, we believe that the need for
   curiosity-driven analysis is greater and that this should be the priority.

2. We value **open source** over closed source solutions.  While some closed
   source solutions may be better for specific needs, especially if a monetary
   investment has already been made, we believe that open source solutions are
   a better long term solution in general.

3. We value **scalability**.  While serial, non-scalable solutions can be
   reasonable algorithm prototypes, they are of limited value in the era of
   Big Data.  We believe that scalability should be considered at all times.

4. We value workflow **portability**.  While having solutions that only work
   on NCAR systems can solve immediate problems, we want to reduce the burden
   on scientists for having to learn different solutions on different
   platforms, whether they be HPC or cloud.  Scientists should decide where to
   do their analysis based on where the data is hosted, not based on where
   they can run the specific code they want to run.

5. We value **transparency** over opacity.  While some work for many reasons
   cannot be made public, we choose to do all of our work in the open so that
   others can learn from us, leverage our work, and work with us at any time.

6. We value **reproducibility**.  While static, non-reproducible scientific
   communication still has value as the traditional mechanism for exchanging
   knowledge throughout scientific disciplines, we believe reproducible
   mechanisms for publishing and sharing scientific knowledge are more
   important and effective.

By affirming these values, we focus most of our interest on the Pangeo stack that is supported by Xarray, Dask, and Jupyter, as these technologies provide an exceptional foundation for building a replete ecosystem to support scalable analytics.

:::{admonition} A note on reproducibility
From Xdev’s perspective, reproducibility is primarily an issue of scientific
reproducibility, and not (for example) _bit-for-bit reproducibility_. From our
perspective, reproducibility is all about making sure that research, analysis,
and results can actually be reproduced by the people with whom scientific
results are shared.  This is why we encourage Jupyter Notebooks.  Jupyter
Notebooks are the basis for an "executable paper."  A number of entities are
already looking into peer-reviewed notebook publication journals, and the
future of notebooks as the mechanism for reproducible publications is very
promising.  There are, however, technical challenges to making Jupyter
Notebooks truly reproducible, even in a scientific sense.  A Jupyter Notebook
file (i.e., a file with the `.ipynb` extension) will not run properly (or even
at all) without the correct environment (or _kernel_) available in which the
notebook code will run.  If the notebook requires special packages to run
without error, then these packages need to be installed for every user who
wants to execute that notebook.  Containerization is one solution to this
problem, where notebooks are shared with the necessary environment in which
they can run.  This is the mechanism behind the Jupyter Project’s
[Binder](https://mybinder.org) utility.  Binder works by sharing notebooks via
publicly accessible Git repositories inside which are files defining the
environment (and how to build the environment) needed by the notebooks.  A
BinderHub server then can be used to retrieve the notebooks and the
environment definitions to build a container image from which the notebooks
can be run on the cloud.
:::


## Mission & Vision

**Xdev’s mission is to advance open reproducible science through interactive Big Data analysis.**

In five years, we envision a community of scientists at NCAR and beyond
working together to develop and maintain scientific workflows and sharable
software to support those workflows on a platform where these workflows can be
efficiently developed in collaboration and executed.  We envision these
workflows to be reproducible, using Jupyter Notebooks with fixed versioning
and environments (e.g., using containerization).  We envision a core group of
scientists within that community who have helped develop and support the
technology that makes much of this possible, who follow modern engineering
best practices and who leverage each other’s technology to quickly and
efficiently develop new capabilities and new workflows, as well as help other
scientists learn these skills and knowledge themselves.  We envision all of
this technology supporting and empowering not only NCAR staff but the entire
community that NCAR supports.

As part of this vision, we also see Jupyter Notebooks becoming first-class
citizens on HPC systems.  In this vision, we see a different style of
"analysis and visualization cluster," one with computation occurring on HPC
hardware _or_ cloud hardware, with data held on the "edge" of the cloud,
instead of copies of the data in multiple locations.  We see HPC job
scheduling becoming flexible and elastic, instead of only accommodating static
job loads more suited for large model runs.  We see containerization becoming
the norm, not just to provide a pre-defined system environment for software to
run, but to allow user-defined "services" on the HPC system, making it
possible for scientists to share interactive analyses, instead of just static
notebooks.  We see a blurring of the difference between HPC and cloud
computing, and in time we expect very little difference between the two at all.

As the community of scientists who use this style of analysis, and who
contribute back to the software that makes this analysis possible, develops
and grows, we envision Xdev’s contributions will slowly shift toward more
specific engineering efforts that optimize, stabilize, and strengthen the
ecosystem of technologies used by the scientific community.  However, we
envision Xdev still remaining a resource for scientists on all engineering
matters, especially on matters that extend beyond the role that scientists
nominally play.  Xdev will continue to remain a resource of software
engineering knowledge and expertise for the community.


### Xdev & ESDS

The [Earth System Data Science](https://ncar.github.io/esds/) initiative was
created to motivate scientists to build community around using technology for
open reproducible science:

:::{margin}
Read more about the [ESDS Vision](https://ncar.github.io/esds/about/#about-us)!
:::

> The Earth System Data Science initiative aims to profoundly increase the
> effectiveness of the NCAR/UCAR workforce by promoting deeper collaboration
> centered on analytics, improving our capacity to deliver impactful,
> actionable, reproducible science and serve the university community by
> transforming how geoscientists synthesize and extract information from
> large, diverse data sets

ESDS is the force bringing the scientific community together to collaborate,
and Xdev is the catalyst for cultural change.  ESDS has an essentially
scientific focus, while Xdev has an engineering focus.  Xdev brings its
expertise to bear on specific problems that scientists have with the
technology.  Xdev helps steer ESDS scientists toward solutions that
interoperate within Pangeo Environments and helps the scientists build and
depend upon a common stack of software that empowers everyone.  Xdev helps
teach ESDS scientists through ESDS’s training efforts and through direct
collaboration with ESDS scientists on technical projects.  While Xdev means to
address more than just the ESDS community of scientists, ESDS is a strong
partner with Xdev and an excellent source for collaboration.


## Structure

Xdev is currently a _matrixed_ team made of 3 full-time software engineers
with funding from both CISL and CGD.  Two of the software engineers (Anderson
Banihirwe and Julia Kent) report directly to Kevin Paul, and one (Max Grover)
reports directly to Matt Long.  Like all matrixed teams, maintaining a clear
vision of the team’s purpose and objectives across all of the team members’
supervisors is critical.

Xdev also relies closely on a group of 8 software engineers across UCAR who
act as stakeholders in Xdev’s activities.  These software engineers
occasionally provide part-time development support on activities that directly
impact their own work and feedback on and direction for Xdev’s activities,
including assistance with short-term project selection, testing, and feedback,
as well as tutorial input and guidance (see [Governance](#governance)).
Most of these software engineers are also members of ESDS, but some simply
represent Python expertise across UCAR and help expand and shape Xdev’s vision.

Within the core team, there are definite roles and responsibilities.

Kevin Paul is the Team Lead, and helps define and scope development projects
and education/training activities.  The Team Lead seeks out and builds
relationships with stakeholders across UCAR.  In all of our efforts, we hope
that target users will provide direct feedback to our efforts in a tight,
agile iterative cycle, but we acknowledge that this cannot always be expected
of scientists who are not working with the team on a regular basis.  When
decisions are required to keep progress moving forward, the Team Lead acts as
a proxy for the user when the user is not available to provide feedback,
providing functional specifications for Xdev activities from the target user
perspective.

Anderson Banihirwe is the Technical Lead and helps assess the right technology
to use on Xdev projects and activities.  The Technical Lead is responsible for
maintaining a current view of the relevant technology and assessing how
processes need to change based on changing technological capabilities.

Julia Kent is the Training Lead and helps organize and maintain our tutorials
and training materials, working closely with ESDS and Project Pythia.  The
Training Lead is responsible for keeping our educational and training mission
constantly moving forward and building the knowledge base of the scientific
community.

Max Grover is the ESDS Coordinator.  The ESDS Coordinator acts as the liaison
between ESDS and Xdev and helps interface the Xdev Team with ESDS activities.
Max organizes much of the ESDS activities as well as acting as a core
developer for Xdev.

These roles have developed over time out of necessity and the people who have
stepped into these roles have done so voluntarily as our activities have
progressed.  These roles are not set in stone, and we expect them to shift and
evolve as the team moves forward.


## Governance

The Xdev Team is governed by its stakeholders.  In particular, there are three
categories of stakeholders that govern Xdev’s activities:

1. **Member Stakeholders:** Member stakeholders are part-time members of the
   Xdev Team. Member stakeholders are typically software engineers or
   scientists with a dedicated software engineering background and role and
   can provide detailed technical input on projects and other technical
   activities.

2. **Community Stakeholders:** Community Stakeholders consist of the broader
   user community, including scientists who have adopted, or are adopting, the
   Python language for scientific data analysis. Community Stakeholders are
   the experts in how Xdev’s education and technical project work should be
   directed, as they are the target demographic.

3. **Leadership Stakeholders:** Leadership Stakeholders include the Xdev Team
   Lead, the supervisors of the Xdev Members, and other leadership-level
   stakeholders in the success of Xdev and Xdev’s efforts.  Leadership
   Stakeholders are responsible for a broader swath of activities within NCAR
   and the wider community and therefore are capable of directing
   collaborations between Xdev and other groups.

While Xdev activities continue, Member Stakeholders provide monthly feedback
through the Monthly Xdev Stakeholder meeting.  Being technical experts in
their own right, Member Stakeholders are capable of being collaborators on
Xdev Projects, even if they do not have the time to dedicate to project work
themselves.  We call them Member Stakeholders because we consider them Xdev
members, and they are included in all Xdev group communications (e.g., in the
`#xdev` Zulip group, on the [xdev@ucar.edu](mailto:xdev@ucar.edu) mailing
list, etc.).  Hence, Member Stakeholders are capable of staying up-to-date
with Xdev activities and providing technical feedback and guidance on a
frequent basis.

Community Stakeholders are the target demographic for all Xdev activities.
Therefore, Community Stakeholders are the owners of "the problem" that Xdev is
trying to solve through its activities.  Community Stakeholders know better
than anyone else what problems they are experiencing, what they want to learn,
and what they would like to accomplish scientifically via the technology that
Xdev develops.  Hence, Community Stakeholders have the ability to prioritize
future Xdev work, propose Xdev Projects, and act as testers and the first line
of feedback for Xdev results.  Community Stakeholders can provide their
feedback to Xdev through quarterly "Pain Point Surveys" and through a formal
Xdev Project Proposal process.  A list of future projects will be displayed on
the Xdev website and users will be able to "upvote" projects on the list.

Leadership Stakeholders represent the institutional and community leadership,
and therefore have both input on Xdev Project priorities and Xdev direction,
just as Community Stakeholders do.  However, Leadership Stakeholders also
provide input on the workings and processes of Xdev and help address
functional deficiencies, such as addressing skill gaps, assisting in grant
applications, aligning Xdev activities with the institutional mission,
assisting with extending Xdev across the UCAR organization and beyond.
Leadership Stakeholders will meet on a quarterly, triannually, or biannually
frequency, to be determined, at the Monthly Stakeholder Meeting.


## Activities

Xdev is involved in two main activities: training and development.  Xdev’s
training activities center mostly around tutorials and hackathons, organized
and held in collaboration with [Project Pythia](https://projectpythia.org) and
[ESDS](https://ncar.github.io/esds).  Xdev’s development activities are
centered on short-term projects, one-off prototypes, and center-wide service
support.  These development activities focus mostly on usability issues,
rather than performance enhancements, since much of the Pangeo stack is still,
in our opinion, mostly skeletal.  Much of the necessary functionality is there
in the Pangeo stack, but the ease with which many scientific workflows can be
constructed is lacking.  There are usability pain points that we believe need
to be addressed before too much focus can be spent on optimization and
performance, though we recognize that some focus on performance is necessary
to assure that developed solutions are scalable or "efficient enough."


### Education & Training

Xdev’s premier product addressing education and training is the Python
Tutorial Seminar Series, a bi-weekly one-hour seminar series occurring on the
second and fourth Wednesday of each month at 1PM mountain.  The series started
with a simple introduction to Python and has built up to Xarray and Dask.
Many of these tutorials and the training material that accompanies them are
being transferred to Project Pythia, with which Xdev closely collaborates.  At
the time of this writing, there have been 19 tutorials in the Python Seminar
Series, of which 7 were prepared and conducted by non-Xdev members (mostly
members from GeoCAT).

Another mechanism for training that goes beyond what can be learned simply in
the classroom is the hackathon.  The Pangeo community has held regular
hackathons at their annual meetings, and Xdev has borrowed on the Pangeo
hackathon structure.  Hackathons are an excellent way for scientists who have
learned the basics of the technology through tutorials and online material to
build upon that knowledge through projects with measurable objectives.
Hackathons are also an excellent way for scientists to learn open source
culture and open development best practices, which is the primary purpose for
Xdev.  Many of these hackathons are held in collaboration with ESDS.


### Short-Term Projects

Xdev is also planning a series of short-term projects advancing interactive
Big Data analysis by focusing on pain points in the development of scientific
analytic workflows.  We use the term analytics, here, because the entire
workflow goes well beyond simple analysis and visualization, as illustrated
very coarsely in the following figure.

:::{figure} images/pipline.svg
---
width: 600px
name: workflow-pipeline
---
A typical analysis workflow
:::

This figure also attempts to illustrate how scientific workflow development is
quite often iterative, such that the author of the workflow loops back to
previous steps in the workflow development process many times.  This means
that any inefficiencies in the workflow can be magnified many times over,
depending on how many times the step needs to be performed during the
iterative cycle.  Any of these steps can be slow and painful, and we are
working toward addressing all of these steps over the next five years using
the "squeaky wheel" approach: assess what is the most significant pain point,
prototype a solution to alleviate this pain point, repeat.  The first pain
point we are addressing relates to the issue of "checkpointing" noted in the
illustration above.

In addition to issues around workflow development, we are concerned with
reproducibility (see the [note on reproducibility](#bookmark=id.r928icz34xhu)
above).  We advocate the use of Jupyter Notebooks to aid with reproducibility,
but simple use of Notebooks is not enough to guarantee reproducible
workflows.  To ensure reproducibility, we expect to develop best practices and
underlying technology to aid with workflow reproducibility, such as best
practices on how to "fix" a Notebook environment, how to share Notebook
environments with the Notebooks themselves, and how to version workflows and
track (at least minimal) provenance of workflow components.

Xdev’s effort to catalyze cultural change at NCAR will also be a main feature
of our short-term projects.  Through direct collaboration with interested
scientists, we hope to train a core group of scientists in the engineering and
open development processes needed to help support the rest of their own
community.  Like hackathons, these projects serve as an excellent training
mechanism for scientists to learn open source culture and open development
directly through collaboration with the Xdev team. (These are the
["science-software partnerships" mentioned in the ESDS Vision](https://docs.google.com/document/u/0/d/1hwl-3QpFlR8tGrLxdxZrC9edT3CeLTG9dqy6_8KupYg/edit) document.)
The result is not only a publishable software technology but also newly
trained scientists in the maintenance and development of the technology
itself.  This is vital for healthy open source software and sustainability.
There is no single, ideal metric of the success of this goal, but we will
monitor GitHub activity from Xdev Community Stakeholders (i.e., on GitHub
repositories tied to Xdev Projects), tutorial attendance, software downloads,
GitHub "stars" and "watchers", and any other correlated metric we can divine.
All of these metrics will be displayed on the Xdev website.

As mentioned earlier, much of the scalable capabilities already exist in the
Pangeo stack, but it can be cumbersome or not obvious how to construct the
desired result efficiently or correctly.  Education and documentation can
always help address how best to use the technology, but as complex scientific
workflows are constructed we observe that many scientists are doing the same
things and should be able to leverage the same code without "cut-and-paste"
development approaches.  These projects focus on specific issues and
technologies that scientists would like for their own workflows (or the
workflows of their teams and groups) and how to generalize those technologies
for use by a broader audience.

For more details about potential future projects and what we are currently
working on, see the [Current & Future](#current-future) section below.


### One-Off Prototypes

In addition to short-term projects, the Xdev team also develops some in-house
technologies based on observations of difficulties and struggles that we
observe scientists having.  Many of these technologies are "short and sweet"
and do not necessitate any formal project, such as those described in the
short-term project above.

One such technology is
[Jupyter-Forward](https://jupyter-forward.readthedocs.io/en/latest/), which
was developed to give users the ability to launch an instance of JupyterLab on
a remote machine via SSH.  This allows users to use a specific version of
JupyterLab, instead of the one supported by any existing JupyterHub, but it
also allows users to use JupyterLab on a remote machine that doesn’t even have
a running JupyterHub at all.

Another example of an Xdev-authored in-house technology is
[Intake-ESM](https://intake-esm.readthedocs.io/en/latest/).
[Intake](https://intake.readthedocs.io/en/latest/) provides a mechanism for
translating queryable scientific vocabulary into data assets that can then be
easily loaded into analysis notebooks as Xarray Datasets.  Intake-ESM is a
plugin for Intake that makes large, cumbersome datasets of hundreds or even
thousands of Earth system model (ESM) output files easy to access and load.

These are just two examples of the short prototyping that the Xdev does, and
all of these technologies are open source and publicly available.


### Center-Wide Service Support

NCAR, and CISL in particular, provide technological services that leverage
NCAR’s computing capabilities, such as our HPC environments, the NCAR
JupyterHub, the Digital Asset Services Hub (DASH), and others.  These services
interface with a great deal of software developed by the Pangeo community and
by Xdev, at the very least because the software is run in those environments
and through those services.  Hence, Xdev is committed to helping CISL
sysadmins maintain and improve these services to create a better experience
for our users.

The following diagram shows many of the elements that comprise the Pangeo
Environment hosted by NCAR as part of our JupyterHub deployment.  The blue
boxes denote software in the Pangeo stack that is maintained and developed
primarily by the Pangeo community outside of NCAR but to which Xdev
contributes, as well.  The orange boxes represent software and services that
our JupyterHub deployment uses that are hosted by the HPC Division within
CISL.  Since these services and software require system administrator
privileges, Xdev cannot contribute to those technologies without collaboration
with HPCD.  The red box indicates software and services provided by the
Information System’s Division in CISL, another strong collaboration with Xdev,
and the green boxes represent software and technology developed by other teams
within the Technology Development Division in CISL.

:::{figure} images/stack.svg
---
width: 600px
name: Workflow
---
A diagramatic view of the Pangeo stack and how Xdev can collaborate with other
elements within CISL around these software elements
:::

We envision Xdev’s primary role within this ecosystem of software and services
as being the development and testing team tasked with improving the user
experience on the JupyterHub system through new features and capabilities.
Xdev will augment the capabilities of HPCD and ISD, as well as collaborate
with other elements of TDD, such as GeoCAT, to achieve these goals.


### Core Contributions to Pangeo Technologies

A great deal of our mission is dependent on core Pangeo technologies like
Xarray, Dask, and Jupyter.  Building third-party packages that have Xarray or
Dask as dependencies requires constantly making calls about whether certain
features should be implemented in the third-party package itself or in the
upstream dependency.  Since Xarray and Dask are open source, adding features
directly to the upstream dependency is not only possible but encouraged.  This
mode of development helps keep the core technologies, like Xarray and Dask,
healthy and as broadly applicable as possible.  Thus, it helps the development
of our own technology, which uses Xarray and Dask as dependencies, to
contribute to the core technologies ourselves.  Obviously, such contributions
should also be matched with contributions to the core technology documentation
and training materials, as necessary.

The use of these dependencies in our own software also requires that Xdev stay
aware of changes in our software’s dependencies (e.g., Xarray and Dask) so
that we can continue to ensure our own software’s functionality.  This
obviously means staying aware of functionality changes and improvements in new
releases, but it also means staying aware of issues and bugs that might
require fixes in order to address problems propagated through the dependency
into our own software.  In an open source community, we may be the best people
to implement those core technological fixes, and we should be ready to do so,
if necessary.


## Current & Future

We are currently still organizing and conducting the Python Tutorial Seminar
Series.  We are about to conclude our program leading attendees from Python
basics to advanced Xarray and Dask.  The program will continue with more
advanced topics such as advanced visualization in Python (in collaboration
with the GeoCAT team), Object Oriented Programming with Python, machine
learning with Python, and many more.  All of these tutorials are recorded and
the videos hosted for free viewing on YouTube as part of the ProjectPythia
channel.

We are currently working on the Project Funnel short-term project, which seeks
to enable a mechanism for scientists to easily cache and retrieve
"intermediate products" (or diagnostic data produced after a model run, for
example) within their workflows.  That is, after returning to a Jupyter
Notebook after weeks working on another paper or proposal, it would be ideal
for computationally expensive steps in the notebook to be "saved" and
automatically retrieved when the notebook is run again.  Such a technology
could also be modified to make it possible to share intermediate computed
products between workflows, which might make it easier for scientists to build
off of other scientists’ workflows.  This project is being conducted in
collaboration with Matt Long in CGD, and it is also being used as a means of
developing the Team Processes and determining how we can work best together.


### Selecting Future Projects

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
