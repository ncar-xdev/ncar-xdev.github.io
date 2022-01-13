# Processes

:::{warning} **TODO:**
This page should detail what processes we use to do our work.  That includes
that everything should be public on GitHub, and that we have weekly meetings
on Wednesdays at 3PM.  Changes to our processes can be suggested with modifications
to this document.

Currently, this document contains the contents of the old "How we work" document
contained on HackMD, which is *wildly* out of date.
:::

## The Point

This process document is meant as a guide for Xdev Project Team members on how to work on Xdev Projects and work together as a team.

The processes described in this document are shaped by our team process values.

### Team Process Values

- It is preferable for the whole team to move forward slowly *together* than it is for one or two people to move forward quickly while others do nothing.
- Allow the team to continue to make progress even when others are out or unavailable.
- Be accommodating of team members schedules and let them read and respond to communication in their own time.
- Use synchronous communication (e.g., video meetings/calls) for what is best: real-time collaboration (e.g., pair programming).
    - Recall the [Xdev Communication Plan](https://github.com/NCAR/xdev/blob/main/COMMPLAN.md) (todo: add Trello to `COMMPLAN.md`)


## Trello

### Project Board

- **The [Trello board](https://trello.com/b/ul7PB0wv/xdev-team) is to be considered the "fount of knowledge" regarding the project.**
- All relevant GitHub issues/PRs, documents (e.g., HackMD), and other information *not* contained explicitly in the board should be referenced or attached to cards on the board.
    - You can add a Github issue/PR by copying the link to that issue or PR, and pasting in the "add a link" section of the card you are attaching it to
- Collaboration and discussions around project activities should happen on the board, in the comments section of the relevant card.
- Keep up to date with changes on the board by using the "Activity" section of the Board Menu (top right).

### Trello Board How-To

The Trello board is divided into multiple columns called "Lists".  Each List contains "Cards."  Trello board flow works by creating cards and moving them between lists to indicate a change in context related to the card.

In the Xdev project boards, the lists are as follows:

- *Info:* Cards in this list represent addition information pertaining to the project.  This includes User Stories, reference documents, and other kinds of information.  Use these cards to help define tasks in the backlog.  Look to this list to find out what the goals of the project are and what constitutes success.
- *Backlog:* Cards in this column represent tasks that need to be done on the project. New tasks, as they are determined, will be created in this list.  Look to this list to find out what you can do next.
- *In Progress:* Cards from the Backlog list should be moved into this list once work is started on them.  The person who moved the card should also "join" the card/task at this point in time.  Look to this list to find out what people are working on now.
    - Consider having a limit of how many "in progress" cards a single person can have (2 or 3, or maybe even 1)
- *Done:* Cards in this list represent tasks that have been completed.  Look to this list to catch up on what the team has been up to over the last week.
- *Archived:* Cards in this list represent tasks that have been reviewed and archives for reference.  Cards in the Done list will be automatically moved into the Archived list at 11:59PM every Wednesday Async Day.

## Team Async Days

- Wednesdays will be Team "Async Days", when members of the team can "sync up" asynchronously with each other over the course of the day.
- Async Days are designed to remove the need for *another* Zoom meeting.
- On Async Days, members of the team are responsible for visiting the board and checking in on what their teammates have been doing.
- An automated message will be sent out every Wednesday morning from Trello summarizing what cards are "Done" and what cards are "In Progress".
- At the end of the day on Wednesday (11:59PM), Trello will automatically move all cards in the "Done" list to the "Archived" list.


## Weekly Hackathons

- In order to facilitate and encourage teammates to engage in *pair programming*, the weekly Xdev Team Time slot will be used for project hackathons.
- We will meet in the [Xdev Projects Gather Town](https://gather.town/app/NF3AQ5keuLywswp2/xdev-projects).
- Each weekly hackathon will start with a brief "Stand Up" meeting in the **Red Conference Room** in the Gather Town.
- Find partners to work with together and pair program.
- ***Remember:*** Don't just always pick the same partners!  Don't stick with the same partners for the entire hackathon!  Reach out and help each other out.  Use the hackathons to lift the team, to teach *and* get things done!

## How Should New Members / Infrequent Contributors Get Started?

- Do we need a catalog of existing projects? (Revive [`projects/`](https://github.com/NCAR/xdev/blob/main/projects/active) in the repo?)
- Look in the *Backlog* or *In Progress* column of the Trello board
    - Comment on an interesting looking card
    - Do we need a "point of contact" in the Trello cards?
