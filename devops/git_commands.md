
	git init:
		this command will create a new git tracking directory (called .git) to track versions of any files you add to that directory.

	git clone:
		this command will take a copy of an existing repository stored on github.com, and download it to your local computer in the folder youre currently in.
		if you go to https://github.com/outdreamer/finder/ and click on clone or download, you can get the url to use with the git clone command:

		git clone https://github.com/outdreamer/finder.git

		when you download a git repo with this command, you also get the .git folder that tracks all of the file changes saved for that repository. 

	git remote add
		this command lets you specify a repo to push to

		git remote add <remote_name> <remote_repo_url>

		git remote add origin my_url

	git remote set-url https://github.com/turtle20/test.git
		this command changes the remote repository of the local copy - I dont think we needed to run this command, we just needed to set your user config
		https://help.github.com/articles/changing-a-remote-s-url/

	git config
		These were the commands we used to set your user name & email so git could identify your user:

		git config --global user.name "My name"
		git config --global user.email "myemail@gmail.com"

	git checkout -b my_new_branch
		this command creates a new branch, which is a copy of the original branch
		- you'd run this command if you were working on the same repo with other developers, so you could make changes on a different branch,
			and then when you were done with the changes, you could merge it into the original branch once you were sure its unlikely your changes would break 
			anyone's code.

	git pull
		this command pulls all recent changes made to the remote repository that arent already on your local copy
		- youd use this command if you were working with other developers on the same repo, to pull their changes.
		- youd also use it if you had a dev environment set up on another computer, so you could pull your own changes to the other computer to update a site for example.

	git push 
		this command pushes your local changes added with git add & committed with git commit, to the remote repository, so youll see it on the github.com site.

		git push -u <remote_name> <local_branch_name>

		git push -u origin my_new_branch 

	git status
		shows you whether files have been changed & if those changes have been saved
	
	git add
		saves changes to a file

		git add particular_file.txt (to add changes to a particular file at a time)
		git add . (to add all your changes)

	git commit -m "my commit message"
		this command groups changes together with a message

	git log
		this command shows you a list of your previous commmits, which you can exit with :q

	git branch
		tells you which branch (copy of the code) youre working on
		the default branch is master

	git checkout -b new_branch_name
		adds a new branch, creating a copy of whichever branch you were working on & switching to the new branch



#- merge: integrate changes from newly developed features (like new-feature-branch) with latest commit from target branch to merge to (like master)
#- rebase: replay changes from newly developed features (like new-feature-branch) on common commit from target branch to merge to (like master)


# remove large files

# find large files
du -a ./docs | sort -n -r | head -n 20

# go through all commits, removing the file & any of its empty commits, overwriting existing tags
git filter-branch --force --index-filter  "git rm -r --cached --ignore-unmatch .config" --prune-empty --tag-name-filter cat -- --all

# go through all commits, recursively removing all files in path & any of its empty commits, overwriting existing tags
git filter-branch --force --index-filter  "git rm -r --cached --ignore-unmatch path/directory" --prune-empty --tag-name-filter cat -- --all

# add file to .gitignore

# force push local changes
git push origin --force --all

# remove file from tagged releases
git push origin --force --tags

# rebase
git checkout new_branch
git rebase master

# force all objects in your local repository to be dereferenced and garbage collected 
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now


cat [filename] 	Display file’s contents to the standard output device
(usually your monitor).
cd /directorypath 	Change to directory.
chmod [options] mode filename 	Change a file’s permissions.
chown [options] filename 	Change who owns a file.
clear 	Clear a command line screen/window for a fresh start.
cp [options] source destination 	Copy files and directories.
date [options] 	Display or set the system date and time.
df [options] 	Display used and available disk space.
du [options] 	Show how much space each file takes up.
file [options] filename 	Determine what type of data is within a file.
find [pathname] [expression] 	Search for files matching a provided pattern.
grep [options] pattern [filesname] 	Search files or output for a particular pattern.
kill [options] pid 	Stop a process. If the process refuses to stop, use kill -9 pid.
less [options] [filename] 	View the contents of a file one page at a time.
ln [options] source [destination] 	Create a shortcut.
locate filename 	Search a copy of your filesystem for the specified
filename.
lpr [options] 	Send a print job.
ls [options] 	List directory contents.
man [command] 	Display the help information for the specified command.
mkdir [options] directory 	Create a new directory.
mv [options] source destination 	Rename or move file(s) or directories.
passwd [name [password]] 	Change the password or allow (for the system administrator) to
change any password.
ps [options] 	Display a snapshot of the currently running processes.
pwd 	Display the pathname for the current directory.
rm [options] directory 	Remove (delete) file(s) and/or directories.
rmdir [options] directory 	Delete empty directories.
ssh [options] user@machine 	Remotely log in to another Linux machine, over the network.
Leave an ssh session by typing exit.
su [options] [user [arguments]] 	Switch to another user account.
tail [options] [filename] 	Display the last n lines of a file (the default is
10).
tar [options] filename 	Store and extract files from a tarfile (.tar) or tarball (.tar.gz or .tgz).
top 	Displays the resources being used on your system. Press q to
exit.
touch filename 	Create an empty file with the specified name.
who [options] 	Display who is logged on.