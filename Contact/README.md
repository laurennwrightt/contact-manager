# COP4331-G5
This repository will contain all of the files and folders used with each of COP4331 Group 5's projects over the course of the Summer 2021 semester.
## How to use Github
For those who are relatively new to github, I'll add the basics here so you have a quick and easy place to find the necessary information on how to use this platform.
### 1 - Getting Started:
1. Make sure to install the [Git Bash Client](https://git-scm.com/downloads).
2. In order to be able to interact with our repository from your computer, you'll need to set up an SSH key and save it on the github website as a way to tell github that your computer has permission to interact with our repository through your account. Follow [this tutorial](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and then [this tutorial](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
### 2 - Cloning the Repository to your Computer
1. Navigate to the repo's main page on github and look for the green code button. CLick it and toggle to SSH ![Example](https://docs.buddybuild.com/repository/github/img/click-use-ssh.png)
2. Copy the link. It should start with *git@github*. You'll use this in a bit.
3. Open file explorer and navigate somewhere on your computer where you would like the repository to be placed (I **do not** recommend putting it on your desktop). Once there, right click and select ***Git Bash Here***. That should open up a fancy little command prompt window. You can use powershell or basic command line, but this was made specifically for git and is called Git Bash.
4. In the Git Bash window enter: `git clone <SSH Link>` Where SSH Link is the git@github link you copied from github (Don't include the <>). Press enter. You should now see a folder called COP4331-G5 in your file explorer with this readme document inside it. Congrats you just got the ability to commit code to the repo! If this didn't work then **F**.
### 3 - Interacting with the Repository
So all of your primary git commands can be done from within git bash. The big ones you'll be using are fetch, pull, status, add, commit, and push.
* **git fetch** will update your computer with the current state that the online repository is in. So if Nathan makes a new branch, in order for everyone else's computers to know that the branch was created, they need to enter `git fetch` in git bash which will identify any new branches and inform your computer that they exist.
* **git checkout** allows you to switch from one branch to another. To perform the switch, run `git checkout target_branch_name` in git bash.
* **git pull** will find any changes to the current branch that you're on that you're missing and update your local repository with those changes. For example, if both Lauren and Felipe checked out the branch called random-branch on May 21st, on May 22nd Felipe pushed a change to that branch, and May 23rd Lauren decided to do some work on that branch; the version of the branch that Lauren has will be from May 21st without any of Felipe's changes. So to make sure you are always looking at the most up-to-date version of the branch, run `git pull` which woulld pull Felipe's May 22nd changes from github and put them on Lauren's local computer. Not doing this can result in merge conflicts which are a headache to resolve. git pull often.
* **git status** will show you all the changes you've added to the branch that you're on. This is useful right before you try to push your changes to the repo on github.
* **git add** after running `git status` you run `git add file_or_directory_name` for each of the changed files or folders you would like to send to the github repo.
* **git commit** will generate what's called a commit message so when you eventually push your changes to the github repo, they come with a description of what the changes did. The format for this command is `git commit -m "Your message goes in here"`
* **git push** will take your commit message and your added files and folders, then send them to github. Simply enter `git push` after running git commit.
### 4 - Repository Structure
In our github repository you'll notice at the top left there is a word, most likely develop. If you click it, you'll get a list of branches that exist in our repo:


![Example2](https://sarafordnet.files.wordpress.com/2016/12/image90.png)

By default we have two branches. **main** and **develop**. We will ***Never in your entire life or for any reason whatsoever and in zero alternate timelines directly commit and push changes to main***. Main serves as our release branch. It's where our absolute finished product goes. It will be made up of an amalgamation of pull requests from branches that are made from and merged back into **develop** and only once **develop** is in a release state will we then merge it back into main. So basically what we'll do is anytime we need to make a branch, we will make it off of develop. Once that branch works and is complete we will merge it back into develop. develop will then be an amalgamation of all of our branches, and once all of the work is done we'll test develop, and if it works, merge to main.
# contact-manager
