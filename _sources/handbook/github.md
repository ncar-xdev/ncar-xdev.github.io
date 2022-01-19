# How we use GitHub

GitHub is an essential part of how we work.  It is *where* we work, and it defines so much of *how* we work.  As a result, it deserves special attention.  Hence, this page is dedicated to how we use GitHub and, if you are an external collaborator, how you can use GitHub to collaborate with *us*.

Think of this page as describing a "*Day in the Life of an Xdever*".

## Step 1: Catching up

The first step is to use GitHub to learn about what other team members have been doing.  That is, use GitHub to follow up with *what has been done*, *what is being done*, and *what is still to do*.

There are two useful places to catch up with the group:

- [The Xdev Project Board](https://github.com/orgs/ncar-xdev/projects/1): This is a GitHub Project board, in the *new* style.  That is, it displays all of the Issues and Pull Requests across all repositories in the NCAR-Xdev organization, as well as any Issues or Pull Requests in repositories outside the organization that we *added to the board manually.*  You can view the board in tabular form by clicking the *Table* view tab, or you can view the board in a traditional Kanban-style board by clicking the *Board* view tab.  The *Board* view gives you a visually immediate view of *what has been done* (i.e., in the "Done" column), *what is being done* (i.e., in the "In Progress" column), and *what is still to do* (i.e., in the "Todo" column).  The *Table* view allows you to search and sort in various ways that can be extremely useful.

  The advantage to using the Project Board is that you can see all *tasks* related to Xdev work.  Each Issue is a task that is *done* or *to be done* or *is being addressed*, and each Pull Request is work that should reference a task (i.e., issue) that is not done.  Multiple Pull Requests can be created and merged to address a single Issue, and even multiple issues can sometimes be addressed by a single Pull Request (though this is many times due to duplication, which should be avoided).

  The disadvantage to using the Project Board is that it doesn't immediately show you the conversations taking place on each Issue or Pull Request.  Thus, the Project Board can look unchanged, even when a flurry of activity is happening in conversations and commits to Pull Request branches!

- [GitHub Notifications](https://github.com/notifications): Your GitHub Notifications inbox is another great way of catching up with the group.  If you *watch* all repositories in the NCAR-Xdev organization, you will be notified of any activity (new Issues, new Pull Requests, new comments on existing Issues and Pull Requests, etc.) on the given repository.  (Note that you may have to manually *watch* each repository, since there is no way to automatically watch all repositories for a given organization with a single click.  However, we recommend that you manually manage your watch list, anyway.)  Clicking on the "bell icon" at the top-right of the GitHub page will take you to your notifications inbox, where you can see all of your recent notifications like they were emails.

  The advantage to using GitHub notifications is that it shows you any contributions to conversations taking place on Issues and Pull Requests, including new commits and code contributions.  Thus, GitHub notifications give you an excellent view of *what's new* going on in the Xdev space.

  The disadvantage to using GitHub notifications is that it doesn't show you a view of *still to be addressed Issues*, and therefore notifications don't help you determine *what to do next*.

  :::{admonition} Filter your notifications!
  :class: tip
  If you use GitHub for non-Xdev things, it can get overwhelming with notifications coming from all over GitHub.  For this reason, it can be very useful to create [*custom notification filters*](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox#customizing-your-inbox-with-custom-filters) to separate out all of the Xdev notifications from the rest.  You can easily do this by creating a filter on "`org:ncar-xdev`".  You can create another filter that even separates out any Xdev notifications that *@mentions* you or a team you are on by filtering on "`org:ncar-xdev reason:mention reason:team-mention`".  And if you want to include any review requests in that filter, just add `reason:review-requested` to the filter.
  :::

Each individual approach above is useful in its own right, but neither one is ideal.  Together, however, they present a useful way of staying up to date with what everyone is doing on team!  It is *highly advised* that you keep up with the team using these approaches on a regular bases, such as a little time every morning or before you are about to start any Xdev work for the day.

## Step 2: Decide what to do

After getting an understanding of what other people are working on and what still needs to be done ([Step 1](#step-1-catching-up)), you need to pick something to do *yourself*.  There are three *good reasons* to choose something to do:

1. **You are already doing it!**  That is, you have already started a larger effort and it needs to be finished.  If it hasn't stalled or hit a blocking issue that is waiting on resolution, you should continue work on this task until it is done.

   As a good rule of thumb, you should only have one or two tasks that are *in progress* at any time.  Finish the tasks you are working on before moving on to another.

1. **It is urgent or high-priority.**  If you find a few good next tasks from the list of *todo* Issues on an Xdev repository, then choose one that is urgent or high-priority.  If you find a task that you think should be urgent or high-priority, but it isn't labelled with an `urgent` or `high priority` label, then you can either *ask if it should be labelled `urgent` or `high priority` in the Issue itself* or you can just take the initiative and label it `urgent` or `high priority` and start working on it.

1. **It is a challenge.**  Xdev cannot work well if all of the expertise for a specific topic is in the head of only one person!  If you think something will be hard for you to do, but easier for some else, *don't shy away*!  Instead, *ask the expert* to meet with you to discuss how to approach the issue and then *do it yourself.*  Remember that we are there for each other, and that it is our job for the betterment of the community and to NCAR if we let ourselves grow and learn.  The best way to learn is by doing it!

Once you have selected something to do next, **assign yourself to the selected Issue**.  This is a good way of letting people know who is working on addressing a given Issue.

:::{admonition} You don't have to always choose Issues!
:class: tip
There will be plenty of times when you realize that something that needs to be done *isn't on the *todo* list!*  That's okay.  When you realize that something is missing, then just add it yourself (i.e., create a new Issue in the appropriate repository).  And if you want to add an Issue and then immediately start working to address it, that's great!  However, always remember to add an Issue before you start working.  Ideally, all of our Pull Requests should *reference* an existing Issue.
:::

### Xdevdome: *Two devs enter, One team leaves!*

If you're familiar with the old movie [Max Max Beyond Thunderdome](https://en.wikipedia.org/wiki/Mad_Max_Beyond_Thunderdome), you will know the single rule of the Thunderdome is ["two men enter, one man leaves"](https://www.youtube.com/watch?v=9yDL0AKUCKo).  Well, Xdev isn't really competitive in nature, and it *certainly* isn't a bloodsport!  Instead, Xdev encourages more of a cheesy "two devs enter, one team leaves" attitude.

What we mean by this is that we are about trying to build collaboration rather than exclude people.  So, if the most interesting "next step" *to you* is an Issue that someone has already assigned themselves to, then go ahead and assign yourself to the Issue, too.  How does this work in practice?

When you assign yourself to an Issue that already has someone assigned to it, it is your responsibility to contact that person using a *direct mention* (i.e., @mention the GitHub user) in that Issue's conversation.  You should tell the person that you are interested in helping out and that you'd like to discuss with them about how you can do that.  You should then either discuss it *asynchronously* (i.e., in the Issue conversation) or *synchronously* in a video meeting, if possible.  During this conversation, you should:

- Talk about what there is left to work on.
- Talk about how the remaining work can be divided up.
- Share the remaining workload and tackle it as a team.

There are times when some tasks just can't really be divided up, though!  When that is the case, then the two teammates should discuss who will *finish* the task.  It's okay to hand off the task to someone else, if that seems appropriate.  You can also choose to finish the task *together* in a pair programming session.  That can be an excellent way of helping other teammates learn from each other and grow as developers.  Just remember to come to those pair programming sessions prepared!

## Step 3: Share your plans

Once you've decided what you are going to work on next, it is your job to share your plans with the rest of the team.  To do this, we have created a [GitHub Team Discussions board](https://github.com/orgs/ncar-xdev/teams/all/discussions).  Just post in the discussion what you've decided to start working on.  You don't have to include any great detail here!  In fact, all of the details about *how* you intend to do what you are going to do should be detailed in Issues or Pull Requests.  However, you should reference those Issues or Pull Requests in your discussion post!

## Step 4: Do the work

Once you've decided what you are going to do, and you have shared your plans with the team, it's time to start working.  You should make sure that you have an up-to-date fork of the repository you plan to work in, and that you have cloned and pulled down the most recent changes of this fork to your local workspace.  You should make sure that you have an up-to-date environment for the work (e.g., conda), and that you have all the appropriate tools needed for the specific repository, including testing tools (e.g., pytest), linting tools (e.g., pre-commit), etc.  Verify that the testing and development tools in your environment work before starting to do development.

Follow the normal git best practices, and push changes up to your fork only when you know that things are working.  If you are adding lines of code, make sure those lines of code are being tested!  If you are deleting lines of code, make sure those deletions aren't changing any existing tests (or, if appropriate, change the tests accordingly).  If you've added a feature, make sure that some form of documentation (e.g., API documentation) is being added to the package.

:::{admonition} Create Draft Pull Requests early!
:class: tip
You can create a Pull Request for new work in your fork *at any time.*  If you want, you can create the Pull Request only when you are pretty confident that you are close or ready to merge into the main branch.  However, we recommend creating your Pull Requests in *draft mode* at an early stage, possibly even after your very first commit to your fork's branch.  Sharing your Pull Requests with the rest of the team helps other people follow along with what Xdev is doing!  And it helps us learn from each other *while* we are doing our work.
:::

## Step 5: Merge

Once you thing you have a Pull Request that is ready to merge, convert your Pull Request to from a *draft* to a regular Pull Request.  If this does not automatically trigger reviews on your Pull Request from the team, then select a couple people to review your work.  Try not to alway select the same people, though!  It's good to share the review workload around.

At this point, someone on the team should review your Pull Request.  If nobody is reviewing your Pull Request after a day of waiting, give the selected reviewers a gentle nudge with a *direct mention* in the Pull Request conversation.  If the selected reviewer is just too swamped to get to it within 24 hours of receiving the notification, then the reviewer should suggest another reviewer for the Pull Request.  If the selected reviewer has time to conduct the review, but it might take them a while, then the reviewer should let the author of the Pull Request know that they are looking at it and that it might take a little bit.

:::{admonition} Make sure reviews are thorough!
:class: tip
Make sure you take the time to conduct *thorough* reviews!  Reviews can involve a lot of learning before you can make sense of them, if you haven't been following along with the work previously.  *Take the time to learn* from other people's Pull Requests during your reviews!
:::

Once your Pull Request is passing all tests and has at least one approval (and no requests for changes from other people!), then merge the Pull Request.  If a Pull Request is authored by someone with *write* permissions on the repository, then the author of the Pull Request should merge the Pull Request.  If the author doesn't have *write* permissions, through, they should ping someone who *does* have *write* permissions (possibly a reviewer) to merge the Pull Request for them.

## Step 6: Celebrate!

You've now contributed to open source!  Yay!  Celebrate!

Give yourself some time to rest and recouperate.  Catch up on your email.  Disconnect for a little bit and recenter yourself.

Now, go back the beginning and start again.
