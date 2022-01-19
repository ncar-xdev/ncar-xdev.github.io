# GitHub Glossary

Knowing how to *use* GitHub on a day-to-day basis is one thing (see [How we use GitHub](github)), but knowing all of the necessary components is another.  Most of the components are *mentioned* in the [How we use GitHub](github)) section, but it's worth while to list the components in more explicit detail so you have a "lay of the land."

## Organization

To keep us from being too scattered, we have opted to do all of our work (or as much as possible) in our own GitHub organization: [ncar-xdev](https://github.com/ncar-xdev).  If you are a core member of the Xdev Team, you should already be a member (or owner) of the GitHub organization.  If you are a collaborator working with Xdev on a specific project, you should request to be added to the project repositories, as needed.

:::{admonition} Tip
:class: tip
You don't have to be a member of a repository's organization to create a fork of that repository *as long as it is public*!  That also means you do not have to be a member of the organization to submit a Pull Request!  You just won't be able to merge the Pull Request yourself.
:::

## Team

As part of our GitHub organization, we are all on a GitHub Team: `@ncar-xdev/all`.  You can use this team name to @mention the entire team on Issues or Pull Request conversations to draw their attention and to indicate that your attention is important.  More specific teams can be created for individual repositories or projects, but this is the "catch-all" team for everything we do.

:::{admonition} Quick Link
:class: note
[Xdev Team](https://github.com/orgs/ncar-xdev/teams/all)
:::

## Discussions Page

Through this GitHub Team, we also engage in [Team Discussions](https://github.com/orgs/ncar-xdev/teams/all/discussions).  The Team Discussions page should be used every day to share with the rest of the team *what you are planning to do that day.*  This is, in essence, an asynchronous stand-up meeting, and it is a good way for the team to keep in touch with each other and to build an understanding of what we are doing on any given day.

:::{admonition} Quick Link
:class: note
[Team Discussions](https://github.com/orgs/ncar-xdev/teams/all/discussions)
:::

## Project Board

All new [Issues](#issues) and [Pull Requests](#pull-requests) created on repositories in our GitHub organization will be added as items on the [Xdev Tasks](https://github.com/orgs/ncar-xdev/projects/1) GitHub Project.  Issues pertinent to Xdev activities or projects that happen on repositories in other organizations should be added to the project board manually.

On the project board, you can toggle back and forth between a standard Kanban-style *Board* or *Table* view.  Use this project board as a way of seeing visually everything that the team has *to do* and everything the team *is doing*!

:::{admonition} Quick Link
:class: note
[Xdev Tasks Project Board](https://github.com/orgs/ncar-xdev/projects/1)
:::

## Repositories

Within our GitHub organization, we have repositories for our main website (*this site!*) and repositories for our projects (one repository per project).  The main website repository is different from the project repositories, so we will describe that one first.

### Main Website: `ncar-xdev.github.io`

This repository is the main website.  It is a [Jupyter Book](https://jupyterbook.org) and it uses the [Sphinx Pythia Theme](https://sphinx-pythia-theme.readthedocs.io).  This site houses this handbook, background information about Xdev and Pangeo, and our status and metrics pages.

On the repository itself, there are four kinds of [Issues](#issues) that can be created:

- **Bug Reports:** These are issues that describe problems on the site, either actual display or rending issues, incorrect information, typos, problems with CI, etc.  These issues are labeled `bug`.
- **Enhancement Proposals:** These are issues that detail new enhancements to the site, such as a new page, new CI, new sections, etc.  These issues are labeled `enhancement`.
- **Project Proposals:** These are special issues that detail *pitches* for Xdev [Short-Term Projects](about/xdev#short-term-projects).  These issues detail the *problem* the project will solve, what the proposed *solution* will look like, and any *additional requirements* needed to declare the project a success.  These issues are labeled `project`.
- **General:**  General issues are any issues that do not fall into any of the above categories.  This is a "catch-all" category and these issues are identified as *not* having any of the other three labels.

There are issue templates for each of these three kinds of issues.

### Comments on Main Website: `ncar-xdev-utterances`

This repository is used by [utteranc.es](https://utteranc.es/) to provide a mechanism for public comments on our main site.

### Project Repositories

For almost every project that we do in Xdev, whether they are "official" Short-Term Projects or just ongoing activities, there is a repository in the [NCAR-Xdev GitHub Organization](#organization).  Some activities are actually done in different organizations, but we try to keep as much as possible in our organization.  Even if work is scattered across other repositories, the repositories in our organization are used to keep us organized and less scattered.  That means that some project repositories may not have any actual code!  In fact, they may just be *meta repositories* used just to contain Issues that we use to track our progress and keep our tasks cleanly separated from other tasks.

While each project repository can vary depending upon the project, it is safe to assume that each repository has four different kinds of issues:

- **High Priority:** This means that the issue is extremely important, possibly blocking of other development, and that it should be prioritized if at all possible.  These issues are labeled `high priority`.
- **Low Priority:** This means that you shouldn't bother with this right now.  There are other more important things to consider unless you know that addressing this issue is incredibly easy or if there is nothing else to do.  These issues are labeled `low-priority`.
- **Bug Report:** This means there is a bug (incorrect behavior) in the project code.  If the project repository is a *meta repository*, and the actual code is in another repository, then the Issue in the project repository should point to an actual issue in the code repository.  These issues are labeled `bug`.
- **Enhancement Proposal:** These Issues are for new features that should be added to the project.  They may point to Issues in other repositories.  These Issues are labeled `enhancement`.

## Issues

Issues on repositories represent *tasks* that need to be done (or are done, if they are closed Issues).  When you choose to work on addressing a given Issue, you should *assign yourself* to the Issue to indicate that you will be working on it.  If someone else has already assigned themselves to an Issue you want to work on, don't worry!  You can collaborate.  Refer to the [Xdevdome Rule](github#xdevdome-two-devs-enter-one-team-leaves) for how to deal with this kind of situation.

:::{admonition} Label issues appropriately!
:class: warning
Please label all new issue appropriately when they are created.  This helps the team decide what they need to work on next.  If you need help deciding an Issue's priority, ping the entire [team](#team) on a comment in the Issue to ask for a decision.
:::

Remember that once you realize that something needs to be done in a project or on a specific repository, you should create an issue for that task in the appropriate repository so that others might be able to help address it.

## Pull Requests

Pull Requests on repositories represent *tasks* that are being worked on *right now*.  Every Pull Request should reference and be connected to a given [Issue](#issues).  A single Pull Request need not close an Issue, as multiple Pull Requests might need to be completed before an Issue is completely resolved.  Usually, a single Pull Request will not close *multiple* Issues, but it is possible, for example, if multiple *Bug Reports* are created for the same piece of code.

:::{admonition} Pull Requests don't need self-assignment!
Who is working on a Pull Request is usually obvious.
:::

One approving review should be conducted before any Pull Request is merged.  Please remember to be thorough in your reviews!  Also, remember to spread reviews out so that one person is not doing all of the reviews.

## Notifications

GitHub notifications can be *extremely useful* for keeping up with what is happening in Xdev!  They are also extremely useful for communicating with other members of the team.  Team members should *direct mention* (@mention) anyone whenever they need that person's input or advice.  When *you* are direct mentioned, you should prioritize responding to those notifications so as not to block progress in the team.  Direct mentions should be responded to with the same priority as requests for reviews.

However, GitHub notifications can also be incredibly overwhelming.  To help keep you focused on Xdev-related work *only*, we recommend [creating custom filters](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox#customizing-your-inbox-with-custom-filters) on your [GitHub notifications page](https://github.com/notifications) (which can be found by clicking on the "bell" icon at the top right).  You can filter your notifications on all Xdev Organization repositories with the `org:ncar-xdev` filter, and you can filter on Xdev Organization notifications that directly mention you (either with an @mention, a team @mention, or review request) with the `org:ncar-xdev reason:mention reason:team-mention reason:review-requested` filter.

We also recommend automatically watching repositories and teams (for discussions) and manually removing repositories you choose not to watch as well as disabling all email notifications on using only the GitHub notifications page.
